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
    
    


    }]
trainers=[]
rutas = {
    "NodeJS": {
        "capacidad": 3,
        "inscritos": 0,
        "trainer": None,
        "campers": []
    },
    "Java": {
        "capacidad": 3,
        "inscritos": 0,
        "trainer": None,
        "campers": []
    },
    "NetCore": {
        "capacidad": 3,
        "inscritos": 0,
        "trainer": None,
        "campers": []
    }
}


matriculas={}
evaluaciones={}
riesgo_academico={}
grupos = []
import json



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
        print("Archivo JSON no encontrado, se creará uno nuevo.")




            
            
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
        print("5. Reporte Inscritos")
        print("6. Reporte Aprobados")
        print("7. Reporte Riesgo")
        print("8. Reporte por Ruta")
        print("9. Registrar Trainer")
        print("0. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":
            registrar_camper()
        elif opcion == "2":
            listar_campers()
        elif opcion == "3":
            registrar_examen()
        elif opcion == "4":
            asignar_ruta()
        elif opcion == "5":
            reporte_inscritos()
        elif opcion == "6":
            reporte_aprobados()
        elif opcion == "7":
            reporte_riesgo()
        elif opcion == "8":
            reporte_por_ruta()
        elif opcion == "9":
            registrar_trainer()

        elif opcion == "0":
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

                opcion = input("Seleccione: ")

                if opcion == "1":
                    evaluar_modulo()
                elif opcion == "2":
                    reporte_general()
                elif opcion == "3":
                    reporte_camper()
                elif opcion == "0":
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
            "rutas": rutas
        }, archivo, indent=4)


def registrar_trainer():
    id_trainer = input("ID del trainer: ")
    nombre = input("Nombre: ")
    password_trainer = input("Cree una contraseña para el trainer: ")


    print("Seleccione la ruta que va a entrenar:")

    lista_rutas = list(rutas.keys())

    for i, ruta in enumerate(lista_rutas):
        print(i + 1, ".", ruta)

    opcion = int(input("Opción: "))

    if 1 <= opcion <= len(lista_rutas):
         ruta_seleccionada = lista_rutas[opcion - 1]
    else:
         print("Opción inválida")
         return


    trainer = {
        "id": id_trainer,
        "nombre": nombre,
        "ruta": ruta_seleccionada,
        "password": password_trainer

    }

    trainers.append(trainer)

    rutas[ruta_seleccionada]["trainer"] = nombre

    print("Trainer asignado correctamente.")





            
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


def asignar_ruta():
    id_buscar = input("Ingrese ID del camper: ")

    for camper in campers:
        if camper["id"] == id_buscar:

            if camper["estado"] != "Aprobado":
                print("El camper no ha aprobado el examen inicial.")
                return

            print("Rutas disponibles:")
            for nombre in rutas:
                print("-", nombre)

            ruta_elegida = input("Seleccione la ruta: ")

            if ruta_elegida in rutas:

                if rutas[ruta_elegida]["inscritos"] < rutas[ruta_elegida]["capacidad"]:

                    camper["ruta"] = ruta_elegida
                    camper["estado"] = "Cursando"
                    rutas[ruta_elegida]["inscritos"] += 1
                    rutas[ruta_elegida]["campers"].append(camper["id"])
                    numero_grupo = asignar_grupo(camper["id"])
                    camper["grupo"] = numero_grupo
                    print("Asignado al grupo:", numero_grupo)



                    print("Ruta asignada correctamente ✅")

                else:
                    print("La ruta está llena ❌")
            else:
                print("Ruta no válida")

            return

    print("Camper no encontrado.")






def evaluar_modulo():
    id_buscar = input("Ingrese ID del camper: ")

    for camper in campers:
        if camper["id"] == id_buscar:

            if camper["estado"] != "Cursando":
                print("El camper no está cursando ninguna ruta.")
                return

            teorica = float(input("Nota teórica: "))
            practica = float(input("Nota práctica: "))
            quices = float(input("Nota quices/trabajos: "))

            nota_final = (teorica * 0.3) + (practica * 0.6) + (quices * 0.1)

            camper["notas"].append(nota_final)

            print("Nota final:", nota_final)

            if nota_final < 60:
                camper["riesgo"] = "Alto"
                print("Camper en riesgo académico ⚠️")
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














if __name__ == "__main__":
    cargar_datos()
    menu_principal()
    guardar_datos()
