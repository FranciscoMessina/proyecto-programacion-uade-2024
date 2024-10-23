from acciones_usuario import pedir_accion_usuario
from computadora import actuar_computadora
from ronda import determinar_ganador_ronda
from utilidades import formatear_carta, noop
from variables import get_current_hand, get_current_round, is_last_action_in_round, add_action, USUARIO, COMPUTADORA


def jugar_carta(carta, jugador):
    """
    Funcion que se llama para jugar una carta, crea y devuelve una funcion que al ser llamada
    ejecuta la logica para jugar una carta.

    :param carta: Carta a jugar
    :param jugador: Jugador que juega la carta
    :return:
    """

    def _jugar_carta():
        mano_actual = get_current_hand()
        ronda_actual = get_current_round()

        if jugador == USUARIO:
            mano_actual['cartas_usuario'].remove(carta)
            ronda_actual.update({
                "carta_usuario": carta,
            })
        else:
            mano_actual['cartas_computadora'].remove(carta)
            ronda_actual.update({
                "carta_computadora": carta,
            })

        print(f"{jugador.capitalize()} jugo {formatear_carta(carta)}")

        if is_last_action_in_round():
            add_action(determinar_ganador_ronda)
        else:
            add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

        return noop

    return _jugar_carta


def cantar_truco(jugador):
    """
    Funcion que se llama para cantar truco, crea y devuelve una funcion que al ser llamada

    :param jugador: Jugador que va a cantar el truco
    :return:
    """

    def _cantar_truco():
        mano_actual = get_current_hand()
        mano_actual['truco'].update({
            "activo": False,
            "cantado_por": jugador,
            "nivel": 1
        })

        if is_last_action_in_round():
            pass
        else:
            add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

        return noop

    return _cantar_truco


def aceptar_truco(jugador):
    """
    Funcion que se llama para aceptar el truco, crea y devuelve una funcion que al ser llamada
    ejecuta la logica para aceptar el truco.

    :param jugador: Jugador que va a aceptar el truco
    :return:
    """

    def _aceptar_truco():
        mano_actual = get_current_hand()
        mano_actual['truco'].update({
            "activo": True,
        })

        if is_last_action_in_round():
            add_action(determinar_ganador_ronda)
        else:
            add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

        return noop

    return _aceptar_truco


def rechazar_truco(jugador):
    """
    Funcion que se llama para rechazar el truco, crea y devuelve una funcion que al ser llamada
    ejecuta la logica para rechazar el truco.

    :param jugador: Jugador que va a rechazar el truco
    :return:
    """

    def _rechazar_truco():
        mano_actual = get_current_hand()
        mano_actual['truco'].update({
            "activo": False,
            "rechazado_por": jugador,
        })

        if is_last_action_in_round():
            add_action(determinar_ganador_ronda)
        else:
            add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

        return noop

    return _rechazar_truco


def cantar_envido(jugador):
    """
    Funcion que se llama para cantar envido, crea y devuelve una funcion que al ser llamada

    :param jugador: Jugador que va a cantar el envido
    :return:
    """

    def _cantar_envido():
        mano_actual = get_current_hand()
        mano_actual['envido'].update({
            "activo": False,
            "cantado_por": jugador,
            "nivel": 1
        })

        if is_last_action_in_round():
            pass
        else:
            add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

        return noop

    return _cantar_envido


def aceptar_envido(jugador):
    """
    Funcion que se llama para aceptar el envido, crea y devuelve una funcion que al ser llamada
    ejecuta la logica para aceptar el envido.

    :param jugador: Jugador que va a aceptar el envido
    :return:
    """

    def _aceptar_envido():
        mano_actual = get_current_hand()
        mano_actual['envido'].update({
            "activo": True,
        })

        if is_last_action_in_round():
            add_action(determinar_ganador_ronda)
        else:
            add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

        return noop

    return _aceptar_envido


def rechazar_envido(jugador):
    """
    Funcion que se llama para rechazar el envido, crea y devuelve una funcion que al ser llamada
    ejecuta la logica para rechazar el envido.

    :param jugador: Jugador que va a rechazar el envido
    :return:
    """

    def _rechazar_envido():
        mano_actual = get_current_hand()
        mano_actual['envido'].update({
            "activo": False,
            "rechazado_por": jugador,
        })

        if is_last_action_in_round():
            add_action(determinar_ganador_ronda)
        else:
            add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

        return noop

    return _rechazar_envido