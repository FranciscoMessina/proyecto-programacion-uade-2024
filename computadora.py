from random import choice

from envido import calcular_envido
from mazo import obtener_poder
from ronda import determinar_ganador_ronda
from utilidades import formatear_carta, noop
from variables import get_computer_cards, get_current_round, add_action, get_current_game, is_last_action_in_round, \
    get_current_hand


def actuar_computadora():
    """
    Determina como acciona la computadora en su turno, cuando no tiene que responder al usuario.

    :param cartas: cartas que tiene la computadora
    :param partida: estado actual de la partida
    :param numero_ronda: numero de la ronda actual
    :return:
    """

    partida = get_current_game()
    cartas = get_computer_cards()

    carta_random = choice(cartas)
    return jugar_carta_(carta_random)

    if partida['mano_actual']['rondas'][0]['ganador'] is None and partida['mano_actual']['envido'].get(
            'cantado_por') is None:
        envido_puntos = calcular_envido(cartas)
        if envido_puntos >= 20:
            # CANTAR ENVIDO
            return noop

    cantar_truco = choice([True, False])
    if not cantar_truco:
        carta_random = choice(cartas)
        return jugar_carta_(carta_random)
    elif cantar_truco and partida['mano_actual']['truco'].get('nivel') is None:
        # CANTAR TRUCO
        return noop


def responder_a_carta():
    """
    Determina con que carta responder a una carta jugada por el usuario la computadora

    :return:
    """

    carta_usuario = get_current_round()['carta_usuario']
    cartas_computadora = get_computer_cards()

    # Filtramos las cartas de la computadora para dejar solo las que le ganan o empatan a la carta jugada por el usuario
    cartas_mas_fuertes = list(
        filter(lambda carta: obtener_poder(carta_usuario) <= obtener_poder(carta), cartas_computadora))

    if len(cartas_mas_fuertes) > 0:
        # Si tiene cartas que le gganan o empata, juega la de menor valor disponible
        return jugar_carta_(cartas_mas_fuertes[0])

    # TODO: falta manejar caso de carta empardadora

    # Si no tiene cartas que le ganen juega la carta mas baja que tenga ( su mano esta ordenada de menor a mayor poder)
    return jugar_carta_(cartas_computadora[0])


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
            return aceptar_envido()
        else:
            return rechazar_envido()

    return noop


def aceptar_envido():
    """
    Funcion que se llama cuando la computadora decide
    aceptar el envido cantado por el usuario


    :return:
    """

    def _aceptar_envido():
        mano_actual = get_current_hand()

        mano_actual['envido'].update({
            "activo": True,
        })
        print("La computadora QUIERE el envido.")

        if is_last_action_in_round():
            add_action(determinar_ganador_ronda)
        else:
            from acciones_usuario import pedir_accion_usuario
            add_action(pedir_accion_usuario)

        return noop

    return _aceptar_envido


def rechazar_envido():
    """
    Funcion que se llama cuando la computadora decide
    aceptar el envido cantado por el usuario


    :return:
    """

    def _rechazar_envido():
        mano_actual = get_current_hand()

        mano_actual['envido'].update({
            "activo": False,
            "rechazado_por": "computadora",
        })
        print("La computadora NO QUIERE el envido.")

        if is_last_action_in_round():
            add_action(determinar_ganador_ronda)
        else:
            from acciones_usuario import pedir_accion_usuario
            add_action(pedir_accion_usuario)

        return noop

    return _rechazar_envido


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
            return aceptar_truco()
        else:
            return rechazar_truco()

    return noop


def aceptar_truco():
    """
    Funcion que se llama cuando la computadora decide
    aceptar el truco cantado por el usuario

    :return:
    """

    def _aceptar_truco():
        mano_actual = get_current_hand()

        mano_actual['truco'].update({
            "activo": True,
        })
        print("La computadora QUIERE el truco.")

        if is_last_action_in_round():
            add_action(determinar_ganador_ronda)
        else:
            from acciones_usuario import pedir_accion_usuario
            add_action(pedir_accion_usuario)

        return noop

    return _aceptar_truco()


def rechazar_truco():
    """
    Funcion que se llama cuando la computadora decide
    aceptar el truco cantado por el usuario

    :return:
    """

    def _rechazar_truco():
        mano_actual = get_current_hand()

        mano_actual['truco'].update({
            "activo": False,
            "rechazado_por": "computadora",
        })

        print("La computadora NO QUIERE el truco, ganaste la mano.")

        return noop

    return _rechazar_truco()


def jugar_carta_(carta):
    """
    Crea la funcion que va a ser utilizada para jugar la carta del usuario

    :param carta: carta a jugar

    :return: Funcion para jugar la carta
    """

    def _jugar_carta():
        nonlocal carta

        cartas = get_computer_cards()
        cartas.remove(carta)

        ronda_actual = get_current_round()

        ronda_actual['carta_computadora'] = carta
        print(f"La computadora jugo el {formatear_carta(carta)}")

        if not is_last_action_in_round():
            from acciones_usuario import pedir_accion_usuario
            add_action(pedir_accion_usuario)
        else:
            add_action(determinar_ganador_ronda)

        return noop

    return _jugar_carta
