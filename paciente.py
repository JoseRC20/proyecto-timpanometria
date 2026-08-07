class Oido:
    def __init__(self, compliancia, presion, gradiente):
        self.compliancia = compliancia
        self.presion = presion
        self.gradiente = gradiente

    def __repr__(self):
        return f"Oido(compliancia={self.compliancia}, presion={self.presion}, gradiente={self.gradiente})"

class Paciente:
    def __init__(self, nombre, primer_apellido, segundo_apellido, rut, fecha_nacimiento, id_paciente=None):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
        self.id_paciente = id_paciente
        self.oido_derecho = None
        self.oido_izquierdo = None

    def cargar_oido(self, lado, compliancia, presion, gradiente):
        """lado debe ser 'derecho' o 'izquierdo'"""
        oido = Oido(compliancia, presion, gradiente)
        if lado == "derecho":
            self.oido_derecho = oido
        elif lado == "izquierdo":
            self.oido_izquierdo = oido
        else:
            raise ValueError("lado debe ser 'derecho' o 'izquierdo'")

    def obtener_oido(self, lado):
        if lado == "derecho":
            return self.oido_derecho
        elif lado == "izquierdo":
            return self.oido_izquierdo
        else:
            raise ValueError("lado debe ser 'derecho' o 'izquierdo'")

    def __repr__(self):
        return f"Paciente({self.nombre}, OD={self.oido_derecho}, OI={self.oido_izquierdo})"

