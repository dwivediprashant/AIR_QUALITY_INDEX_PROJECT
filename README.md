##  Tech Stack 

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) +
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) +
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) +
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=matplotlib&logoColor=white) +
![Seaborn](https://img.shields.io/badge/Seaborn-276DC3?style=for-the-badge&logo=python&logoColor=white) +
![Prophet](https://img.shields.io/badge/Prophet-008000?style=for-the-badge&logo=meta&logoColor=white) +
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) +
![XGBoost](https://img.shields.io/badge/XGBoost-EC4D28?style=for-the-badge&logo=xgboost&logoColor=white) +
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) +
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)


#  Air Quality Index (AQI) Prediction using Machine Learning  
 Internship Project  

This repository contains my **internship project** on **Air Quality Index (AQI) Prediction**.  
The goal is to design and develop a machine learning pipeline that forecasts air quality parameters and ultimately predicts AQI for future time periods.  

---

##  Project Overview  

Air pollution is one of the biggest environmental challenges, and predicting AQI helps in:  
-  Raising early health alerts  
-  Guiding environmental policies  
-  Increasing public awareness  

In this project, I use **time-series forecasting** and **machine learning models** to predict pollutants and weather-related factors (Temperature, Relative Humidity, CO, etc.), which are then combined to estimate AQI.  

---

##  Dataset  

- **Source:** [UCI Machine Learning Repository – Air Quality Dataset](https://archive.ics.uci.edu/ml/datasets/Air+Quality)  
- **Duration:** March 2004 – April 2005 (9358 hourly instances)  
- **Key Features:**  
  - CO, NMHC, Benzene, NOx, NO2  
  - Sensor responses (S1–S5)  
  - Temperature, Relative Humidity (RH), Absolute Humidity (AH)  
- **Target:** Future **AQI prediction** (derived from pollutant concentrations).  

---

##  Current Workflow  

### 1. Data Cleaning & Preprocessing  
- Handle missing values and anomalies  
- Standardize time format for Prophet (`ds`, `y`)  

### 2. Univariate Forecasting with Facebook Prophet  
- Predict each feature separately (e.g., Temperature, RH, CO)  
- Split into **80% Train / 20% Test**  
- Forecast future values  

### 3. Model Evaluation (sklearn metrics)  
- **MAE (Mean Absolute Error):** average error in same units  
- **RMSE (Root Mean Squared Error):** penalizes large errors  
- **SMAPE (Symmetric Mean Absolute % Error):** better percentage error measure for small values  

 Example Results (for Temperature):  
```

MAE   = 5.10 °C
RMSE  = 6.31 °C
SMAPE = 55.14 %

```

### 4. Visualization  
- 📈 Train vs Test split  
- 📉 Forecast vs Actual values  

---

##  Future Roadmap  

 **Phase 1 (Current):**  
- Forecast individual features using Prophet  
- Evaluate performance with error metrics  

 **Phase 2 (Next):**  
- Use **XGBoost / Regression models** with multiple features to predict AQI directly  
- Build an **AQI calculation pipeline** using official index formulae  
- Deploy model backend (**Flask / FastAPI**)  

 **Phase 3 (Final):**  
- Integrate with frontend dashboard (**React / Streamlit**)  
- Display real-time AQI predictions and trends  
- Add alert/notification system for poor AQI levels  

---

##  Tech Stack  

- **Languages:** Python  
- **Libraries:** Prophet, Scikit-learn, Pandas, Numpy, Matplotlib, Seaborn  
- **Modeling:** Time Series Forecasting, Regression (planned), XGBoost (planned)  
- **Deployment:** Flask / FastAPI backend + React frontend (planned)  

---

## 🔹 Internship Note  

This project is developed as part of my **internship program**, with the aim to apply **data science and machine learning techniques** for solving real-world environmental challenges.  

---
