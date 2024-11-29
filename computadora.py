import random
from random import choice

from envido import calcular_envido
from mazo import obtener_poder
from utilidades import noop, dev_print
from variables import get_computer_cards, get_current_round, get_current_hand, COMPUTADORA, USUARIO, \
    envido_needs_answer, truco_needs_answer, is_first_round, envido_rechazado_por, envido_cantado_por


def actuar_computadora():
    """
    Determina como acciona la computadora en su turno.

    :return:
    """
    from acciones import cantar_envido

    dev_print('Inicio Actuar computadora')

    mano_actual = get_current_hand()
    cartas = get_computer_cards()

    if envido_needs_answer():
        dev_print('AC- Responder a envido')
        return responder_a_envido()

    if truco_needs_answer():
        dev_print('AC- Responder a truco')
        return responder_a_truco()

    if is_first_round() and envido_rechazado_por() is None and envido_cantado_por() is None:
        dev_print('AC- Cantar envido')
        envido_puntos = calcular_envido(cartas)
        if envido_puntos >= 20:
            # CANTAR ENVIDO
            elegir = choice([1, 2, 3])
            if elegir == 1:

                return cantar_envido(COMPUTADORA, 'envido')
            elif elegir == 2:

                return cantar_envido(COMPUTADORA, 'real_envido')
            elif elegir == 3:

                return cantar_envido(COMPUTADORA, 'falta_envido')
        dev_print('AC- No canta envido por puntos insuficientes')

    c_truco = choice([True, False])
    if c_truco and mano_actual['truco'].get('nivel') == 0:
        dev_print('AC- Cantar truco')
        from acciones import cantar_truco
        return cantar_truco(COMPUTADORA, 1)
    elif c_truco and mano_actual['truco'].get('nivel') == 1 and mano_actual['truco'].get('cantado_por') == USUARIO:
        dev_print('AC- Cantar truco')
        from acciones import cantar_truco
        return cantar_truco(COMPUTADORA, 2)
    elif c_truco and mano_actual['truco'].get('nivel') == 2 and mano_actual['truco'].get('cantado_por') == USUARIO:
        dev_print('AC- Cantar truco')
        from acciones import cantar_truco
        return cantar_truco(COMPUTADORA, 3)
    else:
        if get_current_round().get('carta_usuario') is not None:
            dev_print('AC- Responder a carta')
            return responder_a_carta()

        dev_print('AC- Jugar carta')

        carta_random = choice(cartas)

        from acciones import jugar_carta
        return jugar_carta(carta_random, COMPUTADORA)


def responder_a_carta():
    """
    Determina con qué carta responder a una carta jugada por el usuario la computadora

    :return:
    """
    from acciones import jugar_carta

    carta_usuario = get_current_round()['carta_usuario']
    cartas_computadora = get_computer_cards()

    # Filtramos las cartas de la computadora para dejar solo las que le ganan o empatan a la carta jugada por el usuario
    cartas_mas_fuertes = list(
        filter(lambda carta: obtener_poder(carta_usuario) <= obtener_poder(carta), cartas_computadora))

    if len(cartas_mas_fuertes) > 0:
        # Si tiene cartas que le ganan o empata, juega la de menor valor disponible
        return jugar_carta(cartas_mas_fuertes[0], COMPUTADORA)

    # TODO: falta manejar caso de carta empardadora

    # Si no tiene cartas que le ganen juega la carta más baja que tenga (su mano está ordenada de menor a mayor poder)
    return jugar_carta(cartas_computadora[0], COMPUTADORA)


def responder_a_envido():
    from acciones import aceptar_envido, rechazar_envido, cantar_envido
    """
    Determina como responde la computadora a un envido cantado por el usuario

    :return:
    """

    cantados = get_current_hand()['envido']['cantados']

    # mano_actual = get_current_hand()
    if 'falta_envido' in cantados:
        elegir = choice([1, 2])
        if elegir == 1:
            return aceptar_envido(COMPUTADORA)
        elif elegir == 2:

            return rechazar_envido(COMPUTADORA)

    elif 'real_envido' in cantados:
        elegir = choice([1, 2, 3])
        if elegir == 1:

            return cantar_envido(COMPUTADORA, 'falta_envido')
        elif elegir == 2:

            return aceptar_envido(COMPUTADORA)
        elif elegir == 3:

            return rechazar_envido(COMPUTADORA)

    elif 'envido_2' in cantados:
        # Si se canto envido envido, la computadora decide si aceptar o no
        elegir = choice([1, 2, 3])
        if elegir == 1:

            return cantar_envido(COMPUTADORA, 'real_envido')
        elif elegir == 2:

            return aceptar_envido(COMPUTADORA)
        elif elegir == 3:

            return rechazar_envido(COMPUTADORA)

    elif 'envido' in cantados:
        # Si se canto envido, la computadora decide si aceptar o no
        elegir = choice([1, 2, 3, 4, 5])
        if elegir == 1:

            return cantar_envido(COMPUTADORA, 'falta_envido')
        elif elegir == 2:

            return cantar_envido(COMPUTADORA, 'real_envido')
        elif elegir == 3:

            return cantar_envido(COMPUTADORA, 'envido_2')
        elif elegir == 4:

            return aceptar_envido(COMPUTADORA)
        elif elegir == 5:
            return rechazar_envido(COMPUTADORA)

    return noop


def responder_a_truco():
    """
    Determina como responde la computadora a un truco cantado por el usuario

    :return: Function
    """
    from acciones import aceptar_truco, rechazar_truco
    from acciones import cantar_truco

    mano_actual = get_current_hand()

    if mano_actual['truco'].get('nivel') == 1:
        # Si se canto truco
        aceptar = choice([True, False])
        if aceptar:
            step_up = choice([True, False])
            if step_up:
                return cantar_truco(COMPUTADORA, 2)
            else:
                return aceptar_truco(COMPUTADORA)
        else:
            return rechazar_truco(COMPUTADORA)
    elif mano_actual['truco'].get('nivel') == 2:
        # Si se canto retruco
        aceptar = choice([True])  # True
        if aceptar:
            step_up = choice([True, False])
            if step_up:
                return cantar_truco(COMPUTADORA, 3)
            else:
                return aceptar_truco(COMPUTADORA)
        else:
            return rechazar_truco(COMPUTADORA)
    elif mano_actual['truco'].get('nivel') == 3:
        # Si se canto vale cuatro
        aceptar = choice([True, False])
        if aceptar:
            return aceptar_truco(COMPUTADORA)
        else:
            return rechazar_truco(COMPUTADORA)

    return rechazar_truco(COMPUTADORA)
