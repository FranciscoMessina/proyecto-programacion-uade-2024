import json


def hay_partida_guardada():
    try:
        with open('partida_guardada.json', 'r+') as archivo:
            if archivo:
                return True
    except FileNotFoundError:
        return False

def cargar_partida_guardada():
    with open('partida_guardada.json', 'r+') as archivo:
        if archivo:
            return json.load(archivo)

def guardar_partida(partida):
    try:
        with open('partida_guardada.json', 'w') as archivo:
            json.dump(partida, archivo)

            return True
    except FileNotFoundError:
        return False

# partido de historial
# {
# ganador: 'Computadora' o 'Jugador',
# puntos_jugador: int,
# puntos_computadora: int,
# fecha: str
# }
def buscar_historial():
    pass



def guardar_partida_en_historial(partido):
    pass

def mostrar_historial():
    pass


hay_partida_guardada()
