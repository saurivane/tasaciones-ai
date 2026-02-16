import pytest
import os
from app.model import Model

def test_model_initialization():
    # Test path that should exist or be handled
    model_path = os.path.join("app", "models", "rf_model.pkl")
    model = Model(model_path=model_path)
    assert model.model_path == model_path

def test_model_prediction_format():
    model_path = os.path.join("app", "models", "rf_model.pkl")
    model = Model(model_path=model_path)
    
    # Example data
    data = {
        "habitaciones": 2,
        "metros": 75,
        "garage": 0,
        "ascensor": 1,
        "ubicacion": 1,
        "numero_planta": 3.0
    }
    
    if model.model is not None:
        prediction = model.predict(data)
        assert isinstance(prediction, float)
    else:
        with pytest.raises(Exception, match="Model not loaded"):
            model.predict(data)
