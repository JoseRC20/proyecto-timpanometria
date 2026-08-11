def mostrar_datos_paciente(paciente):
    print("\n" + "="*50)
    print("VERIFICACIÓN DE DATOS ANTES DE GENERAR PDF")
    print("="*50)

    print(f"Nombre completo : {paciente.nombre} {paciente.primer_apellido} {paciente.segundo_apellido}")
    print(f"RUT             : {paciente.rut}")
    print(f"Fecha nacimiento: {paciente.fecha_nacimiento}")
    print(f"Doctor          : {paciente.nombre_doctor}")
    print(f"Fecha consulta  : {paciente.fecha_consulta}")

    print("\n--- Oído derecho ---")
    if paciente.oido_derecho:
        od = paciente.oido_derecho
        print(f"  Compliancia: {od.compliancia}")
        print(f"  Presión    : {od.presion}")
        print(f"  Gradiente  : {od.gradiente}")
    else:
        print("  (sin datos)")

    print("\n--- Oído izquierdo ---")
    if paciente.oido_izquierdo:
        oi = paciente.oido_izquierdo
        print(f"  Compliancia: {oi.compliancia}")
        print(f"  Presión    : {oi.presion}")
        print(f"  Gradiente  : {oi.gradiente}")
    else:
        print("  (sin datos)")

    print("="*50 + "\n")