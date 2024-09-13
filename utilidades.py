from mazo import mazo_truco


def pedir_eleccion(opciones):
    """

    :param opciones:
    :return: eleccion del usuario
    """
    
    for i in range(len(opciones)):
        texto, _ = opciones[i]

        print(f"{i + 1}) {texto} ")

    ingresado = input('\n').strip()

    if ingresado == "":
        print(f"{Colors.RED}{Colors.BOLD}Por favor ingrese un numero {Colors.RESET}")
        pedir_eleccion(opciones)
        return

    eleccion = int(ingresado)

    opciones_disponibles = max(1, len(opciones))

    if eleccion < 1 or eleccion > opciones_disponibles:
        print(f"{Colors.RED}{Colors.BOLD}Eleccion invalida. {Colors.RESET}")
        pedir_eleccion(opciones)
        return
    else:
        return opciones[eleccion - 1][1]


class Colors:
    GREEN = '\033[92m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    RED = '\033[31m'


colores_palos = {
    'espada': Colors.BLUE,
    'basto': Colors.GREEN,
    'oro': Colors.YELLOW,
    'copa': Colors.RED
}


def formatear_carta(carta):
    return f"{colores_palos[carta[1]]}{Colors.BOLD}{carta[0]}{Colors.RESET}"
