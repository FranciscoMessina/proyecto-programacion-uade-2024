from random import choice

from mano import jugar_mano
from utilidades import pedir_eleccion


def nueva_partida():
    puntos_maximos = preguntar_puntos_partida()

    print(f"La partida sera a {puntos_maximos} puntos")

    partida = {
        "puntos_maximos": puntos_maximos,
        "puntos_usuario": 0,
        "puntos_computadora": 0,
        "manos_jugadas": 0,
        "mano_actual": {
            "rondas": [{}]
        },
        "siguiente_en_empezar": choice(["usuario"]),
    }

    continuar = True

    ganador = None

    def terminar_partida(_ganador):
        global ganador, continuar
        ganador = _ganador
        continuar = False

    while continuar:
        jugar_mano(partida, terminar_partida)

    print(f"El ganador de la partida es {ganador}")


def continuar_partida():
    pass


# puntos del partido
def preguntar_puntos_partida():
    print("A cuantos puntos queres jugar? ")

    respuesta = pedir_eleccion([
        ['A 15 puntos', 15],
        ['A 30 puntos', 30]
    ])

    return respuesta
