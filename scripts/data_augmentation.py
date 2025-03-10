import cv2
import albumentations as A
from albumentations.core.bbox_utils import convert_bboxes_to_albumentations, convert_bboxes_from_albumentations
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 1. Define the augmentation pipeline
def create_augmentation_pipeline():
    return A.Compose(
        [
            A.HorizontalFlip(p=0.5),
            A.VerticalFlip(p=0.5),
            A.RandomBrightnessContrast(p=0.2),
            A.ShiftScaleRotate(scale_limit=0.2, rotate_limit=30, shift_limit=0.2, p=0.5),
        ],
        bbox_params=A.BboxParams(format='yolo', label_fields=['class_labels'])
    )

# 2. Load image and labels
def load_image_and_labels(image_path, label_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    with open(label_path, 'r') as f:
        lines = f.readlines()
    
    bboxes = []
    class_labels = []
    for line in lines:
        label = line.strip().split()
        class_labels.append(int(label[0]))
        bboxes.append([float(x) for x in label[1:]])
    
    return image, bboxes, class_labels

# 3. Apply augmentations
def apply_augmentations(image, bboxes, class_labels, transform):
    augmented = transform(image=image, bboxes=bboxes, class_labels=class_labels)
    return augmented['image'], augmented['bboxes'], augmented['class_labels']

# 4. Save augmented image and labels
def save_augmented_data(image, bboxes, class_labels, image_save_path, label_save_path):
    cv2.imwrite(image_save_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    
    with open(label_save_path, 'w') as f:
        for cls, bbox in zip(class_labels, bboxes):
            f.write(f"{cls} {' '.join(map(str, bbox))}\n")

# 5. Visualize augmented image with bounding boxes
def visualize_bboxes(image, bboxes):
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.imshow(image)

    for bbox in bboxes:
        x_center, y_center, width, height = bbox
        x_min = x_center - width / 2
        y_min = y_center - height / 2
        rect = patches.Rectangle((x_min * image.shape[1], y_min * image.shape[0]),
                                 width * image.shape[1],
                                 height * image.shape[0],
                                 linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

    plt.show()
