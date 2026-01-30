import joblib
import os

class Model:
    def __init__(self, model_path="app/models/rf_model.pkl"):
        self.model_path = model_path
        self.model = None
        self.load_model()

    def load_model(self):
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            print(f"Model loaded from {self.model_path}")
        else:
            print(f"Model not found at {self.model_path}")

    def predict(self, data: dict):
        if not self.model:
            raise Exception("Model not loaded")
        
        # We extract the values in the exact order the model was trained on:
        # ['habitaciones', 'metros', 'garage', 'ascensor', 'ubicacion', 'numero_planta']
        input_data = [[
            data['habitaciones'],
            data['metros'],
            data['garage'],
            data['ascensor'],
            data['ubicacion'],
            data['numero_planta']
        ]]
        
        prediction = self.model.predict(input_data)[0]
        return float(prediction)
