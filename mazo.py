from random import choice

# Una matriz con todas las cartas del Truco
mazo_truco = [
    # 0 - nombre, 1 - palo, 2 - numero, 3 - poder
    ["Ancho de Espada", "espada", 1, 14],  # 0
    ["Dos de Espada", "espada", 2, 9],  # 1
    ["Tres de Espada", "espada", 3, 10],  # 2
    ["Cuatro de Espada", "espada", 4, 1],  # 3
    ["Cinco de Espada", "espada", 5, 2],  # 4
    ["Seis de Espada", "espada", 6, 3],  # 5
    ["Siete de Espada", "espada", 7, 12],  # 6
    ["Diez de Espada", "espada", 10, 5],  # 7
    ["Once de Espada", "espada", 11, 6],  # 8
    ["Doce de Espada", "espada", 12, 7],  # 9
    ["Ancho de Basto", "basto", 1, 13],  # 10
    ["Dos de Basto", "basto", 2, 9],  # 11
    ["Tres de Basto", "basto", 3, 10],  # 12
    ["Cuatro de Basto", "basto", 4, 1],  # 13
    ["Cinco de Basto", "basto", 5, 2],  # 14
    ["Seis de Basto", "basto", 6, 3],  # 15
    ["Siete de Basto", "basto", 7, 4],  # 16
    ["Diez de Basto", "basto", 10, 5],  # 17
    ["Once de Basto", "basto", 11, 6],  # 18
    ["Doce de Basto", "basto", 12, 7],  # 19
    ["Uno de Oro", "oro", 1, 8],  # 20
    ["Dos de Oro", "oro", 2, 9],  # 21
    ["Tres de Oro", "oro", 3, 10],  # 22
    ["Cuatro de Oro", "oro", 4, 1],  # 23
    ["Cinco de Oro", "oro", 5, 2],  # 24
    ["Seis de Oro", "oro", 6, 3],  # 25
    ["Siete de Oro", "oro", 7, 11],  # 26
    ["Diez de Oro", "oro", 10, 5],  # 27
    ["Once de Oro", "oro", 11, 6],  # 28
    ["Doce de Oro", "oro", 12, 7],  # 29
    ["Uno de Copa", "copa", 1, 8],  # 30
    ["Dos de Copa", "copa", 2, 9],  # 31
    ["Tres de Copa", "copa", 3, 10],  # 32
    ["Cuatro de Copa", "copa", 4, 1],  # 33
    ["Cinco de Copa", "copa", 5, 2],  # 34
    ["Seis de Copa", "copa", 6, 3],  # 35
    ["Siete de Copa", "copa", 7, 4],  # 36
    ["Diez de Copa", "copa", 10, 5],  # 37
    ["Once de Copa", "copa", 11, 6],  # 38
    ["Doce de Copa", "copa", 12, 7]  # 39
]


# Reparte las cartas a cada jugador
def repartir_cartas(mazo) -> tuple[list, list]:
    """
    Reparte 3 cartas a cada jugador y las ordena por poder de menor a mayor. Devuelve una tupla con las manos de ambos jugadores.

    :param mazo: El mazo con las cartas a utilizar.
    :return (mano_usuario, mano_computadora)
    """
    copia_mazo = mazo.copy()
    cartas_usuario = []
    cartas_computadora = []

    for i in range(3):
        carta = choice(copia_mazo)
        cartas_usuario.append(carta)
        copia_mazo.remove(carta)
        carta = choice(copia_mazo)
        cartas_computadora.append(carta)
        copia_mazo.remove(carta)

    return ordenar_mano_por_poder(cartas_usuario), ordenar_mano_por_poder(cartas_computadora)


# Determina que carta tiene mayor poder para poder ordenar la mano posteriormente
def determinar_carta_mayor(carta_1, carta_2):
    """
    Determina cuál de las dos cartas es mayor. Si son iguales, devuelve "empate".
    :param carta_1:
    :param carta_2:
    :return:
    """
    if obtener_poder(carta_1) > obtener_poder(carta_2):
        return carta_1
    elif obtener_poder(carta_2) > obtener_poder(carta_1):
        return carta_2
    else:
        return "empate"


# Obtiene el palo de la carta
def obtener_palo(carta):
    """
    Devuelve el palo de una carta.
    :param carta:
    :return: Str
    """
    return carta[1]


# Obtiene el poder de la carta
def obtener_poder(carta):
    """
    Devuelve el poder de una carta.
    :param carta:
    :return: int
    """
    return carta[3]


# Obtiene el número de la carta
def obtener_numero(carta):
    """
    Devuelve el número de una carta.
    :param carta:
    :return: int
    """
    return carta[2]


# Ordena la mano del jugador basándonos en el poder
def ordenar_mano_por_poder(mano):
    """
    Ordena una mano de cartas de menor a mayor poder.
    :param mano:
    :return:
    """
    for i in range(len(mano)):
        for j in range(len(mano) - 1):
            if obtener_poder(mano[j]) > obtener_poder(mano[j + 1]):
                mano[j], mano[j + 1] = mano[j + 1], mano[j]
    return mano
