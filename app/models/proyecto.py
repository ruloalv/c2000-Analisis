# models/proyecto.py
from sqlalchemy import Column, Integer, String, Date, Float
from config.mysql import Base

class Proyecto(Base):
    __tablename__ = "proyectos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    fecha_analisis = Column(Date)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    ubicacion = Column(String(200))
    presupuesto_estimado = Column(Float)
