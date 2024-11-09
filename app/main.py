from fastapi import FastAPI
from app.models import jornal
from routers import proveedores
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import HTMLResponse
#Import DB data
from config.mysql import engine, Base
from models import proveedor, producto, maquinaria, proyecto, stock

# Crear todas las tablas
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas exitosamente.")

app = FastAPI()

# Servir archivos estáticos como CSS y JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuración para utilizar plantillas Jinja2
templates = Jinja2Templates(directory="templates")


# Ruta para la página principal con Jinja2Templates
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

#Routers
app.include_router(proveedores.router)

@app.get("/")
async def root():
    return ("Hola root")