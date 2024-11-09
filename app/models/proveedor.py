# models/proveedor.py
from sqlalchemy import Column, Integer, String
from config.mysql import Base

class Proveedor(Base):
    __tablename__ = "proveedores"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    ubicacion = Column(String(250))
    email = Column(String(100), unique=True)
    pagina_web = Column(String(100))
    domicilio = Column(String(250))
    telefono = Column(String(20))
    contacto = Column(String(100))
    cuit = Column(String(11), unique=True)
    iva = Column(String(50))
