from fastapi import FastAPI
from routers import proveedor
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from starlette.requests import Request
# from starlette.responses import HTMLResponse

app = FastAPI()

# Servir archivos estáticos como CSS y JS
# app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configuración para utilizar plantillas Jinja2
# templates = Jinja2Templates(directory="app/templates")


# Ruta para la página principal con Jinja2Templates
# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     return templates.TemplateResponse("base.html", {"request": request})

#Routers
app.include_router(proveedor.router)

@app.get("/")
async def root():
    return ("Hola root")