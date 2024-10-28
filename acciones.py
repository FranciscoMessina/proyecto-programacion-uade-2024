from acciones_usuario import pedir_accion_usuario
from computadora import actuar_computadora
from ronda import determinar_ganador_ronda
from utilidades import formatear_carta, noop, dev_print
from variables import get_current_hand, get_current_round, is_last_action_in_round, add_action, USUARIO, COMPUTADORA, \
    niveles_nombre


def jugar_carta(carta, jugador):
    """
    Funcion que se llama para jugar una carta, crea y devuelve una funcion que al ser llamada
    ejecuta la logica para jugar una carta.

    :param carta: Carta a jugar
    :param jugador: Jugador que juega la carta
    :return:
    """

    dev_print('Jugar Carta Builder')

    def _jugar_carta():
        mano_actual = get_current_hand()
        ronda_actual = get_current_round()

        dev_print('Jugar Carta Execution')

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
            dev_print('LAST ACTION IN ROUND')
            add_action(determinar_ganador_ronda)
        else:
            add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

        return noop

    return _jugar_carta


def cantar_truco(jugador, nivel):
    """
    Funcion que se llama para cantar truco, crea y devuelve una funcion que al ser llamada
    ejecuta la logica para cantar el truco.

    :param jugador: Jugador que va a cantar el truco
    :param nivel: Nivel del truco a cantar (1, Truco) (2, Retruco) (3, Vale Cuatro)
    :return:
    """

    dev_print('Cantar Truco Builder')

    def _cantar_truco():
        mano_actual = get_current_hand()
        mano_actual['truco'].update({
            "activo": False,
            "cantado_por": jugador,
            "nivel": nivel,
            "esperando": True
        })

        dev_print('Cantar Truco Execution')




        print(f"{jugador.capitalize()} canta {niveles_nombre[nivel]}")

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

    dev_print('Aceptar Truco Builder')

    def _aceptar_truco():
        mano_actual = get_current_hand()
        mano_actual['truco'].update({
            "activo": True,
            "esperando": False,
        })

        dev_print('Aceptar Truco Execution')

        print(f"{jugador.capitalize()} quiere el truco")

        if is_last_action_in_round():
            dev_print('LAST ACTION IN TRUCO')
            add_action(determinar_ganador_ronda)
        else:
            dev_print('NOT LAST ACTION IN TRUCO')
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

    dev_print('Rechazar Truco Builder')

    def _rechazar_truco():
        mano_actual = get_current_hand()
        mano_actual['truco'].update({
            "activo": False,
            "rechazado_por": jugador,
            "esperando": False
        })

        dev_print('Rechazar Truco Execution')

        print(f"{jugador.capitalize()} no quiere el truco")

        return noop

    return _rechazar_truco



def cantar_envido( jugador):
    """
    Funcion que se llama para cantar envido, crea y devuelve una funcion que al ser llamada

    :param jugador: Jugador que va a cantar el envido
    :return:
    """

    dev_print('Cantar Envido Builder')

    def _cantar_envido():
        mano_actual = get_current_hand()
        mano_actual['envido'].update({
            "activo": False,
            "cantado_por": jugador,
            "cantos": [],
            "nivel": 1,
            "esperando": True
        })

        dev_print('Cantar Envido Execution')

        print(f"{jugador.capitalize()} canta envido")

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

    dev_print('Aceptar Envido Builder')

    def _aceptar_envido():
        mano_actual = get_current_hand()
        mano_actual['envido'].update({
            "activo": True,
            "esperando": False
        })

        dev_print('Aceptar Envido Execution')

        print(f"{jugador.capitalize()} acepta el envido")

        # aca falta agregar la accion para determinar el ganador del envido, y sumar los puntos correspondientes
        # add_action()
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

    dev_print('Rechazar Envido Builder')

    def _rechazar_envido():
        mano_actual = get_current_hand()
        mano_actual['envido'].update({
            "activo": False,
            "rechazado_por": jugador,
            "esperando": False
        })

        dev_print('Rechazar Envido Execution')

        print(f"{jugador.capitalize()} no quiere el envido")

        # aca falta agregar la accion para calcular los puntos en base a que nivel de envido estemos,
        # y que se sumen a los puntos del jugador que lo habia cantado.
        # add_action()

        # Despues se deberia llamar a la accion para pedir la proxima accion del jugador o computadora
        add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

        return noop

    return _rechazar_envido
