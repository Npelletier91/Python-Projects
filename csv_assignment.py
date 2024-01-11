import os
import pandas as pd

dataset_root = "C:\\Users\\Nicol\\Documents\\Python Practice\\images"

image_data = pd.DataFrame(columns=["image_path", "label"])

for root, dirs, files in os.walk(dataset_root):
    for file in files:
        image_path = os.path.join(root,file)
        
        label = os.path.basename(root)
        
        row = pd.DataFrame({"image_path": [image_path], "label": [label]})
        
        image_data = pd.concat([image_data, row], ignore_index=True)

image_data.to_csv("image_dataset.csv", index=False)
file_path = "image_dataset.csv"
os.startfile(file_path)
