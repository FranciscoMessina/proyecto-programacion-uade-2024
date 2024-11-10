from datetime import date

from archivos import abrir_archivo, guardar_archivo
from utilidades import Colores
from variables import get_computer_points, get_user_points, get_max_points, get_current_game


def guardar_historial():
    historial = abrir_archivo("historial.json")

    if not historial:
        historial = []

    fecha = date.today()

    historial.append({
        "puntos_computadora": get_computer_points(),
        "puntos_usuario": get_user_points(),
        "puntos_maximos": get_max_points(),
        "ganador": get_current_game()['ganador'],
        "fecha": str(fecha)

    })

    guardar_archivo("historial.json", historial)


def ver_historial():
    historial = abrir_archivo("historial.json")

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
            print(f"   Ganador: {partida['ganador'].upper()}")
            print(f"   Fecha (Año-Mes-Día): {partida['fecha']}\n")
            print("".center(50, '-'))
            print("")
