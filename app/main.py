from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from app.model import Model
import uvicorn
import os

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Load model
model_path = os.path.join("app", "models", "rf_model.pkl")
# Quick fix for path if running from root or inside app
if not os.path.exists(model_path):
     model_path = "models/rf_model.pkl" # Try relative to app folder if docker structure differs

prediction_model = Model(model_path=model_path)

class PropertyData(BaseModel):
    habitaciones: int
    metros: int
    garage: int
    ascensor: int
    ubicacion: int
    numero_planta: float

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Property Price Predictor via FastAPI. Go to /static/index.html for the UI."}

@app.post("/predict")
async def predict(data: PropertyData):
    try:
        # Convert Pydantic model to dict
        input_data = data.dict()
        price = prediction_model.predict(input_data)
        return {"predicted_price": price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
