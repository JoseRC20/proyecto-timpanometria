def datos_paciente():
    """Pide los datos del paciente y devuelve un diccionario."""
    nombre = input("Nombre: ")
    primer_apellido = input("Primer apellido: ")
    segundo_apellido = input("Segundo apellido: ")
    rut = input("Rut: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    return {
        "nombre": nombre,
        "primer_apellido": primer_apellido,
        "segundo_apellido": segundo_apellido,
        "rut": rut,
        "fecha_nacimiento": fecha_nacimiento,
    }


def datos_consulta():
    """Pide los datos de la consulta y devuelve un diccionario."""
    nombre_doctor = input("Doctor: ")
    fecha_consulta = input("Fecha consulta: ")
    return {
        "nombre_doctor": nombre_doctor,
        "fecha_consulta": fecha_consulta,
    }
