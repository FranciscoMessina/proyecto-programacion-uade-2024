from datetime import date
import json
import time
from variables import get_computer_points,get_user_points,get_max_points
from datetime import date
from datetime import datetime


#Fecha actual



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

    fecha=datetime.now()

    if historial == False:
        print("no tenes historial aun")

    else:
        for index, partida in enumerate(historial):
            print(f"La partida fue a {partida["puntos_maximos"]} puntos \n Puntos del usuario: {partida["puntos_usuario"]}\n Puntos de la computadora: {partida["puntos_computadora"]} \n fecha:{fecha.day}/{fecha.month}/{fecha.year}\n hora:{fecha.hour}:{fecha.minute} ")
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
