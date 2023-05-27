# Video Panoptic Segmentation 

## Video K-Net 

In our project, we use Video K-Net: a simple, strong, and unified framework for fully end-to-end dense video segmentation. 
The method is built upon K-Net, a method of unifying image segmentation via a group of learnable kernels.
[Paper](https://arxiv.org/abs/2204.04656), [Sides](./slides/Video-KNet-cvpr-slides-10-25-version.pptx), [Poster](./slides/cvpr22_poster_lxt_zww_pjm.pdf), [Video](https://www.youtube.com/watch?v=LIEyp_czu20&t=3s)


This project contains the training and testing code of Video K-Net for VPS (Video Panoptic Segmentation).


### Environment and DataSet Preparation 

The requirements to run the repo can be found in "requirements.txt".

We have also built a [docker image]() with all these requirements for ease of use.

As for the dataset preparation, please refer to DATASET.md for all the steps to follow to prepare the three datasets used.


### Scripts

1. First pretrain K-Net on Cityscapes-STEP datasset. As shown in original STEP paper(Appendix Part) and our own EXP results, this step is very important to improve the segmentation performance.
You can also use our trained model for verification.

Cityscape-STEP follows the format of STEP: 17 stuff classes and 2 thing classes. 

```bash
# train cityscapes step panoptic segmentation models
sh ./tools/slurm_train.sh $PARTITION knet_step configs/det/knet_cityscapes_step/knet_s3_r50_fpn.py $WORK_DIR --no-validate
```

2. Then train the Video K-Net on KITTI-STEP. We have provided the pretrained models from Cityscapes of Video K-Net.

For slurm users:

```bash
# train Video K-Net on KITTI-step using R-50
GPUS=8 sh ./tools/slurm_train.sh $PARTITION video_knet_step configs/det/video_knet_kitti_step/video_knet_s3_r50_rpn_1x_kitti_step_sigmoid_stride2_mask_embed_link_ffn_joint_train.py $WORK_DIR --no-validate --load-from /path_to_knet_step_city_r50
```

```bash
# train Video K-Net on KITTI-step using Swin-base
GPUS=16 GPUS_PER_NODE=8 sh ./tools/slurm_train.sh $PARTITION video_knet_step configs/det/video_knet_kitti_step/video_knet_s3_swinb_rpn_1x_kitti_step_sigmoid_stride2_mask_embed_link_ffn_joint_train.py $WORK_DIR --no-validate --load-from /path_to_knet_step_city_r50
```

Our models are trained with two V100 machines. 

For Local machine:

```bash
# train Video K-Net on KITTI-step with 8 GPUs
sh ./tools/dist_train.sh video_knet_step configs/det/video_knet_kitti_step/video_knet_s3_r50_rpn_1x_kitti_step_sigmoid_stride2_mask_embed_link_ffn_joint_train.py 8 $WORK_DIR --no-validate
```


3. Testing and Demo.

We provide both VPQ and STQ metrics to evaluate VPS models. 

```bash
# test locally 
sh ./tools/dist_step_test.sh configs/det/knet_cityscapes_ste/knet_s3_r50_fpn.py $MODEL_DIR 
```

We also dump the colored images for debug.

```bash
# eval STEP STQ
python tools/eval_dstq_step.py result_path gt_path
```

```bash
# eval STEP VPQ
python tools/eval_dvpq_step.py result_path gt_path
```


### Pretraining and training checkpoints

The checkpoints for our pretraining and training can be found in [this folder](https://drive.google.com/drive/folders/1l1rVqQaE6VCfgHc50QEUXW-4EbYqokN2?usp=sharing) on Google Drive.


| Checkpoint name                           | Refers to                                                                 |
|-------------------------------------------|---------------------------------------------------------------------------|
| knet_pretraining_fpn_8                    | K-Net training on Cityscapes dataset with increased FPN layers            |
| video_knet_training_fpn_8                 | Video-K-Net training on Kitti-step dataset with increased FPN layers      |
| video_knet_baseline                       | Video-K-Net training on Kitti-step dataset with baseline model            |
|                                           | and pretraining baseline checkpoint                                       |
| video_knet_baseline_modified_pretraining  | Video-K-Net training on Kitti-step dataset with baseline model            |
|                                           | and modified pretraining (knet_pretraining_fpn_8) checkpoint              |
| video_knet_baseline_modified_training     | Video-K-Net training on Kitti-step dataset with modified model            |
|                                           | (8 FPN layers) and pretraining baseline checkpoint                        |


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

