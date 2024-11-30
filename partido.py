from archivos import guardar_archivo, abrir_archivo, borrar_archivo
from historial import guardar_partida_en_historial
from mano import jugar_mano
from utilidades import pedir_eleccion, player_color, Colores, limpiar_terminal, spinner
from variables import init_game, reset_game, get_current_game, default_game_init


def nueva_partida():
    """
     Crea una nueva partida, pide al usuario los inputs necesarios para la misma,
    y ejecuta las manos hasta que se llegue al puntaje máximo indicado por el usuario
    :return:
    """
    puntos_maximos = preguntar_puntos_partida()

    print(" Iniciando una nueva partida ".center(60, '-'))
    print('\n')
    spinner(
        f"{Colores.BLINK}La partida sera a {Colores.UNDERLINE}{puntos_maximos}{Colores.RESET}{Colores.BLINK} puntos{Colores.RESET}".center(
            66, ' '), 16)

    # inicializamos la partida en un diccionario.
    partida = default_game_init()

    partida['puntos_maximos'] = puntos_maximos

    init_game(partida)

    jugar_partida()


def continuar_partida():
    """
    Continua una partida guardada.

    :return:
    """

    spinner('Recuperando partida guardada...  ', 12)

    partida_guardada = abrir_archivo("partida_guardada.json")

    if not partida_guardada:
        print(f"{Colores.RED}No se pudo recuperar la partida guardada.{Colores.RESET}")
        borrar_archivo("partida_guardada.json")
        return

    print(f"{Colores.GREEN}Partida recuperada con éxito.{Colores.RESET}")

    init_game(partida_guardada)

    jugar_partida()


def jugar_partida():
    limpiar_terminal()

    continuar = True

    def terminar_partida(ganador):
        nonlocal continuar
        continuar = False

        partida_actual = get_current_game()
        # Asignamos al ganador
        partida_actual['ganador'] = ganador
        guardar_partida_en_historial()

        print(f"El ganador de la partida es {player_color[ganador]}{ganador.upper()}{Colores.RESET}\n\n")
        # Reseteamos los datos de la partida para dejar
        # listo para iniciar una proxima partida.
        reset_game()
        borrar_partida_guardada()

    while continuar:
        try:
            jugar_mano(terminar_partida)
        except KeyboardInterrupt:
            print("Partida interrumpida por el usuario.\n")

            guardar_partida()

            continuar = False


def guardar_partida():
    """
    Guarda la partida actual en un archivo JSON. Para poder ser retomada.
    :return:
    """

    spinner("Guardando partida...", 12)

    datos_a_guardar = get_current_game()

    # eliminamos las acciones del array, porque no pueden ser convertidas a JSON.
    datos_a_guardar['mano_actual']['acciones'] = []

    # Eliminamos la última ronda, ya que no se terminó de jugar.

    ultima_ronda = datos_a_guardar['mano_actual']['rondas'].pop()

    # En este caso alguno de los jugadores ya tiraron cartas, pero como para retomar la partida eliminamos rondas
    # incompletas, tenemos que volver a agregar la carta a sus manos originales.
    if len(datos_a_guardar['mano_actual']['cartas_usuario']) < 3 - len(datos_a_guardar['mano_actual']['rondas']):
        datos_a_guardar['mano_actual']['cartas_usuario'].append(
            ultima_ronda['carta_usuario']
        )
    elif len(datos_a_guardar['mano_actual']['cartas_computadora']) < 3 - len(datos_a_guardar['mano_actual']['rondas']):
        datos_a_guardar['mano_actual']['cartas_computadora'].append(
            ultima_ronda['carta_computadora']
        )

    guardar_archivo("partida_guardada.json", datos_a_guardar)

    print(f"\r{Colores.GREEN}Partida guardada con éxito.{Colores.RESET}\n")

    return


def preguntar_puntos_partida():
    """
    Pregunta al usuario a cuantos puntos quiere jugar la partida.
    :return:
    """
    return pedir_eleccion([
        f'{Colores.UNDERLINE}A cuantos puntos querés jugar?{Colores.RESET}\n',
        ['A 15 puntos', 15],
        ['A 30 puntos', 30]
    ], True)


def hay_partida_guardada():
    """
    Verifica si hay una partida guardada.
    :return:
    """
    partida_guardada = abrir_archivo("partida_guardada.json")

    if partida_guardada:
        return True

    return False


def borrar_partida_guardada():
    """
    Borra la partida guardada.
    :return:
    """
    try:
        spinner("Borrando partida guardada...", 12)

        borrar_archivo("partida_guardada.json")

        print(f"\r{Colores.GREEN}Partida guardada borrada con éxito.{Colores.RESET}\n")

    except Exception as a:
        print(f"\r{Colores.RED}No se pudo borrar la partida guardada.{Colores.RESET}\n")

    return
