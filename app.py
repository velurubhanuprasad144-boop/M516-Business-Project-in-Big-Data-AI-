from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd, joblib, json

app = FastAPI(title="Insurance Charges API")
model = joblib.load('gradient_boosting_model.pkl')
scaler = joblib.load('scaler.pkl')
feature_order = json.load(open('feature_order.json'))

class InputData(BaseModel):
    age: int
    sex: int
    bmi: float
    children: int
    smoker: int
    region_northwest: int
    region_southeast: int
    region_southwest: int
    smoker_bmi: float

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/predict")
def predict(payload: InputData):
    df = pd.DataFrame([payload.dict()])[feature_order]
    scaled = scaler.transform(df)
    pred = model.predict(scaled)
    return {"predicted_charge": float(pred)}
