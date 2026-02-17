campers=[{
    "id":"1115187651",
    "nombre":"alejo",
    "apellido":"lopez",
    "direccion":"calle 1a #11-40",
    "acudiente":"viviana",
    "telefono_cel":3207895300,
    "telefono_fijo":3137659601,
    "estado":"inscrito",
    "riesgo":"Bajo",
    "notas": [],
    "password":"123456"
    
    


    }]

trainers=[
]
rutas = {
    "NodeJS": {
        "capacidad": 30,
        "inscritos": 0,
        "trainer": None,
        "campers": []
    },
    "Java": {
        "capacidad": 30,
        "inscritos": 0,
        "trainer": None,
        "campers": []
    },
    "NetCore": {
        "capacidad": 30,
        "inscritos": 0,
        "trainer": None,
        "campers": []
    }
}


matriculas=[]
evaluaciones=[]
riesgo_academico={}
grupos = []
import json
from datetime import datetime




password_coordinador = "admin123"



def registrar_camper():
    id=input("ID:")
    nombre=input("Nombre:")
    apellido=input("Apellido:")
    direccion=input("Direccion:")
    acudiente=input("Acudiente:")
    telefono_cel=input("Telefono celular:")
    telefono_fijo=input("Telefono fijo:")
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
        "notas": [],
        "password": password
}
    
    campers.append(camper)
    print("Camper registrado exitosamente!!!!")





def listar_campers():
    if len(campers) == 0:
        print("No hay campers registrados.")
    else:
        for camper in campers:
            print("------------------------")
            print("ID:", camper["id"])
            print("Nombre:", camper["nombre"], camper["apellido"])
            print("Estado:", camper["estado"])
            print("Riesgo:", camper["riesgo"])


def cargar_datos():
    global campers, trainers, rutas

    try:
        with open("datos.json", "r") as archivo:
            datos = json.load(archivo)
            campers = datos["campers"]
            trainers = datos["trainers"]
            rutas = datos["rutas"]
    except FileNotFoundError:
        print("Archivo JSON no encontrado, se creara uno nuevo.")

from datetime import datetime

def registrar_matricula():
    id_camper = input("ID del camper a matricular: ")
    
    camper = next((c for c in campers if c["id"] == id_camper), None)
    if not camper:
        print("Camper no encontrado.")
        return
    if camper.get("estado") != "Aprobado":
        print("El camper debe estar en estado 'Aprobado' para matricularse.")
        return

    
    if len(trainers) == 0:
        print("No hay trainers registrados.")
        return
    print("Trainers disponibles:")
    for t in trainers:
        print(f"{t['id']} - {t['nombre']} (Rutas: {t.get('rutas', t.get('ruta'))})")
    id_trainer = input("Ingrese ID del trainer encargado: ")
    trainer = next((t for t in trainers if t["id"] == id_trainer), None)
    if not trainer:
        print("Trainer no encontrado.")
        return

    ruta = input("Ingrese ruta asignada (ej. NodeJS): ")
    if ruta not in rutas:
        print("Ruta no válida.")
        return

    fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
    salon = input("Salón de entrenamiento: ")

    matricula = {
        "camper_id": id_camper,
        "trainer_id": id_trainer,
        "ruta": ruta,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "salon": salon,
        "fecha_matricula": datetime.now().isoformat()
    }
    matriculas.append(matricula)
    print("Matrícula creada correctamente.")





            
            
def menu_principal():
    while True:
        print("===== SISTEMA CAMPUS =====")
        print("1. Coordinador")
        print("2. Trainer")
        print("3. Camper")
        print("0. Salir")

        opcion = int(input("Seleccione su perfil: "))

        if opcion == 1:
             clave = input("Ingrese contraseña de coordinador: ")
             if clave == password_coordinador:
              menu_coordinador()
             else:
              print("Contraseña incorrecta")

        elif opcion == 2:
            menu_trainer()
        elif opcion == 3:
            menu_camper()
        elif opcion == 0:
            print("Saliendo...")
            break
        else:
            print("Opción inválida")



def menu_coordinador():
    while True:
        print("--- COORDINADOR ---")
        print("1. Registrar Camper")
        print("2. Listar Campers")
        print("3. Registrar Examen Inicial")
        print("4. Asignar Ruta")
        print("5. Crear ruta")
        print("6. Reporte Inscritos")
        print("7. Reporte Trainers")
        print("8. Reporte Aprobados")
        print("9. Reporte Riesgo")
        print("10. Reporte por Ruta")
        print("11. Registrar Trainer")
        print("12. Registrar Matricula")
        print("13. Estadistica de modulos")
        print("0. Volver")

        opcion =int(input("Seleccione: "))

        if opcion == 1:
            registrar_camper()
        elif opcion == 2:
            listar_campers()
        elif opcion == 3:
            registrar_examen()
        elif opcion == 4:
            asignar_ruta()
        elif opcion==5:
            crear_ruta()
        elif opcion == 6:
            reporte_inscritos()
        elif opcion==7:
            reporte_trainers()

            
        elif opcion == 8:
            reporte_aprobados()
        elif opcion == 9:
            reporte_riesgo()
        elif opcion == 10:
            reporte_por_ruta()
        elif opcion == 11:
            registrar_trainer()
        elif opcion==12:
            registrar_matricula()
        elif opcion==13:
            estadisticas_modulos()

        elif opcion == 0:
            break
        else:
            print("Opción inválida")


def menu_trainer():
    id_buscar = input("Ingrese su ID de trainer: ")
    clave = input("Ingrese su contraseña: ")

    for trainer in trainers:
        if trainer["id"] == id_buscar and trainer["password"] == clave:

            while True:
                print("--- TRAINER ---")
                print("1. Evaluar Módulo")
                print("2. Reporte General")
                print("3. Reporte por Camper")
                print("0. Volver")

                opcion =int(input("Seleccione: "))

                if opcion == 1:
                    evaluar_modulo()
                elif opcion == 2:
                    reporte_general()
                elif opcion == 3:
                    reporte_camper()
                elif opcion == 0:
                    break
                else:
                    print("Opción inválida")
            return

    print("ID o contraseña incorrectos.")




def menu_camper():
    id_buscar = input("Ingrese su ID: ")
    clave = input("Ingrese su contraseña: ")

    for camper in campers:
        if camper["id"] == id_buscar and camper["password"] == clave:
            print("--- INFORMACIÓN DEL CAMPER ---")
            print("Nombre:", camper["nombre"])
            print("Estado:", camper["estado"])
            print("Riesgo:", camper["riesgo"])
            print("Notas:", camper["notas"])
            return

    print("ID o contraseña incorrectos.")

def guardar_datos():
    with open("datos.json", "w") as archivo:
        json.dump({
            "campers": campers,
            "trainers": trainers,
            "rutas": rutas,
            "matriculas": matriculas,
            "evaluaciones": evaluaciones,
            "grupos": grupos
        }, archivo, indent=4)


def registrar_trainer():
    print("--- REGISTRO DE NUEVO TRAINER ---")
    id_t = input("ID del trainer: ")
    nombre = input("Nombre completo: ")
    
    
    rutas_trainer = []
    print("Ingrese las rutas que maneja el trainer (presione Enter vacío para terminar):")
    while True:
        r = input("- Ruta: ")
        if not r: 
            break
        # Validamos que la ruta exista en nuestro sistema
        if r in rutas:
            rutas_trainer.append(r)
        else:
            print(f" La ruta '{r}' no existe en el sistema. Intente con: {list(rutas.keys())}")

    # Registro de horario flexible
    print("Defina el horario (Formato HH:MM, ej: 06:00-18:00):")
    horario_str = input("Horario: ")
    
    try:
        h_inicio, h_fin = horario_str.split("-")
        inicio = convertir_Hora_a_Minutos(h_inicio)
        fin = convertir_Hora_a_Minutos(h_fin)
        
        # Ahora solo validamos que la hora final sea después de la inicial
        if fin <= inicio:
         print("❌ Error: La hora de finalización debe ser posterior a la de inicio.")
         return

        # Creamos el perfil del trainer
        nuevo_trainer = {
            "id": id_t,
            "nombre": nombre,
            "rutas": rutas_trainer,
            "horario": {
                "texto": horario_str,
                "inicio_min": inicio,
                "fin_min": fin
            }
        }
        
        trainers.append(nuevo_trainer)
        print(f"✅ Trainer {nombre} registrado con éxito con {len(rutas_trainer)} rutas.")
        
    except ValueError:
        print("❌ Error: Formato de horario inválido. Use HH:MM-HH:MM")





            
def registrar_examen():
    id_buscar = input("Ingrese ID del camper: ")

    encontrado = False

    for camper in campers:
        if camper["id"] == id_buscar:
            encontrado = True

            nota_teorica = float(input("Nota teórica: "))
            nota_practica = float(input("Nota práctica: "))

            promedio = (nota_teorica + nota_practica) / 2

            print("Promedio:", promedio)

            if promedio >= 60:
                camper["estado"] = "Aprobado"
                print("Camper aprobado ✅")
            else:
                print("Camper no aprobado ❌")

    if not encontrado:
        print("Camper no encontrado.")


def crear_ruta():
    nombre = input("Nombre ruta: ")
    base_datos_principal = input("SGDB principal: ")
    base_datos_alterna = input("SGDB alterno: ")
    modulos = []
    print("Ingrese módulos (enter vacío para terminar):")
    while True:
        m = input("Módulo: ")
        if not m: break
        modulos.append(m)
    rutas[nombre] = {
        "capacidad": 30,
        "inscritos": 0,
        "trainer": None,
        "campers": [],
        "base_datos_principal": base_datos_principal,
        "base_datos_alterno": base_datos_alterna,
        "modulos": modulos
    }
    print("Ruta creada.")



def asignar_ruta():
    print("--- ASIGNACIÓN DE RUTA ---")
    id_buscar = input("Ingrese el ID del camper aprobado: ")

    
    camper = next((c for c in campers if c["id"] == id_buscar), None)

    if not camper:
        print("❌ Error: El ID ingresado no coincide con ningún camper registrado.")
        return

    # REQUERIMIENTO: Solo campers que pasaron de "Inscritos" a "Aprobados"
    if camper["estado"] != "Aprobado":
        print(f"❌ Error: El camper '{camper['nombre']}' tiene estado '{camper['estado']}'.")
        print("Solo los campers con estado 'Aprobado' pueden ser asignados a una ruta.")
        return

    # Listar rutas creadas para que el usuario elija
    print("\n--- Rutas Disponibles ---")
    if not rutas:
        print("No hay rutas creadas actualmente.")
        return
        
    for nombre, info in rutas.items():
       
        cupos_libres = info["capacidad"] - info["inscritos"]
        print(f"- {nombre} | Cupos disponibles: {cupos_libres}/33")

    ruta_elegida = input("\nNombre de la ruta a asignar: ")

    if ruta_elegida in rutas:
        info_ruta = rutas[ruta_elegida]
        
        # Validación de capacidad
        if info_ruta["inscritos"] < info_ruta["capacidad"]:
            
            # 1. Actualizar datos del camper
            camper["ruta"] = ruta_elegida
            camper["estado"] = "Cursando" 
            
            # 2. Actualizar datos de la ruta
            info_ruta["inscritos"] += 1
            info_ruta["campers"].append(camper["id"])
            
            # 3. Asignación de grupo 
            numero_grupo = asignar_grupo(camper["id"])
            camper["grupo"] = numero_grupo
            
            print(f"✅ ¡Éxito! El camper {camper['nombre']} ha sido asignado a la {ruta_elegida}.")
            print(f"Asignado al Grupo: {numero_grupo}")
        else:
            print(f"❌ Error: La ruta '{ruta_elegida}' ya alcanzó su capacidad máxima de 33.")
    else:
        print("❌ Error: La ruta seleccionada no existe.")






def evaluar_modulo():
    id_buscar = input("Ingrese ID del camper: ")

    for camper in campers:
        if camper["id"] == id_buscar:
            if camper.get("estado") != "Cursando":
                print("El camper no está cursando ninguna ruta.")
                return

            modulo = input("Nombre del módulo (ej. Fundamentos): ")
            teorica = float(input("Nota teórica: "))
            practica = float(input("Nota práctica: "))
            quices = float(input("Nota quices/trabajos: "))
            nota_final = (teorica * 0.3) + (practica * 0.6) + (quices * 0.1)
            aprobado = nota_final >= 60

            
            evaluacion = {
                "camper_id": id_buscar,
                "ruta": camper.get("ruta"),
                "modulo": modulo,
                "teorica": teorica,
                "practica": practica,
                "quices": quices,
                "nota_final": nota_final,
                "aprobado": aprobado,
                "fecha": datetime.now().isoformat(),
                "trainer": None  
            }
            evaluaciones.append(evaluacion)
            camper["notas"].append(nota_final)

            
            if not aprobado:
                camper["riesgo"] = "Alto"
                camper["rendimiento"] = "Bajo"  
                
                print("Camper en riesgo académico ⚠️ y en rendimiento Bajo")
            else:
                print("Módulo aprobado ✅")

            return

    print("Camper no encontrado.")




def menu_reportes():
    while True:
        print("\n--- MENU REPORTES ---")
        print("1. Reporte general")
        print("2. Reporte por estudiante")
        print("3. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            reporte_general()
        elif opcion == "2":
            reporte_camper()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


def reporte_general():
    print("--- REPORTE GENERAL ---")

    if len(campers) == 0:
        print("No hay campers registrados.")
        return

    for camper in campers:
        print("----------------------------")
        print("ID:", camper["id"])
        print("Nombre:", camper["nombre"], camper["apellido"])
        print("Estado:", camper["estado"])
        print("Riesgo:", camper["riesgo"])

        if len(camper["notas"]) > 0:
            print("Notas:", camper["notas"])
        else:
            print("Notas: Sin registros")

def reporte_camper():
    print("--- REPORTE POR CAMPER ---")

    id_buscar = input("Ingrese el ID del camper: ")

    for camper in campers:
        if camper["id"] == id_buscar:
            print("\nInformación del Camper")
            print("Nombre:", camper["nombre"], camper["apellido"])
            print("Estado:", camper["estado"])
            print("Riesgo:", camper["riesgo"])

            if len(camper["notas"]) > 0:
                print("Notas:", camper["notas"])
            else:
                print("No tiene notas registradas.")

            return

    print("Camper no encontrado.")


def reporte_inscritos():
    print("--- Campers Inscritos ---")
    for camper in campers:
        if camper["estado"] == "inscrito":
            print(camper["nombre"], camper["apellido"])


def reporte_aprobados():
    print("--- Campers Aprobados ---")
    for camper in campers:
        if camper["estado"] == "Aprobado":
            print(camper["nombre"], camper["apellido"])


def reporte_riesgo():
    print("--- Campers en Riesgo Alto ---")
    for camper in campers:
        if camper["riesgo"] == "Alto":
            print(camper["nombre"], camper["apellido"])


def reporte_por_ruta():
    print("--- Campers por Ruta ---")
    for camper in campers:
        if "ruta" in camper and camper["ruta"] != None:
            print(camper["nombre"], "-", camper["ruta"])


def reporte_rutas():
    print("--- REPORTE DE RUTAS ---")

    for nombre, datos in rutas.items():
        print("\nRuta:", nombre)
        print("Trainer:", datos["trainer"])
        print("Capacidad:", datos["capacidad"])
        print("Inscritos:", datos["inscritos"])

        if len(datos["campers"]) == 0:
         print("Campers: Ninguno")
        else:
         print("Campers inscritos:")
    
         for id_camper in datos["campers"]:
             for camper in campers:
                 if camper["id"] == id_camper:
                     print("-", camper["nombre"], camper["apellido"])
        


def estadisticas_modulos(ruta_filtro=None, trainer_filtro=None):
    
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
        if ev["aprobado"]:
            stats[key]["aprobados"] += 1
        else:
            stats[key]["reprobados"] += 1

    
    for (ruta, modulo, trainer), v in stats.items():
        print(f"Ruta: {ruta} | Módulo: {modulo} | Trainer: {trainer}")
        print(f"  Aprobados: {v['aprobados']}  Reprobados: {v['reprobados']}  Total: {v['total']}")





def asignar_grupo(camper_id):
    for grupo in grupos:
        if len(grupo["miembros"]) < 30:
            grupo["miembros"].append(camper_id)
            return grupo["numero"]

    
    nuevo_grupo = {
        "numero": len(grupos) + 1,
        "miembros": [camper_id]
    }

    grupos.append(nuevo_grupo)
    return nuevo_grupo["numero"]


def reporte_trainers():
    print("--- Entrenadores registrados ---")
    if not trainers:
        print("No hay trainers.")
    for t in trainers:
        print(f"ID: {t['id']} | Nombre: {t['nombre']} | Rutas: {t.get('rutas', t.get('ruta'))}")




def cargar_datos():
    global campers, trainers, rutas, matriculas, evaluaciones, grupos
    try:
        with open("datos.json", "r") as archivo:
            datos = json.load(archivo)
            campers = datos.get("campers", campers)
            trainers = datos.get("trainers", trainers)
            rutas = datos.get("rutas", rutas)
            matriculas = datos.get("matriculas", [])
            evaluaciones = datos.get("evaluaciones", [])
            grupos = datos.get("grupos", [])
    except FileNotFoundError:
        print("Archivo JSON no encontrado, se creará uno nuevo.")



def convertir_Hora_a_Minutos(hora_str):
    hora, minuto = map(int, hora_str.split(":"))
    return hora * 60 + minuto

def hay_Cruze_Horario(inicio1, fin1, inicio2, fin2):
    return max(inicio1, inicio2) < min(fin1, fin2)









if __name__ == "__main__":
    cargar_datos()
    
    menu_principal()
    guardar_datos()
