import cv2
import os

# Generates binary masks for ALL class subdirectories inside images/ in one run.
# For each class, reads images from images/<class_name>/ and writes masks to masks/<class_name>/.

images_root = "images"

class_dirs = sorted([
    d for d in os.listdir(images_root)
    if os.path.isdir(os.path.join(images_root, d))
])
print(f"Found classes: {class_dirs}")

for class_name in class_dirs:
    input_folder = os.path.join(images_root, class_name)
    output_folder = os.path.join("masks", class_name)
    os.makedirs(output_folder, exist_ok=True)

    processed = 0
    for filename in os.listdir(input_folder):
        if filename.endswith((".png", ".PNG")):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

            if image is not None:
                binary_mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                binary_mask[binary_mask > 0] = 255
                mask = 255 - binary_mask
                cv2.imwrite(os.path.join(output_folder, filename), mask)
                processed += 1
            else:
                print(f"  Could not read: {image_path}")

    print(f"  Class '{class_name}': {processed} masks -> {output_folder}/")

print("Done.")
