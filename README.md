## Synthetic Data Generation for YOLOv8 Object Detection for Rescue League autonomous dexterity

Follow `data/steps.md` to prepare your data, then run all cells in `create_synthetic_dataset.ipynb`.

The generated dataset can be directly used to train a YOLOv8 object detection model
([Ultralytics detect docs](https://docs.ultralytics.com/tasks/detect/)).

### Multi-Class Support

The notebook supports generating datasets with **multiple object classes** in a single run.  
The **folder name is the class name** — place clipped images in per-class subdirectories:

```
data/
├── bg/                     # background images (shared)
├── clipped_images/
│   ├── estop/              # raw RGBA PNGs for "estop"
│   └── button/             # raw RGBA PNGs for "button"
├── images/                 # auto-populated by remove_transparency_samsung.py
└── masks/                  # auto-populated by cropped_images_to_masks.py
```

Run the three preparation scripts once for all classes, then run the notebook end-to-end.  
See `data/steps.md` for the full workflow.

### Notes

1) A Samsung phone is used to generate clipped images, skipping manual cutout work.

2) https://docs.ultralytics.com/tasks/detect/ for YOLOv8 object detection format reference.
