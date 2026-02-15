from ultralytics import YOLO

# 1. Load the pre-trained Nano brain
model = YOLO("yolov8n.pt")

# 2. Train it for 100 epochs (Real Machine Learning!)
print("Starting Engine for 100 Epochs...")
model.train(data="data_config.yaml", epochs=100, imgsz=640)
