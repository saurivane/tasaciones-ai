# 🏡 Predictor Valor Inmueble (IA)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)

Este proyecto es una aplicación web completa que utiliza Inteligencia Artificial para predecir el precio de inmuebles basándose en datos reales del mercado. Incluye desde el análisis de datos y entrenamiento del modelo hasta una interfaz de usuario moderna lista para producción.

## ✨ Características

- **Modelo de IA**: Regresores basados en **Random Forest** entrenados con datos históricos.
- **Backend**: API robusta construida con **FastAPI**.
- **Frontend**: Interfaz de usuario moderna con diseño **Glassmorphism** y temática verde profesional.
- **Nuevas Funcionalidades**:
    -   📍 **Campo de Dirección**: Captura la ubicación exacta del inmueble.
    -   📊 **Integración Google Sheets**: Exportación automática de leads y valoraciones.
    -   💰 **Precios Redondeados**: Visualización amigable de rangos de precio.
- **Contenedorizado**: Totalmente preparado para correr con **Docker** y **Docker Compose**.
- **Despliegue**: Configurado para despliegue continuo en **Vercel**.

## 🛠️ Stack Tecnológico

- **Análisis y ML**: Python, Pandas, Scikit-Learn, Joblib.
- **API**: FastAPI, Uvicorn, Pydantic.
- **Frontend**: HTML5, Vanilla CSS, JavaScript (Fetch API).
- **Infraestructura**: Docker, Vercel.

## 🚀 Instalación y Uso

### 🐳 Con Docker (Recomendado)

Asegúrate de tener Docker instalado y ejecutándose, luego:

1. Clona el repositorio.
2. Abre una terminal en la carpeta raíz.
3. Ejecuta:
   ```bash
   docker-compose up --build
   ```
4. Accede a la aplicación en: `http://localhost:8000/static/index.html`

### ☁️ Despliegue en Vercel

```bash
vercel --prod
```

### 🐍 Ejecución Local (Opcional)

Si prefieres ejecutarlo sin Docker:

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   pip install pandas numpy uvicorn
   ```
2. Inicia el servidor:
   ```bash
   python -m uvicorn app.main:app --reload
   ```
3. Abre: `http://127.0.0.1:8000/static/index.html`

## 📂 Estructura del Proyecto

```text
├── app/
│   ├── main.py          # Servidor FastAPI
│   ├── model.py         # Interfaz de predicción del modelo
│   ├── models/          # Modelos entrenados (.pkl)
│   └── static/          # Archivos del Frontend (HTML, CSS, JS)
├── train_model.py       # Script de entrenamiento y limpieza de datos
├── analisis.csv         # Dataset utilizado
├── Dockerfile           # Configuración de imagen Docker
├── docker-compose.yml   # Definición de servicios
├── requirements.txt      # Dependencias de Python
└── README.md            # Documentación del proyecto
```

## Estructura de datos

El fichero "analisis.csv" contiene los datos utilizados para entrenar el modelo con las siguientes columnas:
- habitaciones
- metros
- numero_planta
- garage
- ascensor
- ubicacion
- precio



---
Proyecto desarrollado para el análisis y predicción de precios inmobiliarios.