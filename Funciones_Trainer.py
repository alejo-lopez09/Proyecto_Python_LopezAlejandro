import json


def evaluar_modulo():

    # -------- CARGAR JSON --------
    try:
        with open("Campus.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        print("No existe Campus.json o está vacío.")
        return

    campers = data.get("campers", [])
    trainers = data.get("Trainer", [])
    evaluaciones = data.setdefault("evaluaciones", [])

    # -------- BUSCAR CAMPER --------
    id_buscar = input("Ingrese ID del camper: ")

    camper = next((c for c in campers if c.get("id") == id_buscar), None)

    if not camper:
        print("Camper no encontrado.")
        return

    if camper.get("estado") != "Cursando":
        print("El camper no está cursando ninguna ruta.")
        return

    ruta = camper.get("ruta")

    # -------- BUSCAR TRAINER AUTOMATICO --------
    trainer_id = None
    for t in trainers:
        rutas_t = t.get("ruta", [])
        if ruta in rutas_t:
            trainer_id = t.get("id")
            break

    # -------- DATOS DEL MODULO --------
    modulo = input("Nombre del módulo (ej. Fundamentos): ")
    teorica = float(input("Nota teórica: "))
    practica = float(input("Nota práctica: "))
    quices = float(input("Nota quices/trabajos: "))

    # -------- CALCULO --------
    nota_final = (teorica * 0.3) + (practica * 0.6) + (quices * 0.1)
    aprobado = nota_final >= 60

    # -------- CREAR EVALUACION --------
    evaluacion = {
        "camper_id": id_buscar,
        "ruta": ruta,
        "modulo": modulo,
        "teorica": teorica,
        "practica": practica,
        "quices": quices,
        "nota_final": nota_final,
        "aprobado": aprobado,
        "trainer": trainer_id
    }

    evaluaciones.append(evaluacion)

    # -------- ACTUALIZAR CAMPER --------
    if aprobado:
        print("Módulo aprobado ✅")
    else:
        camper["riesgo"] = "Alto"
        camper["rendimiento"] = "Bajo"
        print("Camper en riesgo académico ⚠️ y en rendimiento Bajo")

    # -------- GUARDAR JSON --------
    with open("Campus.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def reporte_general():
    print("--- REPORTE GENERAL ---")

    # cargar JSON
    try:
        with open("Campus.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        print("No existe Campus.json o está vacío.")
        return

    campers = data.get("campers", [])

    if not campers:
        print("No hay campers registrados.")
        return

    for camper in campers:
        print("------------------------------")
        print("ID:", camper.get("id"))
        print("Nombre:", camper.get("nombre"), camper.get("apellido"))
        print("Estado:", camper.get("estado"))
        print("Riesgo:", camper.get("riesgo"))

        notas = camper.get("notas", [])

        if notas:
            print("Notas:", notas)
        else:
            print("Notas: Sin registros")

def reporte_camper():
    print("--- REPORTE POR CAMPER ---")

    id_buscar = input("Ingrese el ID del camper: ")

    try:
        with open("Campus.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        print("No existe Campus.json o está vacío.")
        return

    campers = data.get("campers", [])

    for camper in campers:
        if camper.get("id") == id_buscar:
            print("\nInformación del Camper")
            print("Nombre:", camper.get("nombre"), camper.get("apellido"))
            print("Estado:", camper.get("estado"))
            print("Riesgo:", camper.get("riesgo"))

            notas = camper.get("notas", [])

            if notas:
                print("Notas:", notas)
            else:
                print("No tiene notas registradas.")
            return

    print("Camper no encontrado.")