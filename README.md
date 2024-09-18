/c2000
│
├── /app
│ ├── **init**.py
│ ├── main.py # Archivo principal para iniciar la aplicación
│ ├── /templates # Carpeta para las plantillas HTML (Jinja2)
│ │ └── base.html # Plantilla base HTML
│ └── /static # Carpeta para los archivos estáticos (CSS, JS)
│ ├── /css
│ │ └── styles.css
│ └── /js
│ └── script.js
│
├── .gitignore # Para ignorar archivos innecesarios en Git
├── requirements.txt # Lista de dependencias del proyecto
└── README.md # Documentación del proyecto

# Proyecto de Análisis de Precios

## Descripción

Este proyecto tiene como objetivo crear una aplicación web para cargar datos de materiales, jornales, tiempos estimados de trabajos y maquinarias, con el fin de realizar análisis de precios para obras viales. El frontend está renderizado mediante plantillas HTML usando **Jinja2** y el backend está desarrollado con **FastAPI**.

### **3. Archivos necesarios:**

#### **a. `main.py` (archivo principal del backend):**

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import HTMLResponse

app = FastAPI()

# Servir archivos estáticos como CSS y JS
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configuración para utilizar plantillas Jinja2
templates = Jinja2Templates(directory="app/templates")


# Ruta para la página principal
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})
```
