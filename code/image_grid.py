import os
from PIL import Image

# Set the directory containing your images
image_dir = 'C:\\Users\\mehal\\Downloads\\18786Project\\AttnGAN\\data\\coco\\test2014'

# Size of the grid
grid_size = (10, 10)  # This will create a grid of 20x20

# Size for grid cells: every image will be adjusted to these dimensions
cell_size = (128, 128)

# Create a new image for the grid
grid_image = Image.new('RGB', (grid_size[0] * cell_size[0], grid_size[1] * cell_size[1]))

# List all image files in the directory
image_files = [os for os in os.listdir(image_dir) if os.endswith('.jpg')]

# Function to resize and crop the image
def resize_and_crop(img, target_size):
    img_ratio = img.width / img.height
    target_ratio = target_size[0] / target_size[1]
    if target_ratio > img_ratio:
        # The image is too tall; we need to cut off the top and bottom
        scale_factor = target_size[0] / img.width
        scaled_height = scale_factor * img.height
        img = img.resize((target_size[0], int(scaled_height)), Image.Resampling.LANCZOS)
        top_cut = (img.height - target_size[1]) // 2
        img = img.crop((0, top_cut, target_size[0], top_cut + target_size[1]))
    else:
        # The image is too wide; we need to cut off the sides
        scale_factor = target_size[1] / img.height
        scaled_width = scale_factor * img.width
        img = img.resize((int(scaled_width), target_size[1]), Image.Resampling.LANCZOS)
        side_cut = (img.width - target_size[0]) // 2
        img = img.crop((side_cut, 0, side_cut + target_size[0], target_size[1]))
    return img

# Fill the grid with images
for index, file in enumerate(image_files):
    if index >= grid_size[0] * grid_size[1]:
        break  # Stop if the grid is full
    img_path = os.path.join(image_dir, file)
    img = Image.open(img_path)
    img = resize_and_crop(img, cell_size)
    x = index % grid_size[0] * cell_size[0]
    y = index // grid_size[0] * cell_size[1]
    grid_image.paste(img, (x, y))

# Save the grid image
output_path = 'C:\\Users\\mehal\\Downloads\\18786Project\\AttnGAN\\data\\coco\\grid_image.jpg'
grid_image.save(output_path)
print(f'Grid image saved to {output_path}')
