from database.conexion import engine
from database.modelos import Base

Base.metadata.create_all(engine)
print("Tablas creadas correctamente.")