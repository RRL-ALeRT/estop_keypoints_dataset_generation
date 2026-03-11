import cv2
import os

# Set the class name to rotate images for.
# Change this value for each class you prepare (e.g. "estop", "button", "valve").
class_name = "estop"

# Process all images in the class-specific images folder
images_folder = os.path.join("images", class_name)

for image_filename in os.listdir(images_folder):
    if image_filename.endswith(".png"):
        # Load the image
        image_path = os.path.join(images_folder, image_filename)
        image = cv2.imread(image_path)

        image_name_without_extension = os.path.splitext(image_filename)[0]

        # Rotate the image by 90, 180, and 270 degrees
        for cv2_angle, angle in [
            (cv2.ROTATE_90_CLOCKWISE, 90),
            (cv2.ROTATE_180, 180),
            (cv2.ROTATE_90_COUNTERCLOCKWISE, 270),
        ]:
            rotated_image = cv2.rotate(image, cv2_angle)

            # Save the rotated image
            rotated_image_filename = f"{image_name_without_extension}_{angle}.png"
            rotated_image_path = os.path.join(images_folder, rotated_image_filename)
            cv2.imwrite(rotated_image_path, rotated_image)
