# 🌍 Air Quality Index (AQI) Prediction using Machine Learning

This repository contains my **internship project** on **Air Quality Index (AQI) prediction**, aiming to forecast air quality parameters and estimate AQI for future time periods using **machine learning and time-series forecasting**.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=matplotlib&logoColor=white)
![Prophet](https://img.shields.io/badge/Prophet-008000?style=for-the-badge&logo=meta&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-EC4D28?style=for-the-badge&logo=xgboost&logoColor=white)

---

## Project Overview

Air pollution is a major environmental and public health concern. Predicting AQI helps to:

- Issue **early health warnings**
- Inform **environmental policy decisions**
- Raise **public awareness** of air quality trends

This project leverages **time-series forecasting (Prophet)** and **machine learning models (XGBoost)** to predict pollutant levels and weather-related features, which are then used to estimate AQI.

---

## Dataset

- **Source:** [UCI Machine Learning Repository – Air Quality Dataset](https://archive.ics.uci.edu/ml/datasets/Air+Quality)
- **Duration:** March 2004 – April 2005 (**9358 hourly records**)
- **Key Features:**
  - **Pollutants**: CO, NMHC, Benzene, NOx, NO2
  - **Sensor responses**: S1–S5
  - **Weather**: Temperature, Relative Humidity (RH), Absolute Humidity (AH)
- **Target:** Future AQI values (calculated from pollutant concentrations)

---

## Workflow

1. **Data Preprocessing**

   - Handle missing & anomalous values
   - Drop constant features (e.g., NMHC)
   - Normalize and format timestamps for Prophet

2. **Feature Selection**

   - `CO(GT)`, `NOx(GT)`, `PT08.S1(CO)`, `PT08.S4(NO2)`, `C6H6(GT)`, `Temp`, `RH`

3. **Modeling**

   - **Prophet** → Captures seasonal pollutant patterns
   - **XGBoost** → Learns complex pollutant-AQI relationships
   - Hybrid approach improves accuracy

4. **Evaluation Metrics**

   - **MAE (Mean Absolute Error)** – average error
   - **RMSE (Root Mean Squared Error)** – penalizes large deviations
   - **MAPE/SMAPE** – percentage-based accuracy

   Example (Temperature forecast):

```

MAE   = 5.10 °C
RMSE  = 6.31 °C
SMAPE = 55.14 %

```

5. **Visualization**

- Train vs Test split (80/20)
- Forecast vs Actual plots

---

## Results

- Hybrid **Prophet + XGBoost** achieved **lower error rates** than standalone models.
- Predictions aligned well with real AQI patterns.
- Supports **short-term AQI forecasting** for health and policy use cases.

---

## How to Run

1. Clone this repo:

```bash
git clone https://github.com/your-username/AQI-Prediction.git
cd AQI-Prediction
```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Launch the notebook:

   ```bash
   jupyter notebook "airQualityIndex (3).ipynb"
   ```

## 🔹 Internship Note

This project was developed as part of my **internship program**, applying **data science and machine learning** techniques to address real-world **environmental challenges**.
