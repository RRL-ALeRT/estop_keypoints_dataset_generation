import cv2
import json
import os


# Function to rotate the image and points
def rotate_image_and_points(image, points, angle):
    # Rotate the image
    rotated_image = cv2.rotate(image, angle)

    # Rotate the points accordingly, '1' for visible
    if angle == cv2.ROTATE_90_CLOCKWISE:
        rotated_points = [(image.shape[0] - point[1], point[0], 1) for point in points]
    elif angle == cv2.ROTATE_180:
        rotated_points = [
            (image.shape[1] - point[0], image.shape[0] - point[1], 1)
            for point in points
        ]
    elif angle == cv2.ROTATE_90_COUNTERCLOCKWISE:
        rotated_points = [(point[1], image.shape[1] - point[0], 1) for point in points]

    return rotated_image, rotated_points


# Process all images in the "images" folder
images_folder = "images"
keypoints_folder = "keypoints"

for image_filename in os.listdir(images_folder):
    if image_filename.endswith(".png"):
        # Load the image
        image_path = os.path.join(images_folder, image_filename)
        image = cv2.imread(image_path)

        # Construct the path to the JSON file based on the image file's name
        image_name_without_extension = os.path.splitext(image_filename)[0]
        json_filename = image_name_without_extension + ".json"
        json_path = os.path.join(keypoints_folder, json_filename)

        # Read points from the JSON file
        with open(json_path, "r") as json_file:
            json_data = json.load(json_file)

        # Extract the label and keypoints from the JSON data
        label = json_data["label"]
        keypoints = json_data["keypoints"]

        # Rotate the image and points by 90, 180, and 270 degrees
        rotated_images = []
        rotated_json_data = []
        for angle in [
            cv2.ROTATE_90_CLOCKWISE,
            cv2.ROTATE_180,
            cv2.ROTATE_90_COUNTERCLOCKWISE,
        ]:
            rotated_image, rotated_points = rotate_image_and_points(
                image, keypoints, angle
            )

            if angle == cv2.ROTATE_90_CLOCKWISE:
                angle = 90
            elif angle == cv2.ROTATE_180:
                angle = 180
            elif angle == cv2.ROTATE_90_COUNTERCLOCKWISE:
                angle = 270

            # # Modify the sequence of rotated points for each rotation
            if angle == 90:
                rotated_points = [
                    rotated_points[2],
                    rotated_points[0],
                    rotated_points[3],
                    rotated_points[1],
                    rotated_points[4],
                ]
            elif angle == 180:
                rotated_points = [
                    rotated_points[3],
                    rotated_points[2],
                    rotated_points[1],
                    rotated_points[0],
                    rotated_points[4],
                ]
            elif angle == 270:
                rotated_points = [
                    rotated_points[1],
                    rotated_points[3],
                    rotated_points[0],
                    rotated_points[2],
                    rotated_points[4],
                ]

            # Save the rotated image
            rotated_image_filename = f"{image_name_without_extension}_{angle}.png"
            rotated_image_path = os.path.join(images_folder, rotated_image_filename)
            cv2.imwrite(rotated_image_path, rotated_image)

            # Update the JSON data for the rotated image
            rotated_json = {"label": label, "keypoints": rotated_points}
            rotated_json_filename = f"{image_name_without_extension}_{angle}.json"
            rotated_json_path = os.path.join(keypoints_folder, rotated_json_filename)
            with open(rotated_json_path, "w") as rotated_json_file:
                json.dump(rotated_json, rotated_json_file, indent=4)
