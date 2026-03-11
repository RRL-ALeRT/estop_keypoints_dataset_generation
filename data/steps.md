Preparing data for create_synthetic_dataset.ipynb

The notebook supports one or more object classes. The **folder name is the class name** — each
subdirectory inside `data/images/` and `data/masks/` is one class, and the directory name is used
directly as the class label throughout the pipeline.

## Per-class data preparation (repeat for each class)

1) Copy background images into the `bg/` folder (shared across all classes).

2) Copy clipped images for a class from the Samsung phone into a temporary `clipped_images/`
   folder. These are the raw RGBA PNG cutouts of the object.

3) Run `remove_transparency_samsung.py`. It converts RGBA to RGB and saves images to
   `images/<class_name>/`. Edit the `class_name` variable in the script to match your class name
   before running.

4) Run `rotate_by_90_180_270.py`. It generates 3 additional rotated images (90°, 180°, 270°)
   for each image. Edit the `class_name` variable in the script to match your class name.

5) Run `cropped_images_to_masks.py`. It creates binary masks in `masks/<class_name>/`.
   Edit the `class_name` variable in the script to match your class name.

## Single-class example

For a single class named `estop`:

```
data/
├── bg/
├── images/
│   └── estop/     <- class "estop" (step 3 output)
└── masks/
    └── estop/     <- step 5 output
```

## Multi-class example

For two classes `estop` and `button`:

```
data/
├── bg/
├── images/
│   ├── button/    <- class "button"
│   └── estop/     <- class "estop"
└── masks/
    ├── button/
    └── estop/
```

Repeat steps 2–5 for each class. The notebook detects all class subdirectories automatically;
no manual ID assignment is needed.


