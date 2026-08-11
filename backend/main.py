from paciente import Paciente, Oido
from datos_paciente import datos_paciente, datos_consulta
from datos_curva import seleccionar_oido, datos_prueba, preparar_datos, crear_coordenadas
from grafico_curva import graficar
from generar_pdf import generar_pdf_informe
from database.repositorio import guardar_paciente_completo



def procesar_oido(p1, lado):
    compliancia_estatica, presion, gradiente = datos_prueba()
    mitad_compliance, ancho_1, ancho_2 = preparar_datos(compliancia_estatica, presion, gradiente)
    puntos = crear_coordenadas(presion, compliancia_estatica, mitad_compliance, ancho_1, ancho_2)

    oido = Oido(compliancia_estatica, presion, gradiente, puntos)
    p1.cargar_oido(lado, oido)

    Punto_1, Punto_2, Punto_3 = puntos
    ruta_imagen = f"grafico_{lado}.png"
    graficar(Punto_1, Punto_2, Punto_3, mitad_compliance, lado=lado, guardar_como=ruta_imagen)
    return ruta_imagen


def main():
    nombre, primer_apellido, segundo_apellido, rut, fecha_nacimiento = datos_paciente()
    nombre_doctor, fecha_consulta = datos_consulta()

    p1 = Paciente(nombre, primer_apellido, segundo_apellido, rut, fecha_nacimiento)
    p1.cargar_consulta(nombre_doctor, fecha_consulta)

    imagenes = {}
    seguir = True
    while seguir:
        lado = seleccionar_oido()
        imagenes[lado] = procesar_oido(p1, lado)
        otro = input("¿Cargar datos del otro oído? (s/n): ").strip().lower()
        seguir = otro == "s"
        
    guardar_paciente_completo(p1)

    generar_pdf_informe(
        p1,
        ruta_salida=f"informe_{p1.rut}.pdf",
        imagen_derecho=imagenes.get("derecho"),
        imagen_izquierdo=imagenes.get("izquierdo"),
    )


if __name__ == "__main__":
    main()