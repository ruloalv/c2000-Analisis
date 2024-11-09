# models/personal.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base

class Jornal(Base):
    __tablename__ = "jornales"

    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(String(100), nullable=False)
    jornal_actual = Column(Float, nullable=False)
    fecha_inicio = Column(DateTime, default=datetime.now(datetime.timezone.utc))  # Podrías considerar una relación o JSON para esto

    historial_salarios = relationship("HistorialSalario", back_populates="jornal")

    def __repr__(self):
        return f"<jornal(categoria='{self.categoria}', jornal_actual='{self.jornal_actual}')>"

class HistorialSalario(Base):
    __tablename__ = 'historial_salarios'

    id = Column(Integer, primary_key=True)
    jornal_id = Column(Integer, ForeignKey('jornal.id'), nullable=False)
    importe = Column(Float, nullable=False)  # El salario antiguo
    fecha_inicio = Column(DateTime, default=datetime.now(datetime.timezone.utc))  # Fecha en que comenzó el salario antiguo
    fecha_fin = Column(DateTime, nullable=True)  # Fecha en que terminó ese salario (si aplica)

    # Relación con la tabla Personal
    jornal = relationship("Jornal", back_populates="historial_salarios")

    def __repr__(self):
        return f"<HistorialSalario(jornal={self.jornal}, fecha_inicio={self.fecha_inicio}, fecha_fin={self.fecha_fin})>"