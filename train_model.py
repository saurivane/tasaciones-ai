import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# Create model directory if it doesn't exist
os.makedirs('app/models', exist_ok=True)

def train():
    print("Loading data...")
    # Load data
    try:
        df = pd.read_csv('analisis.csv')
    except FileNotFoundError:
        print("Error: analisis.csv not found.")
        return

    # Preprocessing (copied logic from ml_model.ipynb)
    cols_to_drop = ['nombre', 'url', 'id_inmueble', 'precio', 'valor_garage', 'planta', 'vendedor']
    df = df.drop(columns=cols_to_drop, errors='ignore')

    # Impute missing values
    df['numero_planta'] = df['numero_planta'].fillna(-1)

    # Encode boolean/categorical variables
    df['garage'] = df['garage'].astype(int)
    df['ascensor'] = df['ascensor'].astype(int)

    ubicacion_map = {'Exterior': 1, 'Interior': 0, 'No especificado': -1}
    # Check type before mapping
    if df['ubicacion'].dtype == 'O':
         df['ubicacion'] = df['ubicacion'].map(ubicacion_map).fillna(-1)
    else:
         df['ubicacion'] = df['ubicacion'].fillna(-1)

    print("Data loaded and preprocessed.")
    print(df.info())

    # Split data
    X = df.drop(columns=['precio_total'])
    y = df['precio_total']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model with best parameters from notebook
    # {'max_depth': 10, 'min_samples_split': 2, 'n_estimators': 100}
    print("Training Random Forest model...")
    rf = RandomForestRegressor(
        n_estimators=100, 
        max_depth=10, 
        min_samples_split=2, 
        random_state=42
    )
    rf.fit(X_train, y_train)

    # Evaluate
    y_pred = rf.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print(f"Model Evaluation:")
    print(f"RMSE: {rmse:,.2f}")
    print(f"R2 Score: {r2:.4f}")

    # Save model
    model_path = 'app/models/rf_model.pkl'
    joblib.dump(rf, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train()
