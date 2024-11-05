from mano import jugar_mano
from utilidades import pedir_eleccion
from variables import init_game, reset_game


def nueva_partida():
    """
     Crea una nueva partida, pide al usuario los inputs necesarios para la misma,
    y ejecuta las manos hasta que se llegue al puntaje máximo indicado por el usuario
    :return:
    """
    puntos_maximos = preguntar_puntos_partida()

    print("INICIANDO NUEVA PARTIDA")
    print(f"La partida sera a {puntos_maximos} puntos")

    # inicializamos la partida en un diccionario.
    init_game(puntos_maximos)

    continuar = True

    ganador = None

    while continuar:
        resultado = jugar_mano()

        if resultado['accion'] == 'terminar_partida':
            # Si se termina la partida, salimos del loop
            continuar = False
            # Asignamos al ganador
            ganador = resultado['ganador']

            # Reseteamos los datos de la partida para dejar
            # listo para iniciar una proxima partida.
            reset_game()

    print(f"El ganador de la partida es {ganador.upper()}")


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
