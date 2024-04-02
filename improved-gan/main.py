from inception_score.model import get_inception_score
import os
from PIL import Image
import numpy as np
image_arrays = []
image_folder_path = '../models/coco_AttnGAN2/example_captions'
for filename in os.listdir(image_folder_path):
    img_path = os.path.join(image_folder_path, filename)
    if os.path.isfile(img_path):
        # Open the image with PIL
        with Image.open(img_path) as img:
            # Convert the image to RGB (in case it's not already in this format)
            img = img.convert('RGB')
            
            # Convert the PIL image to a numpy array
            img_array = np.array(img)
            
            # Add to your list
            image_arrays.append(img_array)

inc_score_mean, inc_score_variance = get_inception_score(image_arrays, splits=10)
print(inc_score_mean,inc_score_variance)