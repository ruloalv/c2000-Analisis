# models/maquinaria.py
from sqlalchemy import Column, Integer, String, Float
from config.mysql import Base

class Maquinaria(Base):
    __tablename__ = "maquinarias"
    
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(100), nullable=False)
    descripcion = Column(String(250))
    precio_compra = Column(Float)
    costo_uso_diario = Column(Float)
    consumo_combustible_hora = Column(Float)
