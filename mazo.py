from random import randint, choice

mazo_truco = [
    # nombre, palo, numero, poder
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


def repartir_cartas(mazo):
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

    return cartas_usuario, cartas_computadora
