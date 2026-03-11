import os
import cv2
import numpy as np

# Place your clipped RGBA images in class-named subdirectories under clipped_images/:
#   clipped_images/
#   ├── estop/     <- RGBA PNGs for the "estop" class
#   └── button/    <- RGBA PNGs for the "button" class
#
# This script processes ALL class subdirectories in one run and writes the
# converted RGB images to the matching images/<class_name>/ directories.

clipped_images_root = "clipped_images"

# Define the color to replace white transparent pixels (black in BGR format)
replacement_color = (0, 0, 0)

# Threshold for considering a pixel as white (adjust if needed)
white_threshold = 220

class_dirs = sorted([
    d for d in os.listdir(clipped_images_root)
    if os.path.isdir(os.path.join(clipped_images_root, d))
])
print(f"Found classes: {class_dirs}")

for class_name in class_dirs:
    input_folder = os.path.join(clipped_images_root, class_name)
    output_folder = os.path.join("images", class_name)
    os.makedirs(output_folder, exist_ok=True)

    processed = 0
    for filename in os.listdir(input_folder):
        if filename.endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_UNCHANGED)

            if img.shape[-1] == 4:  # RGBA
                alpha_mask = (img[:, :, :3] > white_threshold).all(axis=2) & (
                    img[:, :, 3] < 255
                )
                img[alpha_mask, :3] = replacement_color

            cv2.imwrite(os.path.join(output_folder, filename), img)
            processed += 1

    print(f"  Class '{class_name}': {processed} images -> {output_folder}/")

print("Done.")
