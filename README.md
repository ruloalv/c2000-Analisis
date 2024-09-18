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
