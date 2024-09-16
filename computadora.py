from random import choice

from mazo import obtener_poder


def actuar_computadora(cartas, partida, numero_ronda):
    """
    Determina como acciona la computadora en su turno, cuando no tiene que responder al usuario.

    :param cartas: cartas que tiene la computadora
    :param partida: estado actual de la partida
    :param numero_ronda: numero de la ronda actual
    :return:
    """

    # Por ahora solo juega una carta al azar, le vamos a agregar la posibilidad de cantar truco y envido
    # y tal vez de elegir con mas logica que carta jugar
    carta_random = choice(cartas)

    return {
        "accion": "jugar_carta",
        "carta": carta_random
    }


def responder_a_usuario(accion_usuario, cartas_computadora, partida, numero_ronda):
    """
    Determina la respuesta de la computadora frente a una accion del usuario

    :param accion_usuario: La accion que realizo el usuario
    :param cartas_computadora: las cartas que tiene la computadora
    :param partida: estado actual de la partida
    :param numero_ronda: numero de la ronda actual
    :return:
    """
    if accion_usuario['accion'] == 'jugar_carta':
        # Si el usuario jugo una carta, la computadora responde jugando una carta
        return responder_a_carta(accion_usuario['carta'], cartas_computadora, partida, numero_ronda)
    elif accion_usuario['accion'] == 'cantar_truco':
        # Si el usuario canto truco, la computadora responde aceptando o rechazando (por ahora 50% de cada opcion, a mejorar)
        return choice([{"accion": "aceptar"}, {"accion": "rechazar"}])
    else:
        return None


def responder_a_carta(carta_jugada, cartas_computadora, partida, numero_ronda):
    """
    Determina con que carta responder a una carta jugada por el usuario la computadora

    :param carta_jugada: carta jugada por el usuario
    :param cartas_computadora: cartas que tiene la computadora
    :param partida: estado actual de la partida
    :param numero_ronda: numero de la ronda actual
    :return:
    """

    # Filtramos las cartas de la computadora para dejar solo las que le ganan o empatan a la carta jugada por el usuario
    cartas_mas_fuertes = list(
        filter(lambda carta: obtener_poder(carta_jugada) <= obtener_poder(carta), cartas_computadora))

    if len(cartas_mas_fuertes) > 0:
        # Si tiene cartas que le gganan o empata, juega la de menor valor disponible
        return {"accion": "jugar_carta", "carta": cartas_mas_fuertes[0]}

    # TODO: falta manejar caso de carta empardadora

    # Si no tiene cartas que le ganen juega la carta mas baja que tenga ( su mano esta ordenada de menor a mayor poder)
    return {"accion": "jugar_carta", "carta": cartas_computadora[0]}
