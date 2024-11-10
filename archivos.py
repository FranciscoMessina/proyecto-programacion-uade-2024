from datetime import date
import json

from utilidades import Colores, colores_palos
from variables import get_computer_points, get_user_points, get_max_points, get_current_game
from datetime import date
from mano import jugar_mano


def guardar_archivo(nombre_archivo, datos):
    try:
        with open(nombre_archivo, "w") as archivo:
            json.dump(datos, archivo)
    except Exception as a:
        print("Error al guardar", a)


def abrir_archivo(nombre_archivo):
    datos = None
    try:
        with open(nombre_archivo, "r") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return False
