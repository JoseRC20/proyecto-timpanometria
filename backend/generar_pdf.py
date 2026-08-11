from fpdf import FPDF

class InformePDF(FPDF):
    def header(self):
        self.image("Impedanciometría.png", x=0, y=0, w=210, h=297)


def generar_pdf_informe(paciente, ruta_salida="informe.pdf", imagen_derecho=None, imagen_izquierdo=None):
    pdf = InformePDF(format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica", size=11)

    # --- Datos del paciente (fila 1 y 2) ---
    pdf.set_xy(47, 15)
    pdf.cell(0, 6, f"{paciente.nombre}")

    pdf.set_xy(126, 15)
    pdf.cell(0, 6, f"{paciente.rut}")

    pdf.set_xy(47, 24)
    pdf.cell(0, 6, f"{paciente.primer_apellido} {paciente.segundo_apellido}")

    pdf.set_xy(138, 24)
    pdf.cell(0, 6, f"{paciente.fecha_nacimiento}")

    # --- Doctor y consulta (fila 3) ---
    pdf.set_xy(43, 33)
    pdf.cell(0, 6, f"{paciente.nombre_doctor}")

    pdf.set_xy(136, 33)
    pdf.cell(0, 6, f"{paciente.fecha_consulta}")

    # --- Tabla de parámetros ---
    pdf.set_font("Helvetica", size=10)

    if paciente.oido_izquierdo:
        oi = paciente.oido_izquierdo
        pdf.set_xy(95, 63);  pdf.cell(30, 6, f"{oi.compliancia} ml", align="C")
        pdf.set_xy(95, 75);  pdf.cell(30, 6, f"{oi.presion} daPa", align="C")
        pdf.set_xy(95, 87);  pdf.cell(30, 6, f"{oi.gradiente} daPa", align="C")

    if paciente.oido_derecho:
        od = paciente.oido_derecho
        pdf.set_xy(124, 63); pdf.cell(30, 6, f"{od.compliancia} ml", align="C")
        pdf.set_xy(124, 75); pdf.cell(30, 6, f"{od.presion} daPa", align="C")
        pdf.set_xy(124, 87); pdf.cell(30, 6, f"{od.gradiente} daPa", align="C")

    # --- Gráficos (debajo de "Frecuencia: 226 HZ") ---
    if imagen_izquierdo:
        pdf.image(imagen_izquierdo, x=30, y=115, w=120)

    if imagen_derecho:
        pdf.image(imagen_derecho, x=30, y=200, w=120)

    pdf.output(ruta_salida)
    print(f"PDF generado: {ruta_salida}")