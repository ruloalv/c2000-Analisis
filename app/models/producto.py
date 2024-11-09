# models/producto.py
from sqlalchemy import Column, Integer, String, Float, Date
from config.mysql import Base

class Producto(Base):
    __tablename__ = "productos"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(50))  # 'obra' o 'materia_prima'
    precio_actualizado = Column(Float)
    fecha_precio = Column(Date)
