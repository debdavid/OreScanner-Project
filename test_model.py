from ultralytics import YOLO
import os

# 1. Load the brain
model = YOLO("/Users/emmanueldavid/runs/detect/train5/weights/best.pt")

# 2. Point to the flashcard
training_image_path = os.path.expanduser("~/datasets/ore_data/images/train/ore_0.jpg")

# 3. Scan it at 1% confidence
print("\n--- SCANNING FLASHCARD ---")
results = model(training_image_path, conf=0.01)

# 4. Print the raw mathematical thoughts
print("\n--- THE AI'S RAW THOUGHTS ---")
boxes = results[0].boxes

if len(boxes) == 0:
    print("🚨 THE VERDICT: The AI is completely blind. It predicted 0 boxes.")
else:
    print(f"✅ THE VERDICT: The AI found {len(boxes)} box(es)!")
    print(f"Confidence scores: {boxes.conf.tolist()}")
