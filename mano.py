from acciones_usuario import pedir_accion_usuario
from mazo import repartir_cartas, mazo_truco


def jugar_mano(partida, terminar_partida):
    cartas_usuario, cartas_computadora = repartir_cartas(mazo_truco)
    partida['manos_jugadas'] += 1

    if partida['puntos_usuario'] >= partida['puntos_maximos']:
        terminar_partida('usuario')
        return
    elif partida['puntos_computadora'] >= partida['puntos_maximos']:
        terminar_partida('computadora')
        return

    continuar = True
    ronda = 1
    while continuar and ronda < 4:
        partida['mano_actual']['rondas'].append({
            "ganador": None
        })

        if partida['mano_actual']['rondas'][-1]['ganador'] is None:
            input_usuario = pedir_accion_usuario(cartas_usuario, partida, ronda)

            if input_usuario['accion'] == 'jugar_carta':
                cartas_usuario.remove(input_usuario['carta'])

    return
