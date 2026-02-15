import os
import numpy as np
import cv2

# 1. The Local Override (Bypassing iCloud entirely)
# '~' means /Users/emmanueldavid/
BASE_DIR = os.path.expanduser("~/datasets/ore_data")
IMG_DIR = os.path.join(BASE_DIR, "images/train")
LBL_DIR = os.path.join(BASE_DIR, "labels/train")

os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(LBL_DIR, exist_ok=True)

print(f"Creating data locally in: {BASE_DIR}")

# 2. Generating 100 synthetic ore images
for i in range(100):
    img = np.zeros((640, 640, 3), dtype=np.uint8)
    img[:] = (70, 70, 70) 
    
    x = np.random.randint(50, 590)
    y = np.random.randint(50, 590)
    radius = np.random.randint(20, 60)
    cv2.circle(img, (x, y), radius, (150, 150, 150), -1)
    
    cv2.imwrite(f"{IMG_DIR}/ore_{i}.jpg", img)
    
    x_norm = x / 640.0
    y_norm = y / 640.0
    width_norm = (radius * 2) / 640.0
    height_norm = (radius * 2) / 640.0
    
    with open(f"{LBL_DIR}/ore_{i}.txt", "w") as f:
        f.write(f"0 {x_norm} {y_norm} {width_norm} {height_norm}")

print("✅ Success! 100 images saved SAFELY outside of iCloud.")
