from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("regression.joblib")

class HouseFeatures(BaseModel):
    size: float
    nb_rooms: int
    garden: int

@app.get("/predict")
def predict(size: float, nb_rooms: int, garden: int):
    y_pred = model.predict([[size, nb_rooms, garden]])
    return {"y_pred": float(y_pred[0])}

@app.post("/predict")
def predict_post(features: HouseFeatures):
    y_pred = model.predict([[features.size, features.nb_rooms, features.garden]])
    return {"y_pred": float(y_pred[0])}
