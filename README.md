# OreScanner-Project
YOLOv8 Object Detection pipeline for mining ore analysis (Python/OpenCV).

# OreScanner: AI-Powered Quality Control for Mining

![Python](https://img.shields.io/badge/Python-3.9-blue)
![YOLOv8](https://img.shields.io/badge/AI-YOLOv8-green)
![Computer Vision](https://img.shields.io/badge/Computer_Vision-OpenCV-orange)
![Status](https://img.shields.io/badge/Status-Prototype_v1-yellow)

## Executive Summary
**OreScanner** is an automated computer vision pipeline designed to detect and classify iron ore samples on a conveyor belt. In mining operations, manual sorting is slow, error-prone, and hazardous. This project prototypes a real-time AI solution using **YOLOv8 (You Only Look Once)** to identify ore capability with millisecond latency.

This project demonstrates an end-to-end Machine Learning lifecycle: from **synthetic data engineering** to **model training** and **inference deployment**.

---

## Technical Architecture

The pipeline consists of three core stages:

### 1. Synthetic Data Engineering (`generate_data.py`)
* **Challenge:** Real-world mining data is scarce and expensive to label.
* **Solution:** Built a Python script using `OpenCV` and `NumPy` to programmatically generate **synthetic training datasets**.
* **Technique:** Randomized geometric transformations (radius, position, color variance) to simulate ore diversity on a conveyor belt.
* **Outcome:** Generated 100+ labeled images automatically, eliminating manual annotation time.

### 2. Model Training (`train_model.py`)
* **Architecture:** **YOLOv8 Nano (v8n)** – chosen for its speed/accuracy balance, optimised for edge deployment (e.g., embedded cameras in mines).
* **Training Strategy:** Transfer Learning from COCO weights.
* **Optimisation:** Configured for 100 Epochs with Stochastic Gradient Descent (SGD) to minimise Box Loss.
* **Infrastructure:** Trained locally on **Apple Silicon (M2)** using MPS (Metal Performance Shaders) acceleration.

### 3. Inference & Evaluation (`test_model.py`)
* **Validation:** Custom inference script to test model performance on unseen data.
* **Confidence Thresholding:** Implemented dynamic confidence filtering (1% - 25%) to diagnose model certainty.
* **Visualisation:** Automated bounding box rendering to provide visual proof of detection.

---

## 📊 Results & Performance

| Metric | Performance (Prototype) | Notes |
| :--- | :--- | :--- |
| **mAP@50** | **99.5%** | Achieved on initial validation set |
| **Inference Speed** | **~80ms** | Real-time capable on CPU |
| **Precision** | **High** | Excellent localisation of ore samples |

### Visual Proof
*Below is an example of the model detecting a generated ore sample:*

![Model Prediction](FINAL_RESULT.jpg)
*(Note: Upload your 'FINAL_RESULT.jpg' to the repo to see this image!)*

---

## 🧠 Key Learnings & Challenges

**The "Overfitting" Experiment:**
* **Observation:** Initial training on a small dataset (10 Epochs) led to high training accuracy but poor generalisation on new data (the model "memorised" the pixel locations).
* **Diagnosis:** Analysed raw confidence tensors and discovered the model was "hallucinating" (predicting 111 weak boxes) or going blind on unseen data.
* **Resolution:** Increased dataset diversity and training duration (Epochs) to force the model to learn **features** (shapes/colors) rather than **positions**.

---

## 🚀 How to Run Locally

**1. Clone the Repository**
```bash
git clone [https://github.com/debdavid/OreScanner-Project.git](https://github.com/debdavid/OreScanner-Project.git)
cd OreScanner-Project
