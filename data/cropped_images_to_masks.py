import cv2
import os

# Define the input and output folders
input_folder = "images"
output_folder = "masks"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image (you can add more image extensions if needed)
    if filename.endswith((".png", ".PNG")):
        # Read the image with an alpha channel
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

        if image is not None:
            # Create a binary mask where any non-black pixel is converted to white
            binary_mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            binary_mask[binary_mask > 0] = 255
            # Save the processed image to the output folder
            image = 255 - binary_mask
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, image)

            print(f"Processed and saved: {output_path}")
        else:
            print(f"Could not read: {image_path}")

print("Processing complete.")
