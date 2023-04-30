import json
import os

folder_path = "/Users/mariamhegazy/Desktop/repos/WaymoCOCO/work_dir/panoptic_images/"
file_list = os.listdir(folder_path)

data = {"annotations": []}

# loop to add data
for file in file_list:
    file_name = file
    image_id = file[:-4]
    segment_info = []
    annotation = {
        "file_name": file_name,
        "image_id": image_id,
        "segments_info": segment_info,
    }
    data["annotations"].append(annotation)

# save data to JSON file
with open(
    "/Users/mariamhegazy/Desktop/repos/WaymoCOCO/work_dir/annotations/waymo_panoptic_train.json",
    "w",
) as f:
    json.dump(data, f)
