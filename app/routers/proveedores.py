from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from config.mysql import get_db
from models.proveedor import Proveedor
# from pydantic import BaseModel

router = APIRouter(prefix="/proveedores",
                   tags=["Proveedores"])

templates = Jinja2Templates(directory="templates")

# class Proveedor(BaseModel):
#     id: int
#     name: str
#     location: str
#     cuit: int
#     active: bool

# proveedores_list = [Proveedor(id=1, name="Trafigura", location="Bahia Blanca", cuit="30311221581", active="true"),
#                   Proveedor(id=2, name="Piro y Ruiz S.R.L.", location="Bahia Blanca", cuit="30311221581", active="true"),
#                   Proveedor(id=3, name="Roza Hnos. S.A.", location="Bahia Blanca", cuit="30311221581", active="true")]

@router.get("/")
async def read_proveedores(request: Request, db: Session = Depends(get_db)):
    # Aquí obtienes los proveedores desde la base de datos
    proveedores = db.query(Proveedor).all()

    return templates.TemplateResponse(
        "proveedores.html",
        {"request": request, "proveedores":proveedores, "submenu_open": True})