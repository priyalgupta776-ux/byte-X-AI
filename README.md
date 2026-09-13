# HACKBLOX 2026 — 3LC Scene Classification

A data-centric image classification project developed during the **24-hour HACKBLOX 2026 AI Track** in collaboration with **3LC**.

The goal was to classify natural scene images into six categories while following the challenge constraints and using 3LC to inspect and improve the training data.

## Problem

The task was to classify images into six scene categories:

- Buildings
- Forest
- Glacier
- Mountain
- Sea
- Street

The challenge provided labeled seed data, unlabeled images, validation data, and a hidden test set.

The model architecture was fixed to **ResNet-18**, trained from scratch without pretrained weights or external image data.

## Approach

Instead of focusing only on model architecture changes, I followed a **data-centric machine learning workflow** using 3LC.

The workflow included:

1. Training a baseline ResNet-18 model
2. Inspecting model predictions and difficult samples
3. Exploring image embeddings using UMAP
4. Identifying useful undefined/unlabeled samples
5. Curating labels and assigning sample weights
6. Retraining the model
7. Comparing results across multiple iterations
8. Generating the final predictions and submission

## 📊 Results

| Experiment | Validation Accuracy |
|------------|---------------------:|
| Baseline | 67.25% |
| Iteration 1 | 71.00% |
| Iteration 2 | 73.92% |
| Iteration 3 | 75.00% |
| Final | **76.83%** |

The final development run achieved a **best validation accuracy of 76.83%**, improving the baseline by **9.58 percentage points**.

> Note: 76.83% is the development validation accuracy and is not the hidden test/Kaggle score.

##  Technologies

- Python
- PyTorch
- ResNet-18
- 3LC
- UMAP
- Pandas
- NumPy
- Git & GitHub

##  Repository Structure

```text
├── train.py                  # Model training
├── predict.py                # Prediction and submission generation
├── register_tables.py        # Register dataset tables with 3LC
├── repair_embeddings.py      # Embedding reduction/repair
├── inspect_3lc.py            # 3LC inspection utilities
├── config.yaml               # Project configuration
├── sample_submission.csv     # Submission format
├── submission.csv             # Final submission
├── writeup.md                # Detailed project write-up
│
├── 3lc/
│   └── Intel-Scene-3LC.zip   # Exported 3LC project
│
├── Screenshots/
│   ├── 3lc-charts.png
│   ├── 3lc-runs.png
│   ├── 3lc-tables.png
│   └── Kaggle.png
│
└── submissions/              # Iterative submission files
