from acciones_usuario import pedir_accion_usuario
from computadora import actuar_computadora
from mazo import repartir_cartas, mazo_truco, determinar_carta_mayor
from ronda import determinar_ganador_ronda
from utilidades import formatear_carta
from guardado import guardar_partida

from variables import get_user_points, get_max_points, get_computer_points, get_current_round, get_current_game, \
    get_previous_round, add_action, init_hand, partida_actual, get_current_hand


def jugar_mano():
    """
    Juega una mano de truco, esta funcion es ejecutada las veces necesarias para llegar a los puntos maximos de la partida
    :param partida: estado actual de la partida
    :return:
    """
    # Antes de comenzar una nueva mano se verifica si alguno de los jugadores llego a los puntos maximos,
    # en ese caso se termina la partida
    max_points = get_max_points()

    if get_user_points() >= max_points:
        return {
            "accion": "terminar_partida",
            "ganador": "usuario"
        }

    elif get_computer_points() >= max_points:
        return {
            "accion": "terminar_partida",
            "ganador": "computadora"
        }

    # Aca empieza una nueva mano.
    print(f"Iniciando una nueva mano".center(60, "-"))

    partida = get_current_game()

    # Se reparten las cartas a cada jugadora
    cartas_usuario, cartas_computadora = repartir_cartas(mazo_truco)

    # Se incrementa la cantidad de manos jugadas
    partida['manos_jugadas'] += 1

    # se actualiza el estado de la partida, reiniciando la Mano Actual
    # variable de utilidad para acceder mas facilmente a la mano_actual
    mano_actual = init_hand(cartas_usuario, cartas_computadora)

    continuar = True
    numero_de_ronda = 1
    # Generalmente las manos del truco constan de 3 rondas, pero hay situaciones en las cuales se terminan antes
    # por eso tenemos un while con una condicion de corte en 4 rondas y una bandera: continuar.
    # Esta ultima puede ser modificada dentro de la ronda para darle un final temprano.
    while continuar and numero_de_ronda < 4:
        # Este es el inicio de una nueva ronda en la mano actual.
        # Agregamos a la lista de rondas de la mano una nueva ronda.
        mano_actual['rondas'].append({
            "ganador": None,
        })

        mano_actual['acciones'] = []


        # Guardamos en una variable de utilidad la ronda anterior para acceder más fácilmente a ella.
        # Si es la primera ronda, la ronda anterior es un diccionario vació.
        ronda_anterior = get_previous_round()

        # print('INICIO')
        # print(ronda_actual)
        # print(ronda_anterior)

        if ronda_anterior.get('ganador') == 'computadora':
            add_action(actuar_computadora)

        if ronda_anterior.get('ganador') == 'usuario':
            add_action(pedir_accion_usuario)

        if ronda_anterior == {} or ronda_anterior.get('ganador') == 'empate':
            if partida['siguiente_en_empezar'] == 'usuario':
                add_action(pedir_accion_usuario)

            if partida['siguiente_en_empezar'] == 'computadora':
                add_action(actuar_computadora)

        for idx, action in enumerate(mano_actual['acciones']):
            result = action()
            result()

        # print('final')
        # print(ronda_actual)
        # print(ronda_anterior)

        numero_de_ronda += 1

    # Determinamos quien gano la ronda actual
    ganador_mano = determinar_ganador_de_la_mano()

    # Determinamos cuantos puntos se lleva el ganador de la mano
    puntos_a_sumar = determinar_puntos(mano_actual, ganador_mano, partida)

    # Sumamos los puntos al ganador de la mano
    partida['puntos'][ganador_mano] += puntos_a_sumar

    print(f"Gana {ganador_mano} sumando {puntos_a_sumar} puntos")

    for round in mano_actual['rondas']:
        print(round)

    imprimir_puntos()

    return {
        "accion": "none"
    }


def imprimir_puntos():
    puntos_usuario = get_user_points()
    puntos_computadora = get_computer_points()
    # Printea un gráfico que muestra los puntos de cada jugador
    print("|", end="")
    print(" PUNTOS ".center(95, '='), end='|\n')
    print("|---  01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ", end='|\n')
    print(f"|TU: {"  *" * puntos_usuario} ", end='')
    print("|".rjust(89 - puntos_usuario * 2))
    print(f"|PC: {"  *" * puntos_computadora} ", end='')
    print("|".rjust(89 - puntos_computadora * 2))
    print("|", end="")
    print("".center(95, '='), end='|\n')


def determinar_puntos(mano, ganador, partida):
    """
    Calcula cuantos puntos hay que sumar al ganador de la mano
    :param mano: mano actual
    :return:
    """
    # Siempre se suma al menos 1 punto por ganar la mano
    puntos = 1

    if mano['truco']:
        # Si hubiese truco, se suman los puntos correspondientes al nivel del truco
        puntos += mano['truco']['nivel']

    if mano['envido'].get('rechazado_por') is not None and ganador != mano['envido'].get('rechazado_por'):
        puntos += mano['envido']['nivel'] + 1
    elif ganador == mano['envido'].get('rechazado_por'):
        partida['puntos'][mano['envido'].get('cantado_por')] += 1

    return puntos


def determinar_ganador_de_la_mano():
    """
    Determina quien gano la mano actual
    :param mano: mano actual
    :return:
    """
    mano_actual = get_current_hand()

    # Si se canto truco, y fue rechazado, automatica gana el que lo canto
    if mano_actual['truco'].get('rechazado_por') is not None:
        return mano_actual['truco']['cantado_por']

    ronda_1 = mano_actual['rondas'][0]
    ronda_2 = mano_actual['rondas'][1]
    ronda_3 = mano_actual['rondas'][2]

    rondas_ganadas = {
        "usuario": 0,
        "computadora": 0,
        "empate": 0
    }

    for ronda in mano_actual['rondas']:
        # Sumamos cuantas rondas gano cada jugador
        rondas_ganadas[ronda['ganador']] += 1

    # Empata la primera, gana el siguiente ganador.
    if ronda_1['ganador'] == 'empate':
        return ronda_2['ganador'] if ronda_2['ganador'] != 'empate' else ronda_3['ganador']

    # Si se empata cualquier ronda menos la primera, gana el que gano la primera.
    if rondas_ganadas['empate'] > 0 and ronda_1['ganador'] != 'empate':
        return ronda_1['ganador']

    return "usuario" if rondas_ganadas['usuario'] > rondas_ganadas['computadora'] else 'computadora'
