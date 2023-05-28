# Video Panoptic Segmentation 

## Video K-Net 

In our project, we use Video K-Net: a simple, strong, and unified framework for fully end-to-end dense video segmentation. 
The method is built upon K-Net, a method of unifying image segmentation via a group of learnable kernels.
[Paper](https://arxiv.org/abs/2204.04656), [Sides](./slides/Video-KNet-cvpr-slides-10-25-version.pptx), [Poster](./slides/cvpr22_poster_lxt_zww_pjm.pdf), [Video](https://www.youtube.com/watch?v=LIEyp_czu20&t=3s)


This project contains the training and testing code of Video K-Net for VPS (Video Panoptic Segmentation).


### Environment and DataSet Preparation 

The requirements to run the repo can be found in "requirements.txt".

We have also built a [docker image]() with all these requirements for ease of use.

As for the dataset preparation, please refer to [**DATASET.md**](./DATASET.md) for all the steps to follow to prepare the three datasets used.


### Scripts

1. To pretrain K-Net on Cityscapes-STEP dataset.

```bash
# train cityscapes step panoptic segmentation models
sh ./tools/slurm_train.sh $PARTITION knet_step configs/det/knet_cityscapes_step/knet_s3_r50_fpn.py $WORK_DIR --no-validate
```

2. To train the Video K-Net on KITTI-STEP.

```bash
# train Video K-Net on KITTI-step using R-50
GPUS=8 sh ./tools/slurm_train.sh $PARTITION video_knet_step configs/det/video_knet_kitti_step/video_knet_s3_r50_rpn_1x_kitti_step_sigmoid_stride2_mask_embed_link_ffn_joint_train.py $WORK_DIR --no-validate --load-from /path_to_pretraining_checkpoint
```


3. Testing.

We provide both VPQ and STQ metrics to evaluate VPS models. The colored segmentation images are also saved.

```bash
sh ./tools/inference_kitti_step.sh ./configs/det/video_knet_kitti_step/video_knet_s3_r50_rpn_1x_kitti_step__sigmoid_stride2_mask_embed_link_ffn_joint_train.py $MODEL_DIR $OUT_DIR 
```

### Contributions

As stated in our project milestone, we added two contributions to the original Video-K-Net model:

1. Increase the FPN layers up to P8 to improve the segmentation accuracy. This was done for the pretraining of the K-Net and for the training of the Video-K-Net model. In fact, to be able to compare with the baseline model, we performed the following experiments:

Case A - Baseline: we use the pretrained K-Net model checkpoint and train the Video-K-Net model as is without any modifications.

Case B - Modified pretraining: we pre-train a modified K-Net model with increased FPN layers (8 layers) and train the Video-K-Net model (with the obtained checkpoint) as is without any modification.

Case C - Modified training: we use the pretrained K-Net model checkpoint and train a modified Video-K-Net model with increased FPN layers (8 layers).

Case D - Modified training and pre-training: we pre-train a modified K-Net model with increased FPN layers (8 layers) and train a modified Video-K-Net model with increased FPN layers (8 layers) with the obtained checkpoint.


2. Train on the Waymo dataset.

For the detailed results of our contributions and case studies, please refer to [**RESULTS.md**](./RESULTS.md).

### Pretraining and training checkpoints

The checkpoints for our pretraining and training can be found in [this folder](https://drive.google.com/drive/folders/1l1rVqQaE6VCfgHc50QEUXW-4EbYqokN2?usp=sharing) on Google Drive.


| Checkpoint name                           | Refers to                                                                 |
|-------------------------------------------|---------------------------------------------------------------------------|
| video_knet_baseline (case A)              | Video-K-Net training on Kitti-step dataset with baseline model            |
|                                           | and pretraining baseline checkpoint                                       |
| video_knet_baseline_modified_pretraining  | Video-K-Net training on Kitti-step dataset with baseline model            |
| (case B)                                  | and modified pretraining (knet_pretraining_fpn_8) checkpoint              |
| video_knet_baseline_modified_training     | Video-K-Net training on Kitti-step dataset with modified model            |
| (case C)                                  | (8 FPN layers) and pretraining baseline checkpoint                        |
| knet_pretraining_fpn_8 (case D)           | K-Net training on Cityscapes dataset with increased FPN layers            |
| video_knet_training_fpn_8 (case D)        | Video-K-Net training on Kitti-step dataset with increased FPN layers      |


## Citing Video K-Net

NIPS-2021, K-Net: Unified Segmentation: Our Image baseline (https://github.com/ZwwWayne/K-Net)

ECCV-2022, PolyphonicFormer: A Unified Framework For Panoptic Segmentation + Depth Estimation (winner of ICCV-2021 BMTT workshop)
(https://github.com/HarborYuan/PolyphonicFormer)

```bibtex
@inproceedings{li2022videoknet,
  title={Video k-net: A simple, strong, and unified baseline for video segmentation},
  author={Li, Xiangtai and Zhang, Wenwei and Pang, Jiangmiao and Chen, Kai and Cheng, Guangliang and Tong, Yunhai and Loy, Chen Change},
  booktitle={CVPR},
  year={2022}
}

@article{zhang2021k,
  title={K-net: Towards unified image segmentation},
  author={Zhang, Wenwei and Pang, Jiangmiao and Chen, Kai and Loy, Chen Change},
  journal={NeurIPS},
  year={2021}
}
```

