import joblib
import pandas as pd
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
        
        # Ensure input data matches the model's expected format
        # Expected columns: ['habitaciones', 'metros', 'garage', 'ascensor', 'ubicacion', 'numero_planta']
        input_df = pd.DataFrame([data])
        
        # We assume the input dictionary keys match the training columns exactly
        # Ideally, we should validate this against the model's feature_names_in_ if available
        
        prediction = self.model.predict(input_df)[0]
        return prediction
