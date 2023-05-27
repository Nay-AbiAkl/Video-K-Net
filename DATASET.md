The Cityscapes, KITTI-STEP, and Waymo datasets were used for the pretraining and training in our project.
The preparation of each dataset is explained below.


The final dataset folder looks like this. 
```
root
├── kitti_out
├── video_sequence
│   ├── ├── train
│   ├── ├── val

├── waymo_out
├── video_sequence
│   ├── ├── train
│   ├── ├── val

├── Video-K-Net
│   ├── data
│   ├── ├── cityscapes
```

# KITTI-STEP for Video-K-Net training

## KITTI-STEP dataset

KITTI-STEP extends the existing
[KITTI-MOTS](http://www.cvlibs.net/datasets/kitti/eval_mots.php) dataset with
spatially and temporally dense annotations. KITTI-STEP dataset provides a
test-bed for studying long-term pixel-precise segmentation and tracking under
real-world conditions.

## Label Map

KITTI-STEP adopts the same 19 classes as defined in
[Cityscapes](https://www.cityscapes-dataset.com/dataset-overview/#class-definitions)
with `pedestrians` and `cars` carefully annotated with track IDs. More
specifically, KITTI-STEP has the following label to index mapping:

Label Name     | Label ID
-------------- | --------
road           | 0
sidewalk       | 1
building       | 2
wall           | 3
fence          | 4
pole           | 5
traffic light  | 6
traffic sign   | 7
vegetation     | 8
terrain        | 9
sky            | 10
person&dagger; | 11
rider          | 12
car&dagger;    | 13
truck          | 14
bus            | 15
train          | 16
motorcycle     | 17
bicycle        | 18
void           | 255

&dagger;: Single instance annotations are available.

The groundtruth panoptic map is encoded as follows in PNG format:

```
R = semantic_id
G = instance_id // 256
B = instance % 256
```

## Prepare KITTI-STEP for Training and Evaluation

KITTI-STEP has the same train and test sequences as
[KITTI-MOTS](http://www.cvlibs.net/datasets/kitti/eval_mots.php) (with 21 and 29
sequences for training and testing, respectively). Similarly, the training
sequences are further split into training set (12 sequences) and validation set
(9 sequences).

In the following, we provide a step-by-step walk through to prepare the data.

1.  Download KITTI-STEP images from their
    [official website](https://www.cvlibs.net/datasets/kitti/eval_step.php) and unzip.

    ```bash
    wget ${KITTI_LINK}
    unzip ${KITTI_IMAGES}.zip
    ```

2.  Download groundtruth KITTI-STEP panoptic maps from
    [here](https://storage.googleapis.com/gresearch/tf-deeplab/data/kitti-step.tar.gz).

    ```bash
    # Goto ${KITTI_STEP_ROOT}
    cd ..

    wget https://storage.googleapis.com/gresearch/tf-deeplab/data/kitti-step.tar.gz
    tar -xvf kitti-step.tar.gz
    mv kitti-step/panoptic_maps panoptic_maps
    rm -r kitti-step
    ```
3. Prepare the dataset using the provided script:

    ```bash
    python scripts/kitti_step_prepare.py
    ```

Make sure to change the paths in the mentioned script to the directories where the data was downloaded.

## Cityscapes dataset for pretraining K-Net

### Cityscapes dataset

Cityscapes dataset is a high-resolution road-scene dataset which contains 19 classes. 
(8 thing classes and 11 stuff classes). 2975 images for training, 500 images for validation and 1525 images for testing.

The expected datastructure for Cityscapes dataset is:
```
cityscapes/
  gtFine/
    train/
      aachen/
        color.png, instanceIds.png, labelIds.png, polygons.json,
        labelTrainIds.png
      ...
    val/
    test/
    # below are generated Cityscapes panoptic annotation
    cityscapes_panoptic_train.json
    cityscapes_panoptic_train/
    cityscapes_panoptic_val.json
    cityscapes_panoptic_val/
    cityscapes_panoptic_test.json
    cityscapes_panoptic_test/
  leftImg8bit/
    train/
    val/
    test/
```

### Preparing Cityscapes dataset for pretraining

Install cityscapes scripts by:

```
pip install git+https://github.com/mcordts/cityscapesScripts.git
```

To create the 'labelTrainIds.png' converting the segmentation id map (origin label id maps) to trainId maps (id ranges: 0-18 for training), make sure to have the above structure, then run:
```
CITYSCAPES_DATASET=/path/to/abovementioned/cityscapes python cityscapesscripts/preparation/createTrainIdLabelImgs.py
```

To create the 'TrainIdInstanceImgs.png', run:

```
CITYSCAPES_DATASET=/path/to/abovementioned/cityscapes python cityscapesscripts/preparation/createTrainIdInstanceImgs.py
```

To generate Cityscapes panoptic dataset, run:

```
CITYSCAPES_DATASET=/path/to/abovementioned/cityscapes python cityscapesscripts/preparation/createPanopticImgs.py

```

Make sure to move all generated coco instance annotation files (.json) into the annotations folder.

Then the final folder is like this:

```
├── cityscapes
│   ├── annotations
│   │   ├── instancesonly_filtered_gtFine_train.json # coco instance annotation file(COCO format)
│   │   ├── instancesonly_filtered_gtFine_val.json
│   │   ├── cityscapes_panoptic_train.json  # panoptic json file 
│   │   ├── cityscapes_panoptic_val.json  
│   ├── leftImg8bit
│   ├── gtFine
│   │   ├──cityscapes_panoptic_{train,val}/  # png annotations
│   │   
```
