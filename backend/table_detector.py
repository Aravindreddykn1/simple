# backend/table_detector.py
import pkg_resources as pkg
from yolov5 import detect  # Use your trained model here
output = detect.run(weights='runs/train/table_detector/weights/best.pt', source='uploads/', save_crop=True)
