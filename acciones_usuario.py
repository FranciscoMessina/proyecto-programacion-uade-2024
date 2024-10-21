
from guardado import guardar_partida
from computadora import responder_a_carta, responder_a_truco, responder_a_envido
from envido import calcular_envido
from ronda import determinar_ganador_ronda

from utilidades import formatear_carta, pedir_eleccion, noop
from variables import get_current_hand, get_user_cards, is_first_round, get_current_round, add_action, \
    is_last_action_in_round



def pedir_accion_usuario():
    """
    Muestra al usuario la acciones disponibles y le pide que elija una de ellas

    :param cartas: cartas que tiene el jugador
    :param partida: estado actual de la partida
    :param numero_ronda:  numero de la ronda actual
    :return: valor de la accion que el jugador desea tomar
    """
    opciones = []


    mano_actual = get_current_hand()
    cartas = get_user_cards()

    if is_first_round():
        puntos_envido = calcular_envido(cartas)
        print(f"Tenes {puntos_envido} de envido")
        if mano_actual['envido'].get("activo") is False and mano_actual['envido'].get("cantado_por") is None:
            opciones.append(["Cantar envido", cantar_envido()])

        if mano_actual['envido'].get("cantado_por") == "computadora":
            opciones.append(["Aceptar envido", {"accion": "aceptar_envido"}])
            opciones.append(["No aceptar envido", {"accion": "no_aceptar_envido"}])

    if mano_actual['truco'].get('cantado_por') == "computadora" and mano_actual["truco"].get('nivel') == 0:
        # Si la computadora canta truco se le da la opcion al usuario de aceptar
        opciones.append(["Quiero", {"accion": "aceptar_truco"}])
        opciones.append(["No quiero", {"accion": "rechazar_truco"}])

    else:
        for carta in cartas:
            # Por cada carta en su mano agregamos la opcion de jugarla.
            opciones.append([f"Jugar {formatear_carta(carta)}", jugar_carta(carta)])


    if partida['mano_actual']['guardado'].get('nivel') is None:
            # Si no se ha cantado truco aun, se le da la opcion de cantar truco
            opciones.append(["Guardar Partida", {"accion":"guardar_partida"}])




    if mano_actual['truco'].get('activo') is False:
        # Si no se ha cantado truco aun, se le da la opcion de cantar truco
        opciones.append(["Cantar truco", cantar_truco()])
    """    
    if partida['mano_actual']['truco'].get('nivel') == 1:
        opciones.append(["Cantar retruco", {"accion": "cantar_retruco"}])

    if partida['mano_actual']['truco'].get('nivel') == 2:
        opciones.append(["Cantar vale 4", {"accion": "cantar_vale_4"}])
    """
    return pedir_eleccion(opciones)


def jugar_carta(carta):
    """
    Crea la funcion que va a ser utilizada para jugar la carta del usuario

    :param carta: carta a jugar

    :return: Funcion para jugar la carta
    """

    def _jugar_carta():

        nonlocal carta

        cartas = get_user_cards()
        cartas.remove(carta)

        ronda_actual = get_current_round()

        ronda_actual['carta_usuario'] = carta
        print(f"Jugaste el {formatear_carta(carta)}")

        # print('__??', is_last_action_in_round())
        if is_last_action_in_round():
            add_action(determinar_ganador_ronda)
            print('Es la ultima accion de la ronda')
        else:
            add_action(responder_a_carta)

        return noop

    return _jugar_carta


def cantar_truco():
    """
    Crea la funcion que va a ser utilizada para cantar truco

    :return: Funcion para cantar truco
    """

    def _cantar_truco():
        mano_actual = get_current_hand()
        mano_actual['truco'].update({
            "activo": False,
            "cantado_por": "usuario",
            "nivel": 1
        })

        if is_last_action_in_round():
            pass
        else:
            add_action(responder_a_truco)

        return noop

    return _cantar_truco


def cantar_envido():
    """
    Crea la funcion que va a ser utilizada para cantar envido

    :return: Funcion para cantar envido
    """

    def _cantar_envido():
        mano_actual = get_current_hand()
        mano_actual['envido'].update({
            "activo": False,
            "cantado_por": "usuario",
            "nivel": 1
        })

        if is_last_action_in_round():
            pass
        else:
            add_action(responder_a_envido)

        return noop

    return _cantar_envido
