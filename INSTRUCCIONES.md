# Guía Paso a Paso: Predicción de Precios de Inmuebles con Docker

Este documento detalla cómo ejecutar la aplicación web que hemos creado para predecir precios de inmuebles utilizando el modelo Random Forest entrenado.

## 📂 Estructura del Proyecto

Tu carpeta de proyecto debería tener ahora esta estructura:

```
/scraping
├── analisis.csv           # Datos de origen
├── train_model.py         # Script para entrenar el modelo
├── requirements.txt       # Dependencias de Python
├── Dockerfile             # Configuración de imagen Docker
├── docker-compose.yml     # Configuración de servicios Docker
└── app/
    ├── main.py            # Backend (FastAPI)
    ├── model.py           # Gestor del modelo
    └── static/            # Frontend
        ├── index.html     # Página web
        ├── style.css      # Estilos
        └── script.js      # Lógica del cliente
```

## 🚀 Cómo Ejecutar el Proyecto (La forma fácil)

Como hemos configurado **Docker**, no necesitas instalar Python ni librerías en tu máquina si no quieres. Solo necesitas Docker Desktop instalado.

### Paso 1: Abrir Terminal
Abre una terminal (PowerShell o CMD) en la carpeta del proyecto:
`cd "c:\Users\sauri\Documents\Proyectos\IA\san isidro\scraping"`

### Paso 2: Construir y Arrancar con Docker
Ejecuta el siguiente comando:

```bash
docker-compose up --build
```

Esto hará lo siguiente automáticamente:
1.  Creará una "imagen" de Linux con Python.
2.  Instalará todas las librerías necesarias.
3.  Ejecutará `train_model.py` para re-entrenar el modelo con los datos más recientes de `analisis.csv` y guardarlo.
4.   Iniciará el servidor web.

### Paso 3: Usar la Aplicación
Una vez veas mensajes en la terminal indicando que el servidor está corriendo (Uvicorn running on...), abre tu navegador y ve a:

👉 **http://localhost:8000/static/index.html**

Aquí verás el formulario. Introduce los datos (habitaciones, metros, etc.) y pulsa "Calcular Precio".

## 🐍 Ejecución Manual (Sin Docker)

Si prefieres correrlo directamente en tu entorno Python local:

1.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Entrenar el modelo:**
    ```bash
    python train_model.py
    ```
    *Esto creará el archivo `app/models/rf_model.pkl`.*

3.  **Iniciar el servidor:**
    ```bash
    python -m uvicorn app.main:app --reload
    ```

4.  **Acceder:** Visita `http://127.0.0.1:8000/static/index.html`

## 🛠️ Descripción Técnica

-   **`train_model.py`**: Es el equivalente a tu Jupyter Notebook pero limpio. Carga `analisis.csv`, limpia los datos (quita columnas inútiles, rellena nulos) y entrena el Random Forest. Luego guarda el modelo en un archivo `.pkl` binario.
-   **`app/main.py`**: Es el cerebro web. Usa FastAPI para recibir los datos del formulario web, pasárselos al modelo, y devolver la predicción.
-   **`app/static/`**: Contiene la interfaz gráfica. Hemos usado un diseño moderno (Glassmorphism) para que se vea profesional.
