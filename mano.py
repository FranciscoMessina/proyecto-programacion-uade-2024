from ronda import determinar_ganador_ronda
from usuario import pedir_accion_usuario, mostrar_mano_usuario
from computadora import actuar_computadora
from mazo import repartir_cartas, mazo_truco

from utilidades import dev_print, Colores, player_color, noop
from variables import get_user_points, get_max_points, get_computer_points, get_current_game, \
    get_previous_round, add_action, init_hand, get_current_hand, COMPUTADORA, USUARIO, reset_hand, get_current_round, \
    round_started_by, quien_es_mano


def jugar_mano(terminar_partida):
    """
    Juega una mano de truco, esta función es ejecutada las veces necesarias para llegar a los puntos máximos de la partida

    :return:
    """
    # Antes de comenzar una nueva mano se verifica si alguno de los jugadores llego a los puntos máximos,
    # en ese caso se termina la partida
    max_points = get_max_points()

    if get_user_points() >= max_points:
        return terminar_partida(USUARIO)

    elif get_computer_points() >= max_points:
        return terminar_partida(COMPUTADORA)

    # Aca empieza una nueva mano.
    print(f" Iniciando una nueva mano ".center(60, "-"))
    print("\n\n")

    partida = get_current_game()

    if partida['mano_actual'] == {}:
        # Se reparten las cartas a cada jugadora
        cartas_usuario, cartas_computadora = ([["Cuatro de Espada", "espada", 4, 1], ["Cinco de Espada", "espada", 5, 2], ["Seis de Espada", "espada", 6, 3]], [["Cuatro de Espada", "espada", 4, 1], ["Cinco de Espada", "espada", 5, 2], ["Seis de Espada", "espada", 6, 3]])     #repartir_cartas(mazo_truco)

        # actualizamos que jugador empieza la mano
        if partida["manos_jugadas"] != 0:
            partida['siguiente_en_empezar'] = USUARIO if partida['siguiente_en_empezar'] == COMPUTADORA \
                else COMPUTADORA

        # Se inicializa la mano actual, con las cartas de cada jugador
        mano_actual = init_hand(cartas_usuario, cartas_computadora)
    else:
        print('Retomando partida')
        mano_actual = partida['mano_actual']

    # Se incrementa la cantidad de manos jugadas
    partida['manos_jugadas'] += 1

    mostrar_mano_usuario()

    continuar = True
    numero_de_ronda = len(mano_actual['rondas'])
    # Generalmente, las manos del truco constan de 3 rondas, pero hay situaciones en las cuales se terminan antes
    # por eso tenemos un while con una condición de corte después de la 3 ronda y una bandera: continuar.
    # Esta última puede ser modificada dentro de la ronda para darle un final temprano.
    while continuar and numero_de_ronda < 3:
        numero_de_ronda += 1

        # Este es el inicio de una nueva ronda en la mano actual.
        # Agregamos a la lista de rondas de la mano una nueva ronda.

        mano_actual['rondas'].append({
            "ganador": None,
        })

        # Aca reiniciamos las acciones de la mano, para iniciar la siguiente ronda.
        # ¿Qué son las acciones? Son funciones que agregamos a esta lista y que se ejecutan en orden.
        # Cada una de ellas es ejecutada y debe devolver otra función que se ejecutara cuando termine.
        # (noop) puede devolverse para no hacer nada.
        # Cuando no quedan más funciones en la lista, se termina la ronda.
        mano_actual['acciones'] = []

        print(f" Ronda {numero_de_ronda} ".center(60, "-"))
        # Guardamos en una variable de utilidad la ronda anterior para acceder más fácilmente a ella.
        # Si es la primera ronda, la ronda anterior es un diccionario vació.
        empieza = round_started_by()

        if empieza == USUARIO:
            add_action(pedir_accion_usuario)
        else:
            add_action(actuar_computadora)

        # Acá ejecutamos las acciones, es simplemente una iteración por la lista de acciones.
        # Al ejecutar cada acción, llamamos a la función que devuelve.
        # Muchas de las acciones agregan otra función a la lista durante su ejecución.
        # Una vez que no quedan más acciones en la lista se termina la ronda.
        for idx, action in enumerate(mano_actual['acciones']):
            result = action()
            result()

        determinar_ganador_ronda()

        ronda_actual = get_current_round()
        ronda_anterior = get_previous_round()

        # Si el truco fue rechazado, termina la mano
        if mano_actual['truco'].get('rechazado_por') is not None:
            continuar = False
        if numero_de_ronda >= 2:
            # Si se jugaron dos rondas, y la primera fue empatada y la segunda no, termina la mano.
            if ronda_anterior.get('ganador') == 'empate' and ronda_actual.get('ganador') != 'empate':
                continuar = False

            # Si se jugaron dos rondas, y la primera no fue empatada y la segunda sí, termina la mano.
            if ronda_anterior.get('ganador') != "empate" and ronda_actual.get('ganador') == "empate":
                continuar = False

            # Si un jugador gana dos rondas seguidas, termina la mano.
            if ronda_actual.get('ganador') == ronda_anterior.get('ganador') and ronda_actual.get('ganador') != "empate" or ronda_actual.get('ganador') != 'empate':
                continuar = False

    # Determinamos quien gano la ronda actual
    ganador_mano = determinar_ganador_de_la_mano()

    # Determinamos cuantos puntos se lleva el ganador de la mano
    puntos_a_sumar = determinar_puntos_ganador()

    # Sumamos los puntos al ganador de la mano
    print(ganador_mano)
    partida['puntos'][ganador_mano] += puntos_a_sumar

    print(
        f"\n\nGana {player_color[ganador_mano]}{ganador_mano.upper()}{Colores.RESET} sumando {puntos_a_sumar} puntos!")

    imprimir_puntos(max_points)

    reset_hand()

    return noop


def imprimir_puntos(max):
    """
    Imprime en consola los puntos de cada jugador.
    :return:
    """
    puntos_usuario = get_user_points()
    puntos_computadora = get_computer_points()
    # Imprime un gráfico que muestra los puntos de cada jugador
    print("\n|", end="")
    print(" PUNTOS ".center(95, '='), end='|\n')
    print("|---  01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ", end='|\n')
    if puntos_usuario <= max:
        print(f"|{Colores.BACKGROUND_GREEN}TU: {"  *" * puntos_usuario} ", end='')
        print(f'{Colores.BACKGROUND_DEFAULT}', end='')
        print("|".rjust(91 - puntos_usuario * 3))

    else:
        print(f"|{Colores.BACKGROUND_GREEN}TU: {"  *" * max} ", end='')
        print(f'{Colores.BACKGROUND_DEFAULT}', end='')
        print("|".rjust(91 - max * 3))
    if puntos_computadora <= max:
        print(f"|{Colores.BACKGROUND_RED}PC: {"  *" * puntos_computadora} ", end='')
        print(f'{Colores.BACKGROUND_DEFAULT}', end='')
        print("|".rjust(91 - puntos_computadora * 3))
    else:
        print(f"|{Colores.BACKGROUND_RED}PC: {"  *" * max} ", end='')
        print(f'{Colores.BACKGROUND_DEFAULT}', end='')
        print("|".rjust(91 - max * 3))

    print("|", end="")
    print("".center(95, '='), end='|\n')
    print('\n')


def determinar_puntos_ganador():
    """
    Calcula cuantos puntos hay que sumar al ganador de la mano.
    :return: Int: puntos a sumar al ganador
    """
    truco = get_current_hand()['truco']

    # Siempre se suma al menos 1 punto por ganar la mano
    puntos = 1

    if truco.get('rechazado_por'):
        puntos += truco['nivel'] - 1
        dev_print("truco nivel:", truco['nivel'])

    else:
        # Si hubiese truco, se suman los puntos correspondientes al nivel del truco
        puntos += truco['nivel']
        dev_print("truco nivel:", truco['nivel'])

    return puntos


def determinar_ganador_de_la_mano():
    """
    Función para determinar quien gano la mano basándose en las rondas jugadas.

    :return: Str: "usuario" | "computadora"
    """
    mano_actual = get_current_hand()

    rondas = mano_actual['rondas']

    # Si se cantó truco, y fue rechazado, automáticamente gana el que lo canto
    if mano_actual['truco'].get('rechazado_por') is not None:
        return mano_actual['truco']['cantado_por']

    if len(rondas) <= 2:
        # Si solo se jugaron dos rondas,
        # Si se empata la segunda, gana el ganador de la primera
        if rondas[-1]['ganador'] == 'empate':
            return rondas[-2]['ganador']
        # Si se empató la primera, gana el ganador de la segunda.
        return rondas[-1]['ganador']

    ronda_1 = rondas[0]
    ronda_2 = rondas[1]
    ronda_3 = rondas[2]

    rondas_ganadas = {
        USUARIO: 0,
        COMPUTADORA: 0,
        "empate": 0
    }

    for ronda in rondas:
        # Sumamos cuantas rondas gano cada jugador
        rondas_ganadas[ronda['ganador']] += 1

    if rondas_ganadas['empate'] == 3:
        return quien_es_mano()

    # Empata la primera, gana el siguiente ganador.
    if ronda_1['ganador'] == 'empate':
        return ronda_2['ganador'] if ronda_2['ganador'] != 'empate' else ronda_3['ganador']

    # Si se empata cualquier ronda menos la primera, gana el que gano la primera.
    if rondas_ganadas['empate'] > 0 and ronda_1['ganador'] != 'empate':
        return ronda_1['ganador']
    

    return USUARIO if rondas_ganadas[USUARIO] > rondas_ganadas[COMPUTADORA] else COMPUTADORA
