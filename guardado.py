from datetime import date
import json
from variables import get_computer_points,get_user_points,get_max_points,get_current_game
from datetime import date
from mano import jugar_mano


def guardar_historial():

    historial = abrir_archivo("historial.json")

    if historial ==  False:
        historial = []

    fecha=date.today()

    resultado=jugar_mano()
    ganador=resultado['ganador']

    historial.append({
        "puntos_computadora":get_computer_points(),
        "puntos_usuario":get_user_points(),
        "puntos_maximos":get_max_points(),
        "ganador":str(ganador),
        "fecha": str(fecha)

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

  
    if historial == False or len(historial) == 0:
        print("no tenes historial aun")
    else:
        for idx, partida in enumerate(historial):
            print(f"""                
                      {idx+1}) historial:
                      La partida fue a {partida["puntos_maximos"]} puntos
                      Puntos del usuario: {partida["puntos_usuario"]}
                      Puntos de la computadora: {partida["puntos_computadora"]} 
                      ganador :{partida["ganador"]}
                      fecha: {partida["fecha"]} 
            """)
            


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
