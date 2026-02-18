def info_camper(camper):
    print("\n--- INFORMACIÓN DEL CAMPER ---")
    print("Nombre:", camper["nombre"], camper["apellido"])
    print("Estado:", camper["estado"])
    print("Riesgo:", camper["riesgo"])

def ver_notas_camper(camper):

    if len(camper["notas"]) > 0:
        print("\nNotas:", camper["notas"])
    else:
        print("\nNo tiene notas registradas")

def ver_horario_camper(camper, matriculas):

    encontrado = False

    for m in matriculas:
        if m["camper_id"] == camper["id"]:
            print("\n--- HORARIO ---")
            print("Ruta:", m["ruta"])
            print("Módulo:", m["modulo"])
            print("Horario:", m["horario"])
            print("Trainer:", m["trainer"])
            encontrado = True
    if not encontrado:
        print("No tiene horario asignado")
