from usuario import pedir_accion_usuario, mostrar_mano_usuario
from computadora import actuar_computadora
from mazo import repartir_cartas, mazo_truco

from utilidades import dev_print
from variables import get_user_points, get_max_points, get_computer_points, get_current_game, \
    get_previous_round, add_action, init_hand, get_current_hand, COMPUTADORA, USUARIO


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
    print("\n\n")
    print(f"Iniciando una nueva mano".center(60, "-"))
    print("\n\n")

    partida = get_current_game()

    # Se reparten las cartas a cada jugadora
    cartas_usuario, cartas_computadora = repartir_cartas(mazo_truco)

    # actualizamos que jugador empieza la mano
    if partida["manos_jugadas"] != 0:
        partida['siguiente_en_empezar'] = USUARIO if partida['siguiente_en_empezar'] == COMPUTADORA \
            else COMPUTADORA

    # Se inicializa la mano actual, con las cartas de cada jugador
    mano_actual = init_hand(cartas_usuario, cartas_computadora)

    mostrar_mano_usuario()

    # Se incrementa la cantidad de manos jugadas
    partida['manos_jugadas'] += 1

    continuar = True
    numero_de_ronda = 1
    # Generalmente, las manos del truco constan de 3 rondas, pero hay situaciones en las cuales se terminan antes
    # por eso tenemos un while con una condición de corte en 4 rondas y una bandera: continuar.
    # Esta última puede ser modificada dentro de la ronda para darle un final temprano.
    while continuar and numero_de_ronda < 4:
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

        # Guardamos en una variable de utilidad la ronda anterior para acceder más fácilmente a ella.
        # Si es la primera ronda, la ronda anterior es un diccionario vació.
        ronda_anterior = get_previous_round()

        if ronda_anterior.get('ganador') == COMPUTADORA:
            # Si tiene que empezar la computadora, agregamos la acción de actuar_computadora a la lista de acciones.
            add_action(actuar_computadora)

        if ronda_anterior.get('ganador') == USUARIO:
            # Si tiene que empezar el usuario, agregamos la acción de pedir_accion_usuario a la lista de acciones.
            add_action(pedir_accion_usuario)

        if ronda_anterior == {} or ronda_anterior.get('ganador') == 'empate':
            if partida['siguiente_en_empezar'] == USUARIO:
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

        numero_de_ronda += 1

    # Determinamos quien gano la ronda actual
    ganador_mano = determinar_ganador_de_la_mano()

    # Determinamos cuantos puntos se lleva el ganador de la mano
    puntos_a_sumar = determinar_puntos_ganador()

    # Sumamos los puntos al ganador de la mano
    partida['puntos'][ganador_mano] += puntos_a_sumar

    print(f"Gana {ganador_mano} sumando {puntos_a_sumar} puntos")

    imprimir_puntos()

    return {
        "accion": "none"
    }


def imprimir_puntos():
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
    print(f"|TU: {"  *" * puntos_usuario} ", end='')
    print("|".rjust(91 - puntos_usuario * 3))
    print(f"|PC: {"  *" * puntos_computadora} ", end='')
    print("|".rjust(91 - puntos_computadora * 3))
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

    # Si se cantó truco, y fue rechazado, automáticamente gana el que lo canto
    if mano_actual['truco'].get('rechazado_por') is not None:
        return mano_actual['truco']['cantado_por']

    ronda_1 = mano_actual['rondas'][0]
    ronda_2 = mano_actual['rondas'][1]
    ronda_3 = mano_actual['rondas'][2]

    rondas_ganadas = {
        USUARIO: 0,
        COMPUTADORA: 0,
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

    return USUARIO if rondas_ganadas[USUARIO] > rondas_ganadas[COMPUTADORA] else COMPUTADORA
