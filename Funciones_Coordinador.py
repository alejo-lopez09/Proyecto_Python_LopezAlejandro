import json
import os


def registrar_camper():

    id = input("ID: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    direccion = input("Direccion: ")
    acudiente = input("Acudiente: ")
    telefono_cel = input("Telefono celular: ")
    telefono_fijo = input("Telefono fijo: ")
    password = input("Cree una contraseña: ")

    camper = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "direccion": direccion,
        "acudiente": acudiente,
        "telefono_cel": telefono_cel,
        "telefono_fijo": telefono_fijo,
        "estado": "inscrito",
        "riesgo": "Bajo",
        "nota_examen": 0,
        "nota_proyecto": 0,
        "nota_quiz": 0,
        "password": password
    }

    archivo = "Campus.json"

    # Si el archivo existe, se lee
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as file:
            datos = json.load(file)
    

    # Agregamos el nuevo camper
    datos["campers"].append(camper)

    # Guardamos nuevamente el archivo
    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)

    print("Camper registrado exitosamente!!!!")

def listar_campers():
    archivo = "Campus.json"

    if not os.path.exists(archivo):
        print("No hay archivo de campers.")
        return

    with open(archivo, "r", encoding="utf-8") as file:
        datos = json.load(file)

    campers = datos.get("campers", [])

    if len(campers) == 0:
        print("No hay campers registrados.")
    else:
        for camper in campers:
            print("----------------------------")
            print("ID:", camper["id"])
            print("Nombre:", camper["nombre"], camper["apellido"])

def registrar_examen():

    with open("Campus.json","r") as f:
        campers = json.load(f)

    id_buscar = input("Ingrese ID del camper: ")

    encontrado = False

    for camper in campers:
        if camper["id"] == id_buscar:
            encontrado = True

            nota_teorica = float(input("Nota teórica: "))
            nota_practica = float(input("Nota práctica: "))

            nota_examen = (nota_teorica + nota_practica) / 2
            camper["nota_examen"] = nota_examen   # ← GUARDAR VARIABLE

            print("Promedio:", nota_examen)

            if nota_examen >= 60:
                camper["estado"] = "Aprobado"
                print("Camper aprobado ✅")
            else:
                camper["estado"] = "No aprobado"
                print("Camper no aprobado ❌")

            break

    if not encontrado:
        print("Camper no encontrado.")

    # GUARDAR CAMBIOS EN JSON
    with open("Campus.json","w") as f:
        json.dump(campers,f,indent=4)

def asignar_ruta():

    # ---- LEER JSON ----
    with open("Campus.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    campers = data["campers"]
    rutas = data["rutas"]

    print("\n--- ASIGNACIÓN DE RUTA ---")
    id_buscar = input("Ingrese el ID del camper aprobado: ")

    camper = next((c for c in campers if c["id"] == id_buscar), None)

    if not camper:
        print("❌ Error: ID no encontrado.")
        return

    # Solo aprobados
    if camper["estado"] != "Aprobado":
        print(f"❌ El camper {camper['nombre']} no está aprobado.")
        return

    print("\n--- Rutas Disponibles ---")

    if not rutas:
        print("No hay rutas creadas.")
        return

    for nombre, info in rutas.items():
        libres = info["capacidad"] - info["inscritos"]
        print(f"{nombre} | Cupos: {libres}/33")

    ruta_elegida = input("Nombre de la ruta a asignar: ")

    if ruta_elegida not in rutas:
        print("❌ Ruta no existe.")
        return

    info_ruta = rutas[ruta_elegida]

    if info_ruta["inscritos"] >= info_ruta["capacidad"]:
        print("❌ Ruta llena.")
        return

    # ---- ACTUALIZAR ----
    camper["ruta"] = ruta_elegida
    camper["estado"] = "Cursando"

    info_ruta["inscritos"] += 1
    info_ruta["campers"].append(camper["id"])

    # ---- GUARDAR JSON ----
    with open("Campus.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✅ {camper['nombre']} asignado a {ruta_elegida}")

def reporte_inscritos():
    print("--- Campers Inscritos ---")

    try:
        with open("Campus.json", "r", encoding="utf-8") as archivo:
            campers = json.load(archivo)
    except FileNotFoundError:
        print("No existe el archivo Campus.json")
        return
    except json.JSONDecodeError:
        print("El JSON está vacío o dañado")
        return

    if not campers:
        print("No hay campers registrados")
        return

    encontrados = False

    for camper in campers:
        if camper.get("estado") == "inscrito":
            print(camper.get("nombre"), camper.get("apellido"))
            encontrados = True

    if not encontrados:
        print("No hay campers inscritos")

def reporte_trainers():
    print("--- Entrenadores registrados ---")

    try:
        with open("Campus.json", "r", encoding="utf-8") as archivo:
            trainers = json.load(archivo)
    except FileNotFoundError:
        print("No existe el archivo Campus.json")
        return
    except json.JSONDecodeError:
        print("El JSON está vacío o dañado")
        return

    if not trainers:
        print("No hay trainers.")
        return

    for t in trainers:
        rutas = t.get("rutas") or t.get("ruta") or "Sin rutas"
        print(f"{t.get('nombre')} {t.get('apellido')} | Rutas: {rutas}")

def reporte_aprobados():
    print("--- Campers Aprobados ---")

    try:
        with open("Campus.json", "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
    except FileNotFoundError:
        print("No existe Campus.json")
        return
    except json.JSONDecodeError:
        print("Campus.json está vacío o dañado")
        return

    
    campers = data if isinstance(data, list) else data.get("campers", [])

    for camper in campers:
        if camper.get("estado", "").lower() == "aprobado":
            print(camper.get("nombre"), camper.get("apellido"))

def reporte_riesgo():
    print("--- Campers en Riesgo Alto ---")

    try:
        with open("Campus.json", "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
    except FileNotFoundError:
        print("No existe Campus.json")
        return
    except json.JSONDecodeError:
        print("Campus.json está vacío o dañado")
        return

    
    campers = data if isinstance(data, list) else data.get("campers", [])

    for camper in campers:
        if camper.get("riesgo", "").lower() == "alto":
            print(camper.get("nombre"), camper.get("apellido"))

def reporte_por_ruta():
    print("--- Campers por Ruta ---")

    try:
        with open("Campus.json", "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
    except FileNotFoundError:
        print("No existe Campus.json")
        return
    except json.JSONDecodeError:
        print("Campus.json está vacío o dañado")
        return

    
    campers = data if isinstance(data, list) else data.get("campers", [])

    for camper in campers:
        ruta = camper.get("ruta")
        if ruta:
            print(camper.get("nombre"), "->", ruta)

def registrar_trainer():
    print("--- REGISTRO DE NUEVO TRAINER ---")

    # Cargar JSON
    try:
        with open("Campus.json", "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
    except:
        data = {}

    # Asegurar estructura
    if "Trainer" not in data:
        data["Trainer"] = []

    if "rutas" not in data:
        data["rutas"] = {}

    id_t = input("ID del trainer: ")
    nombre = input("Nombre completo: ")

    # ---------- RUTAS ----------
    rutas_trainer = []
    print("Ingrese las rutas que maneja el trainer (Enter vacío para terminar):")

    while True:
        r = input("Ruta: ")
        if not r:
            break

        if r in data["rutas"]:
            rutas_trainer.append(r)
        else:
            print(f"La ruta '{r}' no existe. Intente con: {list(data['rutas'].keys())}")

    # ---------- HORARIO ----------
    print("Defina el horario (Formato HH:MM-HH:MM, ej: 06:00-18:00)")
    horario_str = input("Horario: ")

    try:
        inicio, fin = horario_str.split("-")

        def convertir_hora_a_minutos(h):
            horas, minutos = map(int, h.split(":"))
            return horas * 60 + minutos

        inicio_min = convertir_hora_a_minutos(inicio)
        fin_min = convertir_hora_a_minutos(fin)

        if fin_min <= inicio_min:
            print("Error: la hora final debe ser posterior a la inicial.")
            return

        # ---------- NUEVO TRAINER ----------
        nuevo_trainer = {
            "id": id_t,
            "nombre": nombre,
            "ruta": rutas_trainer,
            "horario": {
                "texto": horario_str,
                "inicio": inicio_min,
                "fin": fin_min
            }
        }

        data["Trainer"].append(nuevo_trainer)

        # ---------- GUARDAR JSON ----------
        with open("Campus.json", "w", encoding="utf-8") as archivo:
            json.dump(data, archivo, indent=4, ensure_ascii=False)

        print(f"Trainer {nombre} registrado con éxito con {len(rutas_trainer)} rutas.")

    except ValueError:
        print("Error: formato inválido. Use HH:MM-HH:MM")

def registrar_matricula():

    # ---------- CARGAR JSON ----------
    try:
        with open("Campus.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        print("No existe Campus.json o está vacío.")
        return

    campers = data.get("campers", [])
    trainers = data.get("Trainer", [])
    rutas = data.get("rutas", {})
    matriculas = data.setdefault("matriculas", [])

    # ---------- BUSCAR CAMPER ----------
    id_camper = input("ID del camper a matricular: ")

    camper = next((c for c in campers if c.get("id") == id_camper), None)

    if not camper:
        print("Camper no encontrado.")
        return

    if camper.get("estado") != "Aprobado":
        print("El camper debe estar en estado Aprobado para matricularse.")
        return

    # ---------- MOSTRAR TRAINERS ----------
    if not trainers:
        print("No hay trainers registrados.")
        return

    print("Trainers disponibles:")
    for t in trainers:
        print(f"{t.get('id')} - {t.get('nombre')} | Rutas: {t.get('ruta')}")

    # ---------- SELECCION TRAINER ----------
    id_trainer = input("Ingrese ID del trainer encargado: ")

    trainer = next((t for t in trainers if t.get("id") == id_trainer), None)

    if not trainer:
        print("Trainer no encontrado.")
        return

    # ---------- SELECCION RUTA ----------
    ruta = input("Ingrese ruta asignada (ej: NodeJS): ")

    if ruta not in rutas:
        print("Ruta no válida.")
        return

    # ---------- FECHAS ----------
    fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
    salon = input("Salón de entrenamiento: ")

    # ---------- CREAR MATRICULA ----------
    matricula = {
        "camper_id": id_camper,
        "trainer_id": id_trainer,
        "ruta": ruta,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "salon": salon
    }

    matriculas.append(matricula)

    # opcional: actualizar estado del camper
    camper["estado"] = "Matriculado"

    # ---------- GUARDAR JSON ----------
    with open("Campus.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Matrícula creada correctamente.")

def estadisticas_modulos(ruta_filtro=None, trainer_filtro=None):

    # --------- CARGAR JSON ----------
    try:
        with open("Campus.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        print("No existe Campus.json o está vacío.")
        return

    evaluaciones = data.get("evaluaciones", [])

    if not evaluaciones:
        print("No hay evaluaciones registradas.")
        return

    # --------- PROCESAR ----------
    stats = {}

    for ev in evaluaciones:
        ruta = ev.get("ruta")
        modulo = ev.get("modulo")
        trainer = ev.get("trainer")

        if ruta_filtro and ruta != ruta_filtro:
            continue

        if trainer_filtro and trainer != trainer_filtro:
            continue

        key = (ruta, modulo, trainer)

        if key not in stats:
            stats[key] = {"aprobados": 0, "reprobados": 0, "total": 0}

        stats[key]["total"] += 1

        if ev.get("aprobado"):
            stats[key]["aprobados"] += 1
        else:
            stats[key]["reprobados"] += 1

    # --------- MOSTRAR ----------
    for (ruta, modulo, trainer), v in stats.items():
        print(
            f"Ruta: {ruta} | Módulo: {modulo} | Trainer: {trainer} | "
            f"Aprobados: {v['aprobados']} | Total: {v['total']}"
        )

def crear_ruta():

    nombre = input("Nombre ruta: ")

    # cargar json
    try:
        with open("Campus.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = {}

    # asegurar estructuras
    if "rutas" not in data:
        data["rutas"] = {}
    if "Trainer" not in data:
        data["Trainer"] = []

    # validar duplicado
    if nombre in data["rutas"]:
        print("La ruta ya existe.")
        return

    # mostrar trainers disponibles
    print("\nTrainers disponibles:")
    for t in data["Trainer"]:
        print(f"{t['id']} - {t['nombre']}")

    # pedir IDs de trainers
    trainers_asignados = []
    print("Ingrese IDs de trainers (Enter vacío para terminar):")

    while True:
        id_t = input("ID trainer: ")
        if not id_t:
            break

        existe = any(t["id"] == id_t for t in data["Trainer"])

        if existe:
            if id_t not in trainers_asignados:
                trainers_asignados.append(id_t)
            else:
                print("Ese trainer ya fue agregado.")
        else:
            print("Trainer no existe.")

    # crear ruta
    data["rutas"][nombre] = {
        "capacidad": 33,
        "inscritos": [],
        "trainers": trainers_asignados
    }

    # guardar json
    with open("Campus.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Ruta {nombre} creada con {len(trainers_asignados)} trainer(s).")