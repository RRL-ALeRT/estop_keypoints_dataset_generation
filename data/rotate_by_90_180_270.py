import cv2
import os

# Rotates images for ALL class subdirectories inside images/ in one run.
# For each class, adds 90°, 180°, and 270° rotated copies alongside the originals.

images_root = "images"

class_dirs = sorted([
    d for d in os.listdir(images_root)
    if os.path.isdir(os.path.join(images_root, d))
])
print(f"Found classes: {class_dirs}")

for class_name in class_dirs:
    images_folder = os.path.join(images_root, class_name)
    rotated = 0

    for image_filename in os.listdir(images_folder):
        # Only rotate original images (skip files that already end with _90/_180/_270)
        if not image_filename.endswith(".png"):
            continue
        name_no_ext = os.path.splitext(image_filename)[0]
        if name_no_ext.endswith(("_90", "_180", "_270")):
            continue

        image_path = os.path.join(images_folder, image_filename)
        image = cv2.imread(image_path)

        for cv2_angle, angle in [
            (cv2.ROTATE_90_CLOCKWISE, 90),
            (cv2.ROTATE_180, 180),
            (cv2.ROTATE_90_COUNTERCLOCKWISE, 270),
        ]:
            rotated_image = cv2.rotate(image, cv2_angle)
            rotated_path = os.path.join(images_folder, f"{name_no_ext}_{angle}.png")
            cv2.imwrite(rotated_path, rotated_image)
            rotated += 1

    print(f"  Class '{class_name}': {rotated} rotated images added to {images_folder}/")

print("Done.")
