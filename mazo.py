from random import choice

mazo_truco = [
    # 0 - nombre, 1 - palo, 2 - numero, 3 - poder
    ["Ancho de Espada", "espada", 1, 14],
    ["Dos de Espada", "espada", 2, 9],
    ["Tres de Espada", "espada", 3, 10],
    ["Cuatro de Espada", "espada", 4, 1],
    ["Cinco de Espada", "espada", 5, 2],
    ["Seis de Espada", "espada", 6, 3],
    ["Siete de Espada", "espada", 7, 12],
    ["Diez de Espada", "espada", 10, 5],
    ["Once de Espada", "espada", 11, 6],
    ["Doce de Espada", "espada", 12, 7],
    ["Ancho de Basto", "basto", 1, 13],
    ["Dos de Basto", "basto", 2, 9],
    ["Tres de Basto", "basto", 3, 10],
    ["Cuatro de Basto", "basto", 4, 1],
    ["Cinco de Basto", "basto", 5, 2],
    ["Seis de Basto", "basto", 6, 3],
    ["Siete de Basto", "basto", 7, 4],
    ["Diez de Basto", "basto", 10, 5],
    ["Once de Basto", "basto", 11, 6],
    ["Doce de Basto", "basto", 12, 7],
    ["Uno de Oro", "oro", 1, 8],
    ["Dos de Oro", "oro", 2, 9],
    ["Tres de Oro", "oro", 3, 10],
    ["Cuatro de Oro", "oro", 4, 1],
    ["Cinco de Oro", "oro", 5, 2],
    ["Seis de Oro", "oro", 6, 3],
    ["Siete de Oro", "oro", 7, 11],
    ["Diez de Oro", "oro", 10, 5],
    ["Once de Oro", "oro", 11, 6],
    ["Doce de Oro", "oro", 12, 7],
    ["Uno de Copa", "copa", 1, 8],
    ["Dos de Copa", "copa", 2, 9],
    ["Tres de Copa", "copa", 3, 10],
    ["Cuatro de Copa", "copa", 4, 1],
    ["Cinco de Copa", "copa", 5, 2],
    ["Seis de Copa", "copa", 6, 3],
    ["Siete de Copa", "copa", 7, 4],
    ["Diez de Copa", "copa", 10, 5],
    ["Once de Copa", "copa", 11, 6],
    ["Doce de Copa", "copa", 12, 7]
]


def repartir_cartas(mazo) -> tuple[list, list]:
    """
    Reparte 3 cartas a cada jugador y las ordena por poder de menor a mayor. Devuelve una tupla con las manos de ambos jugadores.

    :param mazo: el mazo con las cartas a utilizar
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


def determinar_carta_mayor(carta_1, carta_2):
    """
    Determina cual de las dos cartas es mayor. Si son iguales, devuelve "empate".
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


def obtener_palo(carta):
    """
    Devuelve el palo de una carta.
    :param carta:
    :return: str
    """
    return carta[1]


def obtener_poder(carta):
    """
    Devuelve el poder de una carta.
    :param carta:
    :return: int
    """
    return carta[3]


def obtener_numero(carta):
    """
    Devuelve el número de una carta.
    :param carta:
    :return: int
    """
    return carta[2]


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
