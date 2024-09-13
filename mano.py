from acciones_usuario import pedir_accion_usuario
from computadora import responder_a_usuario, actuar_computadora
from mazo import repartir_cartas, mazo_truco, determinar_carta_mayor
from utilidades import formatear_carta


def jugar_mano(partida):
    print(f"Inciando mano numero {partida["manos_jugadas"] + 1}")
    cartas_usuario, cartas_computadora = repartir_cartas(mazo_truco)
    partida['manos_jugadas'] += 1

    if partida['puntos']['usuario'] >= partida['puntos_maximos']:
        return {
            "accion": "terminar_partida",
            "ganador": "usuario"
        }
    elif partida['puntos']['computadora'] >= partida['puntos_maximos']:
        return {
            "accion": "terminar_partida",
            "ganador": "usuario"
        }

    continuar = True
    numero_de_ronda = 1
    while continuar and numero_de_ronda < 4:
        # Esto de aca adentro es cada ronda de una mano.
        partida['mano_actual']['rondas'].append({
            "ganador": None,
        })
        ronda_actual = partida['mano_actual']['rondas'][-1]

        ronda_anterior = partida['mano_actual']['rondas'][-2] if numero_de_ronda > 1 else {}

        # print("Ronda Anterior")
        # print(ronda_anterior)
        # print("ronda actual")
        # print(ronda_actual)

        if numero_de_ronda == 1 or numero_de_ronda != 1 and ronda_anterior['ganador'] == 'usuario' or ronda_anterior[
            'ganador'] == 'empate':
            input_usuario = pedir_accion_usuario(cartas_usuario, partida, numero_de_ronda)

            if input_usuario['accion'] == 'jugar_carta':
                cartas_usuario.remove(input_usuario['carta'])
                ronda_actual['carta_usuario'] = input_usuario['carta']
                print(f"Jugaste {formatear_carta(ronda_actual['carta_usuario'])}")

                respuesta_computadora = responder_a_usuario(input_usuario, cartas_computadora, partida, numero_de_ronda)

                if respuesta_computadora['accion'] == "jugar_carta":
                    cartas_computadora.remove(respuesta_computadora['carta'])
                    ronda_actual['carta_computadora'] = respuesta_computadora['carta']
                    print(f"La computadora jugo {formatear_carta(ronda_actual['carta_computadora'])}")

        elif ronda_anterior['ganador'] == 'computadora':
            # tiene que empezar la computadora
            accion_computadora = actuar_computadora(cartas_computadora, partida, numero_de_ronda)

            if accion_computadora['accion'] == "jugar_carta":
                print(f"La computadora jugo {formatear_carta(accion_computadora['carta'])}")
                cartas_computadora.remove(accion_computadora['carta'])
                ronda_actual['carta_computadora'] = accion_computadora['carta']

                respuesta_usuario = pedir_accion_usuario(cartas_usuario, partida, numero_de_ronda)

                if respuesta_usuario['accion'] == "jugar_carta":
                    cartas_usuario.remove(respuesta_usuario['carta'])
                    ronda_actual['carta_usuario'] = respuesta_usuario['carta']

        carta_ganadora = determinar_carta_mayor(ronda_actual['carta_usuario'], ronda_actual['carta_computadora'])

        if carta_ganadora == ronda_actual['carta_usuario']:
            ronda_actual['ganador'] = 'usuario'
        elif carta_ganadora == ronda_actual['carta_computadora']:
            ronda_actual['ganador'] = 'computadora'
        else:
            ronda_actual['ganador'] = 'empate'

        if carta_ganadora == 'empate':
            print(
                f"{formatear_carta(ronda_actual['carta_usuario'])} empata con {formatear_carta(ronda_actual['carta_computadora'])}")
        else:
            print(f"Gano {formatear_carta(carta_ganadora)}, jugada por {ronda_actual['ganador']}")

        numero_de_ronda += 1

    ganador_mano = determinar_ganador_de_la_mano(partida['mano_actual'])

    partida['puntos'][ganador_mano] += 1

    print(f"GANO LA MANO {ganador_mano}")

    print(partida['puntos'])

    return {
        "accion": "none"
    }


def determinar_ganador_de_la_mano(mano):
    ronda_1 = mano['rondas'][0]
    ronda_2 = mano['rondas'][1]
    ronda_3 = mano['rondas'][2]
    rondas_ganadas = {
        "usuario": 0,
        "computadora": 0,
        "empate": 0
    }

    for ronda in mano['rondas']:
        rondas_ganadas[ronda['ganador']] += 1

    # Empata la primera, gana el siguiente ganador.
    if ronda_1['ganador'] == 'empate':
        return ronda_2['ganador'] if ronda_2['ganador'] != 'empate' else ronda_3['ganador']

    # Si se empata cualquier ronda menos la primera, gana el que gano la primera.
    if rondas_ganadas['empate'] > 0 and ronda_1['ganador'] != 'empate':
        return ronda_1['ganador']

    return "usuario" if rondas_ganadas['usuario'] > rondas_ganadas['computadora'] else 'computadora'
