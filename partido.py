
from random import choice

from mano import jugar_mano


def nueva_partida():
    puntos_maximos = preguntar_puntos_partida()

    print(f"La partida sera a {puntos_maximos} puntos")

    partida = {
        "puntos_maximos": puntos_maximos,
        "puntos_jugador": 0,
        "puntos_computadora": 0,
        "manos_jugadas": 0,
        "mano_actual": [],
        "siguiente_en_empezar": choice(["jugador"]),
    }

    continuar = True

    while continuar:
        jugar_mano(partida)

    pass


def continuar_partida():
    pass


# puntos del partido
def preguntar_puntos_partida():
    eleccion = int(input("A cuantos puntos queres jugar? \n 1) 30 Puntos \n 2) 15 Puntos \n"))

    return 15 if eleccion == 1 else 30


    
    
    
    

