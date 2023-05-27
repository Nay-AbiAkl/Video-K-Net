# Video Panoptic Segmenation 



## Waymo Dataset

The second contribution is training Video-Knet on the Waymo dataset which is larger and more diverse with 5 different camera views. We aim to explore training Video-Knet on the Waymo dataset. More specifically, we aim to test once on all the 5 different views and once with 3 different camera views. Since the Waymo Open dataset is huge, we extract the same number of training images as Kitti Step which is around 10k and 5k testing dataset.

We aim to test the different in generalisation on new datasets by testing the model trained on Waymo on the kitti dataset and the other way around. We perform the cross testing to check the generalisation of the model to evaluate whether training on different camera views can increase generalisation. We assume that both datasets share the same domain knowledge and are not significantly different than each other. However, statistical analysis could be conducted to analyse whether there is a significant difference between the distributions of the features of both datasets. 

We also hypothesize that the fourth and fifth views only see the sides of the car which are often just building which do not contribute to generalisation on the front views of the kitti step dataset. Therefore, we remove the fourth and fifth views and test the difference in performance between training on 5 different cameras and 3 different cameras. We hypothesize that removing these two views could possibly even make the generalization better because both the 3-camera and 5-camera datasets have the same number of datapoints but the latter has much less of the front, front-left and front-right views. 


In order to train Video-Knet on Waymo, we had to pre-process it from scratch to match the format of the Kitti-step dataset. All the datasets trained on Video-Knet are processed to match the CoCo format including Kitti-step and Cityscape. So, we followed the same formatting by making use of the Waymo Open package. We believe this is a contribution to the community as we did not find any source online that does that from scratch. Therefore, the following files were added.


To convert Waymo to Kitti format:
```waymo_tools/Convert_waymo_to_kitti.ipynb```

The tfrecords used for the training dataset:
```waymo_tools/waymo.txt```

To ensure we have RGB and panoptic pairs of images:
```waymo_tools/check_image_pairs.py```

To delete the fourth and fifth camera views:
```waymo_tools/extract_cam_data.py```


