# import os
# import shutil

# new_img_folder = "C:/Users/mehal/Downloads/18786Project/AttnGAN/data/coco/cat_val"
# old_img_folder = "C:/Users/mehal/Downloads/18786Project/AttnGAN/data/coco/val2014"

# filenames = os.listdir(new_img_folder)

# for file in filenames:
#     name = file.split('.')[0]
#     textfile = name + '.txt'
#     og_path = os.path.join(old_img_folder, textfile)
#     new_path = os.path.join(new_img_folder, textfile)

#     # Using shutil for copying files which is more robust than os.system with command line
#     shutil.copy(og_path, new_path)

import os
import pickle

# Path to the directory containing the text files
directory = 'C:/Users/mehal/Downloads/18786Project/AttnGAN/data/cat/val2014'

# List all files in the directory
files = os.listdir(directory)

# List to store names of all text files
file_names = []

# Iterate over each file
for file_name in files:
    # Check if the file is a text file
    if file_name.endswith('.txt'):
        # Store the file name
        file_names.append(file_name.split('.')[0])

# Serialize the list of file names to a pickle file
pickle_file_path = 'C:/Users/mehal/Downloads/18786Project/AttnGAN/data/cat/val/filenames.pickle'
with open(pickle_file_path, 'wb') as file:
    pickle.dump(file_names, file)