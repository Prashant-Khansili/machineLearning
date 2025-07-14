import os

def auto_label_full_image(img_dir, label_dir, class_id):
    os.makedirs(label_dir, exist_ok=True)
    for img_file in os.listdir(img_dir):
        if img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
            name = os.path.splitext(img_file)[0]
            label_path = os.path.join(label_dir, name + ".txt")
            with open(label_path, 'w') as f:
                f.write(f"{class_id} 0.5 0.5 1.0 1.0\n")

# Example usage:
# auto_label_full_image('lemon_dataset/images/train/ripe_lemons', 'lemon_dataset/labels/train/ripe_lemons', class_id=0)
# auto_label_full_image('lemon_dataset/images/train/unripe_lemons', 'lemon_dataset/labels/train/unripe_lemons', class_id=1)
auto_label_full_image('lemon_dataset/images/val/unripe_lemons', 'lemon_dataset/labels/val/unripe_lemons', class_id=1)
auto_label_full_image('lemon_dataset/images/val/ripe_lemons', 'lemon_dataset/labels/val/ripe_lemons', class_id=0)