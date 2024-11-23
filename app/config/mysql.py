from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuración de conexión
DB_HOST = "autorack.proxy.rlwy.net"
DB_PORT = "50812"
DB_USER = "root"
DB_PASSWORD = "dbLnhTjzsETZAlKEBfKoVFeCJfKsiDUw"
DB_NAME = "railway"

# Cadena de conexión
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Configuración de la base de datos
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()