from database.conexion import obtener_sesion
from database.modelos import PacienteDB, ConsultaDB, OidoDB


def guardar_paciente_completo(paciente):
    """Recibe un objeto Paciente (de paciente.py) y lo guarda en la BD."""
    sesion = obtener_sesion()
    try:
        # Buscar si el paciente ya existe por RUT
        paciente_db = sesion.query(PacienteDB).filter_by(rut=paciente.rut).first()

        if not paciente_db:
            paciente_db = PacienteDB(
                nombre=paciente.nombre,
                primer_apellido=paciente.primer_apellido,
                segundo_apellido=paciente.segundo_apellido,
                rut=paciente.rut,
                fecha_nacimiento=paciente.fecha_nacimiento,
            )
            sesion.add(paciente_db)
            sesion.flush()  # para obtener el id generado antes del commit

        consulta_db = ConsultaDB(
            paciente_id=paciente_db.id,
            nombre_doctor=paciente.nombre_doctor,
            fecha_consulta=paciente.fecha_consulta,
        )
        sesion.add(consulta_db)
        sesion.flush()

        if paciente.oido_derecho:
            od = paciente.oido_derecho
            sesion.add(OidoDB(
                consulta_id=consulta_db.id, lado="derecho",
                compliancia=od.compliancia, presion=od.presion, gradiente=od.gradiente,
            ))

        if paciente.oido_izquierdo:
            oi = paciente.oido_izquierdo
            sesion.add(OidoDB(
                consulta_id=consulta_db.id, lado="izquierdo",
                compliancia=oi.compliancia, presion=oi.presion, gradiente=oi.gradiente,
            ))

        sesion.commit()
        print(f"Paciente {paciente.rut} guardado en la base de datos (consulta id={consulta_db.id}).")
        return consulta_db.id

    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar en la base de datos: {e}")
        raise
    finally:
        sesion.close()


def buscar_paciente_por_rut(rut):
    sesion = obtener_sesion()
    try:
        return sesion.query(PacienteDB).filter_by(rut=rut).first()
    finally:
        sesion.close()