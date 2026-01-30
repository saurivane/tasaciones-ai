# Implementation Plan - Property Price Prediction Landing Page

The goal is to create a web application where users can input property details to get a price prediction, based on the analysis from `ml_model.ipynb`.

## Proposed Changes

### Backend (Python/FastAPI)
#### [NEW] [train_model.py](file:///c:/Users/sauri/Documents/Proyectos/IA/san%20isidro/scraping/train_model.py)
- Script to train the Random Forest model using `analisis.csv`.
- Saves the trained model to `app/models/rf_model.pkl`.
- Uses the hyperparameters found in the notebook: `n_estimators=100`, `max_depth=10`, `min_samples_split=2`.

#### [NEW] [app/main.py](file:///c:/Users/sauri/Documents/Proyectos/IA/san%20isidro/scraping/app/main.py)
- FastAPI application.
- Endpoint `/predict` to accept JSON payload: `habitaciones`, `metros`, `garage`, `ascensor`, `ubicacion`, `numero_planta`.
- Serves static files for the frontend.

#### [NEW] [app/model.py](file:///c:/Users/sauri/Documents/Proyectos/IA/san%20isidro/scraping/app/model.py)
- Helper class to load the model and make predictions.

### Frontend (HTML/CSS/JS)
#### [NEW] [app/static/index.html](file:///c:/Users/sauri/Documents/Proyectos/IA/san%20isidro/scraping/app/static/index.html)
- Modern landing page with a form for property details.
- "Calculate Price" button.
- Result display area.

#### [NEW] [app/static/style.css](file:///c:/Users/sauri/Documents/Proyectos/IA/san%20isidro/scraping/app/static/style.css)
- Aesthetic styling (glassmorphism/modern UI).

#### [NEW] [app/static/script.js](file:///c:/Users/sauri/Documents/Proyectos/IA/san%20isidro/scraping/app/static/script.js)
- Handles form submission.
- Calls the `/predict` API.
- Updates the UI with the result.

### Infrastructure
#### [NEW] [Dockerfile](file:///c:/Users/sauri/Documents/Proyectos/IA/san%20isidro/scraping/Dockerfile)
- Python 3.9+ image.
- Installs dependencies.
- Runs `train_model.py` (optional, or pre-trained) and starts FastAPI.

#### [NEW] [docker-compose.yml](file:///c:/Users/sauri/Documents/Proyectos/IA/san%20isidro/scraping/docker-compose.yml)
- Service definition for the web app.

#### [NEW] [requirements.txt](file:///c:/Users/sauri/Documents/Proyectos/IA/san%20isidro/scraping/requirements.txt)
- `fastapi`, `uvicorn`, `pandas`, `scikit-learn`, `joblib`.

## Verification Plan
### Automated Tests
- Run `train_model.py` to ensure model is created.
- Start API locally `uvicorn app.main:app --reload` and test `/predict` with curl/Postman.
- Build Docker image and run container.

### Manual Verification
- Open `http://localhost:8000` in browser.
- Fill out the form and check if the price is realistic.
