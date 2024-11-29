from datetime import date

from archivos import abrir_archivo, guardar_archivo
from utilidades import Colores, player_color
from variables import get_computer_points, get_user_points, get_max_points, get_current_game


def guardar_partida_en_historial():
    """
    Guarda la partida actual en el historial
    :return:
    """

    # Tratamos de abrir el archivo para ver si ya existen partidas
    historial = abrir_archivo("historial.json")

    if not historial:
        # En caso de que no existan partidas, lo inicializamos como una lista vacia
        historial = []

    fecha = date.today()

    # Agregamos a la lista los datos que queremos guardar de la partida actual.
    historial.append({
        "puntos_computadora": get_computer_points(),
        "puntos_usuario": get_user_points(),
        "puntos_maximos": get_max_points(),
        "ganador": get_current_game()['ganador'],
        "fecha": str(fecha)

    })

    # Guardamos la lista actualizada en el archivo
    guardar_archivo("historial.json", historial)


def ver_historial():
    """
    Muestra el historial de partidas guardadas
    :return:
    """

    # Abrimos el archivo de historial
    historial = abrir_archivo("historial.json")

    # Si no existe el archivo o tiene una lista vacia, mostramos un mensaje indicando que aun no se jugaron partidas.
    if historial == False or len(historial) == 0:
        print("\n\n\nAún no jugaste ninguna partida,")
        print("cuando lo hagas podras ver tu historial aqui.\n\n\n")
    else:
        print(f'{Colores.YELLOW}{Colores.BOLD}{Colores.UNDERLINE}Historial de partidas{Colores.RESET}: \n')
        for idx, partida in enumerate(historial):
            print(f"{idx + 1})", end='')
            print(f" La partida fue a {partida['puntos_maximos']} puntos")
            print(f"   Puntos del usuario: {partida['puntos_usuario']}")
            print(f"   Puntos de la computadora: {partida['puntos_computadora']}")
            print(f"   Ganador: {player_color[partida['ganador']]}{partida['ganador'].upper()}{Colores.RESET}")
            print(f"   Fecha (Año-Mes-Día): {partida['fecha']}\n")
            print("".center(50, '-'))
            print("")
