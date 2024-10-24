from random import choice

from envido import calcular_envido
from mazo import obtener_poder
from utilidades import noop, dev_print
from variables import get_computer_cards, get_current_round, get_current_hand, COMPUTADORA, envido_needs_answer, \
    truco_needs_answer, is_first_round


def actuar_computadora():
    """
    Determina como acciona la computadora en su turno.

    :return:
    """

    dev_print('Inicio Actuar computadora')

    mano_actual = get_current_hand()
    cartas = get_computer_cards()

    if envido_needs_answer():
        dev_print('AC- Responder a envido')
        return responder_a_envido()

    if truco_needs_answer():
        dev_print('AC- Responder a truco')
        return responder_a_truco()

    if is_first_round() and mano_actual['envido'].get('cantado_por') is None:
        dev_print('AC- Cantar envido')
        envido_puntos = calcular_envido(cartas)
        if envido_puntos >= 20:
            # CANTAR ENVIDO
            from acciones import cantar_envido
            return cantar_envido(COMPUTADORA)
        dev_print('AC- No canta envido por puntos insuficientes')

    c_truco = choice([True, False])
    if c_truco and mano_actual['truco'].get('nivel') == 0:
        dev_print('AC- Cantar truco')
        from acciones import cantar_truco
        return cantar_truco(COMPUTADORA)
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
    Determina con que carta responder a una carta jugada por el usuario la computadora

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

    # Si no tiene cartas que le ganen juega la carta mas baja que tenga ( su mano esta ordenada de menor a mayor poder)
    return jugar_carta(cartas_computadora[0], COMPUTADORA)


def responder_a_envido():
    """
    Determina como responde la computadora a un envido cantado por el usuario

    :return:
    """

    mano_actual = get_current_hand()

    if mano_actual['envido'].get('nivel') == 1:
        # Si se canto envido, la computadora decide si aceptar o no
        aceptar = choice([True, False])
        if aceptar:
            from acciones import aceptar_envido
            return aceptar_envido(COMPUTADORA)
        else:
            from acciones import rechazar_envido
            return rechazar_envido(COMPUTADORA)

    return noop


def responder_a_truco():
    """
    Determina como responde la computadora a un truco cantado por el usuario

    :return:
    """

    mano_actual = get_current_hand()

    if mano_actual['truco'].get('nivel') == 1:
        # Si se canto retruco, la computadora decide si aceptar o no
        aceptar = choice([True, False])
        if aceptar:
            from acciones import aceptar_truco
            return aceptar_truco(COMPUTADORA)
        else:
            from acciones import rechazar_truco
            return rechazar_truco(COMPUTADORA)

    return noop
