from datetime import date
import json
import time
from variables import get_computer_points,get_user_points,get_max_points
from datetime import date
from datetime import datetime


#Fecha actual
now = datetime.now()


def guardar_historial():

    historial = abrir_archivo("historial.json")

    if historial ==  False:
        historial = []

    historial.append({
        "puntos_computadora":get_computer_points(),
        "puntos_usuario":get_user_points(),
        "puntos_maximos":get_max_points(),

     })

    guardar_archivo("historial.json", historial)

def guardar_partida():

    guardar_archivo("partida_guardada.json", {
        "puntos_computadora":get_computer_points(),
        "puntos_usuario":get_user_points(),
        "puntos_maximos":get_max_points(),
    })


def ver_historial():
    historial = abrir_archivo("historial.json")

    if historial == False:
        print("no tenes historial aun")

    else:
        for index, partida in enumerate(historial):
            print(f"{index}) A {partida["puntos_maximos"]} puntos \n Punto usuario: {partida["puntos_usuario"]}\n fecha:{now()}")
            

def guardar_archivo(nombre_archivo, datos):
    try:
        with open(nombre_archivo,"w") as archivo:
            json.dump(datos, archivo)
    except:
        print("Error al guardar")

def abrir_archivo(nombre_archivo):
    datos = None
    try:
        with open(nombre_archivo, "r") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return False
