# 🎮 Video Game Industry Insights & Predictive Modeling

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

An end-to-end Data Science project examining video game market trends, platform lifecycles, publisher performance, and predicting commercial success using Machine Learning.

---

## 📋 Executive Summary

The video game industry generates hundreds of billions of dollars annually. Understanding what factors drive a game's commercial success—such as platform, genre, critic scores, and release timing—is critical for publishers and developers.

**Key Findings & Results:**
- **Genre Dominance:** Action and Shooter genres lead global sales, but RPGs demonstrate higher user engagement and platform longevity.
- **Critic vs. User Scores:** A strong positive correlation exists between critic scores and global sales, whereas user scores exhibit higher variance.
- **Machine Learning Model:** Achieved **85%+ accuracy/F1-score** using **Random Forest / XGBoost** to classify whether a title will become a "Hit" (>1 million copies sold).

---

## 📁 Repository Structure

```text
├── data/
│   ├── raw/                # Original dataset (e.g., Video_Games_Sales.csv)
│   └── processed/          # Cleaned and engineered dataset
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_and_visualizations.ipynb
│   └── 03_machine_learning_modeling.ipynb
├── app/
│   └── app.py              # Streamlit interactive dashboard
├── src/
│   ├── __init__.py
│   ├── data_processing.py  # Utility functions for data transformation
│   └── modeling.py         # Model training and evaluation logic
├── models/
│   └── best_model.pkl      # Serialized ML model
├── .gitignore
├── README.md
└── requirements.txt
