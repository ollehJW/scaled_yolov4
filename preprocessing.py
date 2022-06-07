# %%
import pandas as pd
from PIL import Image


# %%
bb_box = pd.read_csv("/home/jongwook95.lee/vision/Slive/ScaledYOLOv4-yolov4-csp/our_data/head-export.csv")
bb_box.head()

category_dict = dict()
category_dict['person'] = 0
category_dict['safehat'] = 1

# %%
for image_name in list(set(bb_box['image'])):
    temp_bb_box = bb_box.loc[bb_box['image'] == image_name, ['xmin', 'ymin', 'xmax', 'ymax', 'label']].reset_index(drop = True)
    name = image_name.split('.')[0]
    name_image = '/home/jongwook95.lee/vision/Slive/ScaledYOLOv4-yolov4-csp/our_data/images/train/' + name + '.jpg'
    image = Image.open(name_image)
    image_width, image_height = image.size
    name = '/home/jongwook95.lee/vision/Slive/ScaledYOLOv4-yolov4-csp/our_data/labels/train/' + name + '.txt'
    with open(name, 'w') as label_file:
        for index in range(len(temp_bb_box['xmin'])):
            category_idx = category_dict[temp_bb_box['label'][index]]
            temp = list(temp_bb_box.iloc[index, :])
            x_center = (temp[0] + temp[2])/2
            y_center = (temp[1] + temp[3])/2
            width = temp[2] - temp[0]
            height = temp[3] - temp[1]
        
            label_file.write(
                f"{category_idx} {x_center/image_width} {y_center/image_height} {width/image_width} {height/image_height}\n"
            )


# %% Normalize
