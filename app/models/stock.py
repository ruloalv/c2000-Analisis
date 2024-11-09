# models/stock_despacho.py
from sqlalchemy import Column, Integer, String, Float
from config.mysql import Base

class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer)  # Podrías usar ForeignKey
    cantidad = Column(Integer)
    cliente = Column(String(250))
    tipo_operacion = Column(String(50))  # Venta o compra
