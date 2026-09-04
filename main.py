from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("heart_model.joblib")
features = joblib.load("heart_conditions.joblib")


class HeartConditions(BaseModel):
    age: float = Field(gt=0, description="Age of the patient")
    sex: float = Field(ge=0, le=1, description="Sex of the patient (0 or 1)")
    cp: float = Field(ge=0, le=3, description="Chest pain type (0 to 3)")
    trestbps: float = Field(gt=0, description="Resting blood pressure")
    chol: float = Field(gt=0, description="Serum cholesterol")
    fbs: float = Field(ge=0, le=1, description="Fasting blood sugar (0 or 1)")
    restecg: float = Field(ge=0, le=2, description="Resting ECG results (0 to 2)")
    thalach: float = Field(gt=0, description="Maximum heart rate achieved")
    exang: float = Field(ge=0, le=1, description="Exercise-induced angina (0 or 1)")
    oldpeak: float = Field(ge=0, description="ST depression induced by exercise")
    slope: float = Field(ge=0, le=2, description="Slope of the peak exercise ST segment")
    ca: float = Field(ge=0, le=4, description="Number of major vessels (0 to 4)")
    thal: float = Field(ge=0, le=3, description="Thalassemia value (0 to 3)")


@app.get("/")
def home():
    return {
        "message": "Heart Disease Prediction API",
        "status": "running",
        "endpoint": "send post request to /predict"
    }


@app.post("/predict")
def predict(heart: HeartConditions):
    try:

        input_data = pd.DataFrame([{
            "age": heart.age,
            "sex": heart.sex,
            "cp": heart.cp,
            "trestbps": heart.trestbps,
            "chol": heart.chol,
            "fbs": heart.fbs,
            "restecg": heart.restecg,
            "thalach": heart.thalach,
            "exang": heart.exang,
            "oldpeak": heart.oldpeak,
            "slope": heart.slope,
            "ca": heart.ca,
            "thal": heart.thal
        }])

        prediction = model.predict(input_data)

        predicted = (
            "Low Risk of Heart Disease"
            if prediction[0] == 0
            else "High Risk of Heart Disease"
        )

        return {
            "Prediction": predicted
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction Failed: {str(e)}"
        )