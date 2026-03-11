Preparing data for create_synthetic_dataset.ipynb

The **folder name is the class name**. Place your clipped images in per-class subdirectories and
run the three preparation scripts **once** — they process all classes in a single run.

## Step 1 – Organise clipped images

Copy your raw RGBA PNG cutouts from the Samsung phone into `clipped_images/<class_name>/`:

```
data/
└── clipped_images/
    ├── estop/    <- RGBA PNGs for the "estop" class
    └── button/   <- RGBA PNGs for the "button" class
```

Also copy your background images into `bg/` (shared across all classes).

## Step 2 – Run the preparation scripts (one shot for all classes)

```bash
cd data
python remove_transparency_samsung.py  # converts RGBA -> RGB, writes images/*/
python rotate_by_90_180_270.py         # adds 90/180/270° rotated copies to images/*/
python cropped_images_to_masks.py      # generates binary masks in masks/*/
```

After these three scripts complete, your data directory will look like:

```
data/
├── bg/
├── clipped_images/
│   ├── estop/
│   └── button/
├── images/
│   ├── estop/
│   └── button/
└── masks/
    ├── estop/
    └── button/
```

## Step 3 – Generate the dataset

Run all cells in `create_synthetic_dataset.ipynb`. The notebook auto-detects all class
subdirectories and generates the full train/val dataset in one go.

To add a new class later, add `clipped_images/<new_class>/` and re-run the three scripts.


