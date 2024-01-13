Preparing data for create_synthetic_dataset.ipynb

1) copy background images in 'bg' folder

2) copy clipped images from Samsung phone to 'clipped_images' folder

3) run remove_transparency_samsung.py. It'll convert rgba to rgb correctly and images are copied to 'images' folder

4) annotations.xml is generated using cvat. Run cvat_annotations_to_json.py. It'll create 'keypoints' folder with keypoints in json format.

5) run rotate_by_90_180_270.py. It'll generate 3 additional images and corresponding transformed keypoints.

6) run cropped_images_to_masks.py. It'll create 'masks' folder with masks of the previously generated images.

