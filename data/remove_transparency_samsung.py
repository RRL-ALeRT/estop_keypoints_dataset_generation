import os
import cv2
import numpy as np

# Set the class name. Images will be saved to images/<class_name>/
# Change this value for each class you prepare (e.g. "estop", "button", "valve").
class_name = "estop"

# Set the path to the folder containing your clipped RGBA images
input_folder = "clipped_images"

# Output folder for this class
output_folder = os.path.join("images", class_name)

# Ensure the output folder exists, create it if not
os.makedirs(output_folder, exist_ok=True)

# Define the color to replace white transparent pixels (black in BGR format)
replacement_color = (0, 0, 0)

# Define the threshold for considering a pixel as white (you can adjust this threshold)
white_threshold = 220

# Loop through all the files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image (you can add more extensions as needed)
    if filename.endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
        # Read the image using OpenCV
        img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_UNCHANGED)

        # Check if the image has an alpha channel (transparency)
        if img.shape[-1] == 4:  # Assuming 4 channels (RGBA)
            # Create a mask for white transparent pixels
            alpha_mask = (img[:, :, :3] > white_threshold).all(axis=2) & (
                img[:, :, 3] < 255
            )

            # Replace RGB channels for white transparent pixels with the specified color
            img[alpha_mask, :3] = replacement_color

        # Save the modified image to the output folder
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, img)
