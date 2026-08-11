from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class PacienteDB(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    primer_apellido = Column(String, nullable=False)
    segundo_apellido = Column(String, nullable=False)
    rut = Column(String, unique=True, nullable=False)
    fecha_nacimiento = Column(String, nullable=False)

    consultas = relationship("ConsultaDB", back_populates="paciente")


class ConsultaDB(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    nombre_doctor = Column(String, nullable=False)
    fecha_consulta = Column(String, nullable=False)

    paciente = relationship("PacienteDB", back_populates="consultas")
    oidos = relationship("OidoDB", back_populates="consulta")


class OidoDB(Base):
    __tablename__ = "oidos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    consulta_id = Column(Integer, ForeignKey("consultas.id"), nullable=False)
    lado = Column(String, nullable=False)  # 'derecho' o 'izquierdo'
    compliancia = Column(Float, nullable=False)
    presion = Column(Integer, nullable=False)
    gradiente = Column(Integer, nullable=False)

    consulta = relationship("ConsultaDB", back_populates="oidos")