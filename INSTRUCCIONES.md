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
1.  Creará una "imagen" de Linux con Python (ahora incluye soporte para `pandas` y `uvicorn`).
2.  Instalará todas las librerías necesarias.
3.  Iniciará el servidor web.

### Paso 3: Usar la Aplicación
Una vez veas mensajes en la terminal indicando que el servidor está corriendo, abre tu navegador y ve a:

👉 **http://localhost:8000/static/index.html**

El formulario ahora incluye:
*   **Dirección del Inmueble**: Campo obligatorio al inicio.
*   **Cálculo IA**: Predicción de precio y rangos (mínimo/máximo) **redondeados a los millares**.
*   **Integración Google Sheets**: Los leads y la dirección se envían automáticamente al completar el formulario de contacto.

## ☁️ Despliegue en Vercel

El proyecto está configurado para desplegarse en Vercel.
*   Se han optimizado las dependencias (`requirements.txt` ligero sin pandas/numpy) para cumplir los límites de tamaño de Vercel.
*   El archivo `vercel.json` configura las rutas estáticas y la API.

## 🐍 Ejecución Manual (Sin Docker)

Si prefieres correrlo directamente en tu entorno Python local:

1.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    pip install pandas numpy uvicorn
    ```

2.  **Iniciar el servidor:**
    ```bash
    python -m uvicorn app.main:app --reload
    ```

3.  **Acceder:** Visita `http://127.0.0.1:8000/static/index.html`

## 🛠️ Descripción Técnica

-   **`app/main.py`**: Es el cerebro web. Usa FastAPI para recibir los datos del formulario web, pasárselos al modelo, y devolver la predicción.
-   **`app/static/`**: Contiene la interfaz gráfica. Hemos usado un diseño moderno (Glassmorphism) para que se vea profesional.
