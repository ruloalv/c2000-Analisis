from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/proveedores",
                   tags="Proveedores")

class Proveedor(BaseModel):
    id: int
    name: str
    location: str

proveedor_list = [Proveedor(id=1, name="Trafigura", location="Bahia Blanca"),
                  Proveedor(id=2, name="Piro y Ruiz S.R.L.", location="Bahia Blanca"),
                  Proveedor(id=3, name="Roza Hnos. S.A.", location="Bahia Blanca")]

@router.get("/")
async def proveedores():
    return proveedor_list