
# Heart Disease Predictor

A machine learning-based heart disease prediction system that uses a **Random Forest classification model** and **FastAPI** to provide real-time predictions through a REST API.

## Overview

This project predicts whether a patient has a **low or high risk of heart disease** based on various medical and clinical features.

The project covers the complete workflow from data analysis and machine learning model training to API deployment.

## Project Workflow

```text
Heart Disease Dataset
        ↓
Data Preprocessing
        ↓
Exploratory Data Analysis
        ↓
Model Training
        ↓
Random Forest Model
        ↓
Model Evaluation
        ↓
Save Trained Model
        ↓
FastAPI
        ↓
POST /predict
        ↓
Heart Disease Prediction
```

## Features

The model uses the following patient features:

* `age` – Age of the patient
* `sex` – Sex of the patient
* `cp` – Chest pain type
* `trestbps` – Resting blood pressure
* `chol` – Serum cholesterol
* `fbs` – Fasting blood sugar
* `restecg` – Resting ECG results
* `thalach` – Maximum heart rate achieved
* `exang` – Exercise-induced angina
* `oldpeak` – ST depression induced by exercise
* `slope` – Slope of the peak exercise ST segment
* `ca` – Number of major vessels
* `thal` – Thalassemia value

## Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **FastAPI**
* **Pydantic**
* **Joblib**
* **Jupyter Notebook**

## Machine Learning Model

The project uses **Random Forest** for classification.

Random Forest combines multiple decision trees to make the final prediction. It was selected because it can handle relationships between multiple features and is generally more robust than using a single decision tree.

The trained model is saved as:

```text
heart_model.joblib
```

Joblib is used to save and load the trained machine learning model without retraining it every time the API starts.

## FastAPI

The trained model is integrated with **FastAPI** to create an API for making predictions.

The API contains:

### GET `/`

This endpoint checks whether the API is running.

Example response:

```json
{
    "message": "Heart Disease Prediction API",
    "status": "running",
    "endpoint": "send post request to /predict"
}
```

### POST `/predict`

This endpoint accepts patient information and returns the predicted heart disease risk.

The input data is validated using **Pydantic** before being passed to the machine learning model.

Example request:

```json
{
    "age": 52,
    "sex": 1,
    "cp": 0,
    "trestbps": 125,
    "chol": 212,
    "fbs": 0,
    "restecg": 1,
    "thalach": 168,
    "exang": 0,
    "oldpeak": 1.0,
    "slope": 2,
    "ca": 2,
    "thal": 3
}
```

Example response:

```json
{
    "Prediction": "Low Risk of Heart Disease"
}
```

or

```json
{
    "Prediction": "High Risk of Heart Disease"
}
```

## Project Structure

```text
heart-disease-predictor/
│
├── data.ipynb
├── model.ipynb
├── heart.csv
├── heart_model.joblib
├── heart_conditions.joblib
├── main.py
├── pyvenv.cfg
└── README.md
```

### File Description

| File                      | Purpose                            |
| ------------------------- | ---------------------------------- |
| `heart.csv`               | Heart disease dataset              |
| `data.ipynb`              | Data analysis and preprocessing    |
| `model.ipynb`             | Machine learning model development |
| `heart_model.joblib`      | Saved trained model                |
| `heart_conditions.joblib` | Saved feature information          |
| `main.py`                 | FastAPI application                |
| `README.md`               | Project documentation              |

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/piyushgupta27-dev/heart-disease-predictor.git
```

### 2. Navigate to the project

```bash
cd heart-disease-predictor
```

### 3. Install dependencies

```bash
pip install pandas numpy scikit-learn fastapi uvicorn pydantic joblib
```

### 4. Start the FastAPI server

```bash
uvicorn main:app --reload
```

### 5. Open the API documentation

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

The interactive Swagger UI allows you to test the `/predict` POST endpoint directly.

## Prediction Process

1. User provides patient information.
2. FastAPI receives the POST request.
3. Pydantic validates the input.
4. The input is converted into a Pandas DataFrame.
5. The trained Random Forest model makes the prediction.
6. The API converts the model output into a readable result.
7. The prediction is returned as a JSON response.

## Disclaimer

This project is created for **educational and demonstration purposes only**. The predictions should not be considered medical advice or used as a substitute for professional medical diagnosis.
