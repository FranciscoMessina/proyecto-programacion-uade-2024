import os
from pydoc import plain

from mazo import obtener_palo, obtener_numero
from variables import USUARIO, COMPUTADORA


# Deja mas prolija la terminal para empezar a jugar
def limpiar_terminal():
    """
    Función de utilidad para limpiar la terminal.

    :return:
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def pedir_eleccion(opciones, limpiar_consola=False):
    """
    Función de utilidad para pedir input al usuario, recibe una lista con las opciones a mostrar y devuelve la elección del usuario.
    Cada elemento de la lista es otra lista con el siguiente formato: [texto, valor].
    Texto es lo que se muestra al usuario al momento de pedirle el input y valor es lo que se devuelve si el usuario elige esa opción.

    También se encarga de validar que la elección del usuario.

    :param opciones: Lista con las opciones a mostrar
    :param limpiar_consola: Booleano que indica si se debe limpiar la consola antes de mostrar las opciones
    :return: elección del usuario
    """

    for i in range(len(opciones)):
        # por cada una de las opciones recibidas, desempaquetamos el texto
        texto, _ = opciones[i]

        print(f"{i + 1}) {texto} ")

    ingresado = input('\n').strip()

    if limpiar_consola:
        limpiar_terminal()

    # Verificamos que el input sea un numero
    if ingresado == "" or not ingresado.isdigit():
        print(f"{Colores.RED}{Colores.BOLD}Por favor ingrese un numero. {Colores.RESET}\n")
        return pedir_eleccion(opciones)

    eleccion = int(ingresado)

    opciones_disponibles = max(1, len(opciones))

    # Si la elección está fuera de rango, la volvemos a pedir.
    if eleccion < 1 or eleccion > opciones_disponibles:
        print(f"{Colores.RED}{Colores.BOLD}Elección invalida. {Colores.RESET}\n")
        return pedir_eleccion(opciones)

    # Devolvemos el valor asignado a la elección
    return opciones[eleccion - 1][1]


# Sé que no se supone que usemos clases, pero es una forma más
# fácil de poder acceder a las propiedades sin cometer errores de tipeo
# asi por favor no nos saquen puntos por esto.
# Si no lo cambiamos a diccionario, solo avisar.
class Colores:
    # Colores para imprimir en consola.
    GREEN = '\033[92m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    RED = '\033[31m'
    UNDERLINE = '\033[4m'


colores_palos = {
    # Asignamos un color a cada palo
    'espada': Colores.BLUE,
    'basto': Colores.GREEN,
    'oro': Colores.YELLOW,
    'copa': Colores.RED
}

player_color = {
    USUARIO: Colores.GREEN,
    COMPUTADORA: Colores.RED
}


def formatear_carta(carta):
    """
    Función de utilidad para generar una string visualmente atractiva de una carta de truco.
    :param carta:
    :return: String estilada para ser impresa en consola
    """
    return f"{colores_palos[obtener_palo(carta)]}{Colores.BOLD}{carta[0]}{Colores.RESET}"


palo_ascii = {
    "espada": lambda num: f"""{colores_palos['espada']}
    +-----------+
    | {num}   .     |
    |    / \    |
    |    | |    |
    |    |.|    |
    |    |.|    |
    |    |:|    |
    |    |:|    |
    |  `--8--'  |
    |     8     |
    |     O     |     
    |         {num} |
    +-----------+
    {Colores.RESET}
    """,
    "basto": lambda num: f"""{colores_palos['basto']}
    """,
    "oro": lambda num: f"""{colores_palos['oro']}
    """,
    "copa": lambda num: f"""{colores_palos['copa']}
"""
}


def imprimir_carta_ascii(carta):
    """
    Imprime una carta en formato ASCII.
    :param carta:
    :return:
    """
    print(palo_ascii[obtener_palo(carta)](obtener_numero(carta)))


# Cambiar esto a True si queres ver los mensajes de debug
DEV = False  # True



def dev_print(*args, **kwargs):
    """
    Función de utilidad para imprimir en consola, pero solo si estamos en modo debug.
    :param args:
    :param kwargs:
    :return:
    """

    if DEV:
        print(f'{Colores.PURPLE}(DEV-ONLY)', *args, f'{Colores.RESET}', **kwargs)


def noop():
    dev_print("Noop fue llamado")
    return "Noop"
