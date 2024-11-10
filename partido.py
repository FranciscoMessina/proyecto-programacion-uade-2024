from archivos import guardar_archivo
from historial import guardar_historial
from mano import jugar_mano
from utilidades import pedir_eleccion, player_color, Colores
from variables import init_game, reset_game, get_current_game, get_computer_points, get_user_points, get_max_points


def nueva_partida():
    """
     Crea una nueva partida, pide al usuario los inputs necesarios para la misma,
    y ejecuta las manos hasta que se llegue al puntaje máximo indicado por el usuario
    :return:
    """
    puntos_maximos = preguntar_puntos_partida()

    print('\n\n\n')
    print("INICIANDO NUEVA PARTIDA".center(60, '-'))
    print(f"\nLa partida sera a {puntos_maximos} puntos\n")

    # inicializamos la partida en un diccionario.
    init_game(puntos_maximos)

    continuar = True

    def terminar_partida(ganador):
        nonlocal continuar
        continuar = False

        partida_actual = get_current_game()
        # Asignamos al ganador
        partida_actual['ganador'] = ganador
        guardar_historial()

        print(f"El ganador de la partida es {player_color[ganador]}{ganador.upper()}{Colores.RESET}\n\n")
        # Reseteamos los datos de la partida para dejar
        # listo para iniciar una proxima partida.
        reset_game()

    while continuar:
        jugar_mano(terminar_partida)


def continuar_partida():
    pass


def preguntar_puntos_partida():
    """
    Pregunta al usuario a cuantos puntos quiere jugar la partida.
    :return:
    """
    print("A cuantos puntos querés jugar? ")

    return pedir_eleccion([
        ["DEMO ONLY 3 puntos", 3],
        ['A 15 puntos', 15],
        ['A 30 puntos', 30]
    ], True)


def guardar_partida():
    guardar_archivo("partida_guardada.json", {
        "puntos_computadora": get_computer_points(),
        "puntos_usuario": get_user_points(),
        "puntos_maximos": get_max_points(),
    })
