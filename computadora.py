import random
from random import choice

from envido import calcular_puntos_envido_computadora
from mazo import obtener_poder
from utilidades import dev_print
from variables import get_computer_cards, get_current_round, get_current_hand, COMPUTADORA, USUARIO, \
    envido_needs_answer, truco_needs_answer, is_first_round, envido_rechazado_por, envido_cantado_por


def actuar_computadora():
    """
    Determina como acciona la computadora en su turno.

    :return:
    """
    from acciones import cantar_envido, cantar_truco, jugar_carta

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

        envido_puntos = calcular_puntos_envido_computadora()

        if envido_puntos >= 30:
            opciones = [
                (cantar_envido(COMPUTADORA, 'envido'), 30),
                (cantar_envido(COMPUTADORA, 'real_envido'), 40),
                (cantar_envido(COMPUTADORA, 'falta_envido'), 20),
            ]

            return elegir_opcion(opciones)

        elif 30 > envido_puntos >= 25:
            opciones = [
                (cantar_envido(COMPUTADORA, 'envido'), 50),
                (cantar_envido(COMPUTADORA, 'real_envido'), 20),
            ]

            return elegir_opcion(opciones)

    if mano_actual['truco'].get('nivel') == 0:
        dev_print('AC- Cantar truco')

        c_truco = elegir_opcion([
            (True, 60),
            (False, 40)
        ])

        if c_truco:
            return cantar_truco(COMPUTADORA, 1)

    elif mano_actual['truco'].get('nivel') == 1 and mano_actual['truco'].get('cantado_por') == USUARIO:
        dev_print('AC- Cantar truco')

        c_truco = elegir_opcion([
            (True, 35),
            (False, 60)
        ])

        if c_truco:
            return cantar_truco(COMPUTADORA, 2)


    elif mano_actual['truco'].get('nivel') == 2 and mano_actual['truco'].get('cantado_por') == USUARIO:
        dev_print('AC- Cantar truco')

        c_truco = elegir_opcion([
            (True, 35),
            (False, 60)
        ])

        if c_truco:
            return cantar_truco(COMPUTADORA, 3)

    if get_current_round().get('carta_usuario') is not None:
        dev_print('AC- Responder a carta')
        return responder_a_carta()

    dev_print('AC- Jugar carta')

    carta_random = choice(cartas)

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

    puntos_de_envido = calcular_puntos_envido_computadora()

    opciones = []
    if 'falta_envido' in cantados:

        if puntos_de_envido >= 30:
            opciones = [
                (aceptar_envido(COMPUTADORA), 90),
                (rechazar_envido(COMPUTADORA), 10)
            ]
        elif 30 > puntos_de_envido >= 27:
            opciones = [
                (aceptar_envido(COMPUTADORA), 70),
                (rechazar_envido(COMPUTADORA), 30)
            ]
        elif 27 > puntos_de_envido >= 24:
            opciones = [
                (aceptar_envido(COMPUTADORA), 30),
                (rechazar_envido(COMPUTADORA), 70)
            ]
        else:
            opciones = [
                (rechazar_envido(COMPUTADORA), 100)
            ]

    elif 'real_envido' in cantados:

        if puntos_de_envido >= 30:
            opciones = [
                (cantar_envido(COMPUTADORA, "falta_envido"), 40),
                (aceptar_envido(COMPUTADORA), 50),
                (rechazar_envido(COMPUTADORA), 10)
            ]
        elif 30 > puntos_de_envido >= 27:
            opciones = [
                (cantar_envido(COMPUTADORA, "falta_envido"), 20),
                (aceptar_envido(COMPUTADORA), 60),
                (rechazar_envido(COMPUTADORA), 20)
            ]
        elif 27 > puntos_de_envido >= 24:
            opciones = [
                (aceptar_envido(COMPUTADORA), 30),
                (rechazar_envido(COMPUTADORA), 70)
            ]
        else:
            opciones = [(rechazar_envido(COMPUTADORA), 100)]


    elif 'envido_2' in cantados:

        if puntos_de_envido >= 30:
            opciones = [
                (cantar_envido(COMPUTADORA, "real_envido"), 60),
                (aceptar_envido(COMPUTADORA), 30),
                (rechazar_envido(COMPUTADORA), 10)
            ]
        elif 30 > puntos_de_envido >= 27:
            opciones = [
                (cantar_envido(COMPUTADORA, "real_envido"), 25),
                (aceptar_envido(COMPUTADORA), 60),
                (rechazar_envido(COMPUTADORA), 15)
            ]
        elif 27 > puntos_de_envido >= 24:
            opciones = [
                (aceptar_envido(COMPUTADORA), 30),
                (rechazar_envido(COMPUTADORA), 70)
            ]
        else:
            opciones = [(rechazar_envido(COMPUTADORA), 100)]


    elif 'envido' in cantados:

        if puntos_de_envido > 30:
            opciones = [
                (cantar_envido(COMPUTADORA, "real_envido"), 25),
                (cantar_envido(COMPUTADORA, 'envido_2'), 30),
                (cantar_envido(COMPUTADORA, 'falta_envido'), 10),
                (aceptar_envido(COMPUTADORA), 30),
                (rechazar_envido(COMPUTADORA), 5)
            ]
        elif 30 > puntos_de_envido > 27:
            opciones = [
                (cantar_envido(COMPUTADORA, "real_envido"), 25),
                (aceptar_envido(COMPUTADORA), 55),
                (rechazar_envido(COMPUTADORA), 20)
            ]
        elif 27 > puntos_de_envido > 24:
            opciones = [
                (aceptar_envido(COMPUTADORA), 30),
                (rechazar_envido(COMPUTADORA), 70)
            ]
        else:
            opciones = [(rechazar_envido(COMPUTADORA), 80), (aceptar_envido(COMPUTADORA), 20)]
    print('Puntos envido pc', puntos_de_envido)
    print(opciones)
    return elegir_opcion(opciones)


def evaluar_fuerza_mano():
    """
    Evalúa la fuerza de la mano de la computadora.
    :param cartas: Lista de cartas de la computadora.
    :return: Fuerza de la mano.
    """
    cartas = get_computer_cards()

    return sum(obtener_poder(carta) for carta in cartas)


def responder_a_truco():
    """
    Determina como responde la computadora a un truco cantado por el usuario.
    :return: Function
    """
    from acciones import aceptar_truco, cantar_truco, rechazar_truco

    mano_actual = get_current_hand()
    cartas_computadora = get_computer_cards()
    fuerza_mano = evaluar_fuerza_mano()
    opciones = []

    if mano_actual['truco'].get('nivel') == 1:
        if fuerza_mano > 20:
            opciones = [
                (cantar_truco(COMPUTADORA, 2), 50),
                (aceptar_truco(COMPUTADORA), 40),
                (rechazar_truco(COMPUTADORA), 10)
            ]
        else:
            opciones = [
                (aceptar_truco(COMPUTADORA), 60),
                (rechazar_truco(COMPUTADORA), 40)
            ]
    elif mano_actual['truco'].get('nivel') == 2:
        if fuerza_mano > 25:
            opciones = [
                (cantar_truco(COMPUTADORA, 3), 40),
                (aceptar_truco(COMPUTADORA), 50),
                (rechazar_truco(COMPUTADORA), 10)
            ]
        else:
            opciones = [
                (aceptar_truco(COMPUTADORA), 70),
                (rechazar_truco(COMPUTADORA), 30)
            ]
    elif mano_actual['truco'].get('nivel') == 3:
        if fuerza_mano > 30:
            opciones = [
                (aceptar_truco(COMPUTADORA), 80),
                (rechazar_truco(COMPUTADORA), 20)
            ]
        else:
            opciones = [
                (aceptar_truco(COMPUTADORA), 50),
                (rechazar_truco(COMPUTADORA), 50)
            ]

    return elegir_opcion(opciones)


def elegir_opcion(opciones):
    """

    :param opciones: una lista de tuplas, el primer elemento de cada tupla es la opcion a ejecutar, y el segundo elemento es el peso (chances de elegir) de esa opcion.
    :return:
    """
    _opciones = []
    pesos = []

    for opcion, peso in opciones:
        _opciones.append(opcion)
        pesos.append(peso)

    return random.choices(_opciones, pesos)[0]
