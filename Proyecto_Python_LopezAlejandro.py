#=====================
# funciones del coordinador
#=====================
from Funciones_Coordinador import registrar_camper
from Funciones_Coordinador import listar_campers
from Funciones_Coordinador import registrar_examen
from Funciones_Coordinador import asignar_ruta
from Funciones_Coordinador import reporte_inscritos
from Funciones_Coordinador import reporte_trainers
from Funciones_Coordinador import reporte_aprobados
from Funciones_Coordinador import reporte_riesgo
from Funciones_Coordinador import reporte_por_ruta
from Funciones_Coordinador import registrar_trainer
from Funciones_Coordinador import registrar_matricula
from Funciones_Coordinador import estadisticas_modulos
from Funciones_Coordinador import crear_ruta
import json


#=====================
# funciones del treiner
#=====================
from Funciones_Trainer import evaluar_modulo
from Funciones_Trainer import reporte_general
from Funciones_Trainer import reporte_camper


#=====================
# funciones del camper
#=====================
from Funciones_Camper import info_camper
from Funciones_Camper import ver_notas_camper
from Funciones_Camper import ver_horario_camper

#=====================
# variables generales
# #=====================
matriculas=[]
evaluaciones=[]
riesgo_academico={}
grupos = []


password_coordinador = "admin123"
       
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
        print("14, crear ruta")
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
        elif opcion==14:
            crear_ruta()
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

            while True:
                print("\n--- CAMPER ---")
                print("1. Ver información")
                print("2. Ver notas")
                print("3. Ver horario")
                print("0. Volver")

                opcion = input("Seleccione: ")

                if opcion == "1":
                    info_camper(camper)

                elif opcion == "2":
                    ver_notas_camper(camper)

                elif opcion == "3":
                    ver_horario_camper(camper)

                elif opcion == "0":
                    break

                else:
                    print("Opción inválida")

            return

    print("ID o contraseña incorrectos")


#=======================
# funciones generales
#=======================
def convertir_Hora_a_Minutos(hora_str):
    hora, minuto = map(int, hora_str.split(":"))
    return hora * 60 + minuto

def hay_Cruze_Horario(inicio1, fin1, inicio2, fin2):
    return max(inicio1, inicio2) < min(fin1, fin2)

def guardar_datos():
    booleanito=True
    while booleanito==True:
        with open("Campus.json", "w") as archivo_usuarios:
            json.dump({
                print("a")
                
            }, archivo_usuarios, indent=4)
        print ("Se guardo correctamente!!!!")
        booleanito=False

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

def guardar_datos():
    booleanito=True
    while booleanito==True:
        with open("Campus.json", "w") as archivo_usuarios:
            json.dump({
                print("a")
                
            }, archivo_usuarios, indent=4)
        print ("Se guardo correctamente!!!!")
        booleanito=False

def cargar_datos():
    global campers, trainers, rutas, matriculas, evaluaciones, grupos
    try:
        with open("Campus.json", "r") as archivo:
            datos_u = json.load(archivo)
            campers = datos_u.get("campers", [])
            trainers = datos_u.get("trainers", [])
    except FileNotFoundError:
        print("Archivo Campus.json no encontrado.")


    try:
     with open("datos.json", "r") as archivo:
            datos_s = json.load(archivo)
            rutas = datos_s.get("rutas", rutas)
            matriculas = datos_s.get("matriculas", [])
            evaluaciones = datos_s.get("evaluaciones", [])
            grupos = datos_s.get("grupos", [])
    except FileNotFoundError:
        print("Archivo datos.json no encontrado.")


#=======================
# ejecucion de codigo
#=======================
if __name__ == "__main__":
    cargar_datos()
    menu_principal()
    guardar_datos()
