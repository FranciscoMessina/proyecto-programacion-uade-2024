from random import choice

from mazo import obtener_poder


def actuar_computadora(cartas, partida, numero_ronda):
    carta_random = choice(cartas)

    return {
        "accion": "jugar_carta",
        "carta": carta_random
    }


def responder_a_usuario(accion_usuario, cartas_computadora, partida, numero_ronda):
    if accion_usuario['accion'] == 'jugar_carta':
        return responder_a_carta(accion_usuario['carta'], cartas_computadora, partida, numero_ronda)
    elif accion_usuario['accion'] == 'cantar_truco':
        return choice([{"accion": "aceptar"}, {"accion": "rechazar"}])
    else:
        return None


def responder_a_carta(carta_jugada, cartas_computadora, partida, numero_ronda):
    cartas_mas_fuertes = list(
        filter(lambda carta: obtener_poder(carta_jugada) <= obtener_poder(carta), cartas_computadora))

    if len(cartas_mas_fuertes) > 0:
        return {"accion": "jugar_carta", "carta": cartas_mas_fuertes[0]}

    # TODO: falta manejar caso de carta empardadora

    return {"accion": "jugar_carta", "carta": cartas_computadora[0]}
