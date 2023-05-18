The Cityscapes, KITTI-STEP, and Waymo datasets were used for the pretraining and training in our project.
The preparation of each dataset is explained below.


Please prepare the data structure as the following instruction:

The final dataset folder should be like this. 
```
root 
├── data
│   ├──  kitti-step
│   ├──  coco
│   ├──  VIPSeg
│   ├──  youtube_vis_2019
│   ├──  cityscapes
```

# [VPS] KITTI-STEP

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


The groundtruth panoptic map is encoded as follows in PNG format:

```
R = semantic_id
G = instance_id // 256
B = instance % 256
```

## Image DataSet For Pretraining K-Net

### Cityscapes dataset

Cityscapes dataset is a high-resolution road-scene dataset which contains 19 classes. 
(8 thing classes and 11 stuff classes). 2975 images for training, 500 images for validation and 1525 images for testing.

Preparing cityscape dataset has three steps:

1, Convert segmentation id map(origin label id maps) to trainId maps (id ranges: 0-18 for training) using 
the official scripts [repo](https://github.com/mcordts/cityscapesScripts)

2, The run python dataset/prepare_cityscapes.py to generate the COCO-like annotations. 
This annotations can be used for Instance Segmentation training.

using csCreateTrainIdLabelImgs.py

and put the instancesonly_filtered_gtFine_train.json into annotations folder


3, For Panoptic Segmenation dataset, to generate the json file 

using csCreatePanopticImgs.py 

or you can download the our transformed .json and .png files via link: () and put the 
json file into annotations folder. 

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
