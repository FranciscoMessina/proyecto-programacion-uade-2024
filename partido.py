from random import choice

from mano import jugar_mano
from utilidades import pedir_eleccion

def nueva_partida():
    puntos_maximos = preguntar_puntos_partida()

    print("INICIANDO NUEVA PARTIDA")
    print(f"La partida sera a {puntos_maximos} puntos")

    partida = {
        "puntos_maximos": puntos_maximos,
        "puntos": {
            "usuario": 0,
            "computadora": 0
        },
        "manos_jugadas": 0,
        "siguiente_en_empezar": choice(["usuario"]),
    }

    continuar = True

    ganador = None

    while continuar:
        resultado = jugar_mano(partida)

        if resultado['accion'] == 'terminar_partida':
            continuar = False
            ganador = resultado['ganador']

    print(f"El ganador de la partida es {ganador}")

def continuar_partida():
    pass


# puntos del partido
def preguntar_puntos_partida():
    print("A cuantos puntos queres jugar? ")

    respuesta = pedir_eleccion([
        ["DEMO ONLY 3 puntos", 3],
        ['A 15 puntos', 15],
        ['A 30 puntos', 30]
    ])

    return respuesta
