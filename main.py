from datos_curva import datos_prueba, preparar_datos, crear_coordenadas
from grafico_curva import graficar
from datos_paciente import datos_paciente, datos_consulta

nombre, primer_apellido, segundo_apellido, rut, fecha_nacimiento = datos_paciente()
nombre_doctor, fecha_consulta = datos_consulta()

compliancia_estatica, presion, gradiente = datos_prueba()
mitad_compliance, ancho_1, ancho_2 = preparar_datos(compliancia_estatica, presion, gradiente)
Punto_1, Punto_2, Punto_3 = crear_coordenadas(presion, compliancia_estatica, mitad_compliance, ancho_1, ancho_2)

graficar(Punto_1, Punto_2, Punto_3, mitad_compliance)