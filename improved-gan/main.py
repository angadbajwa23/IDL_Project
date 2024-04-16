from inception_score.model import get_inception_score
import os
from PIL import Image
import numpy as np
image_arrays = []
image_folder_path = '../models/coco_AttnGAN2/valid/single'
i=0
for filename in os.listdir(image_folder_path):
    i+=1
    #print(i)
    if i%100!=0:
        continue
    folder_path = os.path.join(image_folder_path, filename)
    for folder in os.listdir(folder_path):
        img_path = os.path.join(folder_path,folder)
        
        if os.path.isfile(img_path):
            # Open the image with PIL
            with Image.open(img_path) as img:
                # Convert the image to RGB (in case it's not already in this format)
                img = img.convert('RGB')
                #print(img.size)
                
                # Convert the PIL image to a numpy array
                img_array = np.array(img)
                
                # Add to your list
                image_arrays.append(img_array)
print(image_arrays)

inc_score_mean, inc_score_variance = get_inception_score(image_arrays, splits=10)
print(inc_score_mean,inc_score_variance)