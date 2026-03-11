## Synthetic Data Generation for YOLOv8 Object Detection for Rescue League autonomous dexterity

Follow `data/steps.md` to prepare your data, then run all cells in `create_synthetic_dataset.ipynb`.

The generated dataset can be directly used to train a YOLOv8 object detection model
([Ultralytics detect docs](https://docs.ultralytics.com/tasks/detect/)).

### Multi-Class Support

The notebook supports generating datasets with **multiple object classes**.  
The **folder name is the class name** — create one subdirectory per class:

```
data/
├── bg/                  # background images (shared)
├── images/
│   ├── button/          # class "button"
│   └── estop/           # class "estop"
└── masks/
    ├── button/
    └── estop/
```

The notebook detects all class subdirectories automatically. YOLO integer class IDs are derived
from the sorted alphabetical order of class names at label-writing time — no manual ID assignment
needed.  
See `data/steps.md` for the full per-class data-preparation workflow.

### Notes

1) A Samsung phone is used to generate clipped images, skipping manual cutout work.

2) https://docs.ultralytics.com/tasks/detect/ for YOLOv8 object detection format reference.
