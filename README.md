# 🎮 Video Game Industry Insights & Predictive Modeling

<p align="center">
  <b>Select Language / Selecciona Idioma:</b><br>
  <a href="#-english">🇺🇸 English</a> • <a href="#-español">🇲🇽 Español</a>
</p>

---

## 🇺🇸 English

### Overview
An end-to-end Data Science project examining video game market trends, platform lifecycles, publisher performance, and predicting commercial success using Machine Learning.

### 📋 Executive Summary
The video game industry generates hundreds of billions of dollars annually. Understanding what factors drive a game's commercial success—such as platform, genre, critic scores, and release timing—is critical for publishers and developers.

**Key Findings & Results:**
- **Genre Dominance:** Action and Shooter genres lead global sales, but RPGs demonstrate higher user engagement and platform longevity.
- **Critic vs. User Scores:** A strong positive correlation exists between critic scores and global sales, whereas user scores exhibit higher variance.
- **Machine Learning Model:** Achieved **85%+ accuracy/F1-score** using **Random Forest / XGBoost** to classify whether a title will become a "Hit" (>1 million copies sold).

---

## 🇲🇽 Español

### Descripción General
Un proyecto integral de Ciencia de Datos que analiza tendencias del mercado de videojuegos, ciclos de vida de plataformas, rendimiento de distribuidores y predicción del éxito comercial mediante Machine Learning.

### 📋 Resumen Ejecutivo
La industria de los videojuegos genera cientos de miles de millones de dólares al año. Comprender qué factores impulsan el éxito comercial de un juego (como la plataforma, el género, las puntuaciones de la crítica y la fecha de lanzamiento) es fundamental para desarrolladores y distribuidores.

**Hallazgos Clave y Resultados:**
- **Dominio de Géneros:** Los géneros de Acción y Disparos (Shooter) lideran las ventas globales, mientras que los RPG muestran un mayor compromiso de los usuarios y mayor longevidad en plataformas.
- **Crítica vs. Usuarios:** Existe una fuerte correlación positiva entre las calificaciones de la crítica y las ventas globales, mientras que las calificaciones de los usuarios presentan mayor variabilidad.
- **Modelo de Machine Learning:** Se alcanzó un **85%+ de precisión/F1-score** utilizando **Random Forest / XGBoost** para clasificar si un título se convertirá en un "Éxito" (>1 millón de copias vendidas).

---

## 📁 Repository Structure / Estructura del Repositorio

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
│   ├── data_processing.py  # Utility functions
│   └── modeling.py         # ML logic
├── models/
│   └── best_model.pkl      # Serialized ML model
├── .gitignore
├── README.md
└── requirements.txt
