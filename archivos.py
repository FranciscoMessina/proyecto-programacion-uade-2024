from datetime import date
import json

from utilidades import Colores, colores_palos
from variables import get_computer_points, get_user_points, get_max_points, get_current_game
from datetime import date
from mano import jugar_mano


def guardar_archivo(nombre_archivo, datos):
    """
    Guarda los datos en un archivo json
    :param nombre_archivo:
    :param datos:
    :return:
    """
    try:
        with open(nombre_archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4)
    except Exception as a:
        print("Error al guardar", a)


def abrir_archivo(nombre_archivo):
    """
    Abre un archivo json y devuelve los datos, si el archivo no existe devuelve False.
    :param nombre_archivo:
    :return: datos o False
    """
    try:
        with open(nombre_archivo, "r") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return False


def borrar_archivo(nombre_archivo):
    """
    Borra un archivo
    :param nombre_archivo:
    :return:
    """
    try:
        import os
        os.remove(nombre_archivo)
    except Exception as a:
        print("Error al borrar", a)
