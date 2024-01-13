import os
import xml.etree.ElementTree as ET
import json

# Parse the XML file
tree = ET.parse("annotations.xml")
root = tree.getroot()

# Initialize a dictionary to store the keypoints
keypoints_dict = {}

# Iterate through image elements
for image_elem in root.findall(".//image"):
    image_name = image_elem.get("name")
    points_elem = image_elem.find("points")

    if image_name and points_elem is not None:
        label = points_elem.get("label")
        points_str = points_elem.get("points")

        if label and points_str:
            # Split the points string into a list of integers (rounded)
            points_list = [
                list(map(lambda x: round(float(x)), point.split(",")))
                for point in points_str.split(";")
            ]

            # Mark all points as visible
            visible_points_list = []
            for point in points_list:
                point.append(1)
                visible_points_list.append(point)

            keypoints_dict[image_name] = {
                "label": label,
                "keypoints": visible_points_list,
            }

os.makedirs("keypoints", exist_ok=True)

# Save the keypoints as JSON files
for image_name, keypoints_data in keypoints_dict.items():
    print(image_name)
    json_filename = f"{image_name.strip('.png')}.json"
    with open("keypoints/" + json_filename, "w") as json_file:
        json.dump(keypoints_data, json_file, indent=4)

print("JSON files created successfully.")
