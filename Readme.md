# Heart Disease Prediction with Optimal Feature Selection

## Project Overview

This project aims to build a machine learning–based system for **predicting heart disease**. Unlike most projects that rely on built-in feature selection methods, this project implements a **custom feature selection algorithm** to identify the most relevant features for prediction.

The goal is to compare model performance using:

1. **All features**
2. **Selected optimal features (custom algorithm)**

Finally, a simple **User Interface (UI)** will be created to allow users to input data and see predictions.

---

## Objectives

* Collect and preprocess heart disease dataset.
* Implement a **custom feature selection algorithm** to find the best subset of features.
* Train and evaluate multiple ML models (Logistic Regression, Random Forest, SVM, etc.).
* Compare accuracy, precision, recall, and F1-score with and without feature selection.
* Build a lightweight **UI dashboard** for visualization and prediction.

---

## 🛠 Tech Stack

* **Python** (Core language)
* **Pandas, NumPy** (Data handling & preprocessing)
* **Scikit-learn** (ML models, metrics)
* **Matplotlib / Seaborn** (Visualization)
* **Streamlit / Flask** (UI for predictions)

---

## Project Structure

```
HeartDisease-FeatureSelection/
│── data/                     # Datasets (CSV files)
│── notebooks/                # Jupyter notebooks for experiments
│── src/                      # Core project code
│   ├── preprocessing.py      # Data cleaning & preprocessing
│   ├── feature_selection.py  # Custom feature selection algorithm
│   ├── models.py             # Model training & evaluation
│   ├── utils.py              # Helper functions
│── ui/                       # Frontend/UI code (Streamlit/Flask)
│── results/                  # Plots, metrics, reports
│── README.md                 # Project documentation
│── requirements.txt          # Dependencies
│── main.py                   # Main execution script
```

---

## How to Run

1. Clone this repo:

   ```bash
   git clone https://github.com/yourusername/heart-disease-feature-selection.git
   cd heart-disease-feature-selection
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run experiments in Jupyter Notebook (optional):

   ```bash
   jupyter notebook notebooks/
   ```

4. Run the main script:

   ```bash
   python main.py
   ```

5. Launch the UI:

   ```bash
   streamlit run ui/app.py
   ```

---

## Expected Outcomes

* A comparison of ML models with and without feature selection.
* A custom feature selection algorithm tailored for heart disease dataset.
* Visualizations of feature importance and model results.
* A user-friendly interface for predictions.

---

## Dataset

We will use the **UCI Heart Disease Dataset** (Framingham  dataset).

---
