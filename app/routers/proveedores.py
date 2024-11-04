from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

router = APIRouter(prefix="/proveedores",
                   tags=["Proveedores"])

templates = Jinja2Templates(directory="templates")

class Proveedor(BaseModel):
    id: int
    name: str
    location: str
    cuit: int
    active: bool

proveedores_list = [Proveedor(id=1, name="Trafigura", location="Bahia Blanca", cuit="30311221581", active="true"),
                  Proveedor(id=2, name="Piro y Ruiz S.R.L.", location="Bahia Blanca", cuit="30311221581", active="true"),
                  Proveedor(id=3, name="Roza Hnos. S.A.", location="Bahia Blanca", cuit="30311221581", active="true")]

@router.get("/", response_class=HTMLResponse)
async def obtener_proveedores(request: Request):
    return templates.TemplateResponse(
        "proveedores.html",
        {"request": request, "proveedores":proveedores_list, "submenu_open": True})