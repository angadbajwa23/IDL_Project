import os
import pickle

# Define the directory where the files are located
directory = "C:/Users/mehal/Downloads/18786Project/AttnGAN/data/coco/val2014"

# List all files in the directory
# files = os.listdir(directory)

# # Filter out the .jpg files and extract the filenames without the extension
# image_filenames = [os.path.splitext(file)[0] for file in files if file.endswith('.jpg')]

# # Define the path for the pickle file to be saved
pickle_filename = "../data/coco/val/filenames.pickle"

# # Ensure the target directory exists
# os.makedirs(os.path.dirname(pickle_filename), exist_ok=True)

# # Save the list of filenames to a pickle file
# with open(pickle_filename, 'wb') as handle:
#     try:
#         pickle.dump(image_filenames, handle, protocol=pickle.HIGHEST_PROTOCOL)
#         print("done")
#     except:
#         print("not done")

# Return the path to the created pickle file
# pickle_filename

if os.path.isfile(pickle_filename):
    with open(pickle_filename, 'rb') as f:
        filenames = pickle.load(f)
    print('Load filenames from: %s (%d)' % (pickle_filename, len(filenames)))
else:
    filenames = []
print(filenames)