from paciente import Paciente
from datos_curva import datos_prueba, preparar_datos, crear_coordenadas, seleccionar_oido
from grafico_curva import graficar
from datos_paciente import datos_paciente, datos_consulta

# --- Datos del paciente y consulta (una sola vez) ---
nombre, primer_apellido, segundo_apellido, rut, fecha_nacimiento = datos_paciente()
nombre_doctor, fecha_consulta = datos_consulta()

p1 = Paciente(nombre, primer_apellido, segundo_apellido, rut, fecha_nacimiento)

# --- Función para no repetir el bloque de proceso + gráfico ---
def procesar_y_graficar_oido(oido):
    mitad_compliance, ancho_1, ancho_2 = preparar_datos(oido.compliancia, oido.presion, oido.gradiente)
    Punto_1, Punto_2, Punto_3 = crear_coordenadas(oido.presion, oido.compliancia, mitad_compliance, ancho_1, ancho_2)
    graficar(Punto_1, Punto_2, Punto_3, mitad_compliance)

# --- Cargar y graficar oído(s) ---
seguir = True
while seguir:
    lado = seleccionar_oido()
    compliancia_estatica, presion, gradiente = datos_prueba()

    p1.cargar_oido(lado, compliancia_estatica, presion, gradiente)
    oido = p1.obtener_oido(lado)
    procesar_y_graficar_oido(oido)

    otro = input("¿Cargar datos del otro oído? (s/n): ").strip().lower()
    seguir = otro == "s"

print(p1)