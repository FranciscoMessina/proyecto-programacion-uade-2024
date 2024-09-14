from acciones_usuario import pedir_accion_usuario
from computadora import responder_a_usuario, actuar_computadora
from mazo import repartir_cartas, mazo_truco, determinar_carta_mayor
from utilidades import formatear_carta


def jugar_mano(partida):
    print(f"Iniciando una nueva mano".center(60, "-"))

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
            "ganador": "computadora"
        }

    partida['mano_actual'] = {
        'rondas': [],
        "truco": {},
        "envido": {},
    }

    mano_actual = partida['mano_actual']

    continuar = True

    numero_de_ronda = 1

    while continuar and numero_de_ronda < 4:
        # Esto de aca adentro es cada ronda de una mano.
        mano_actual['rondas'].append({
            "ganador": None,
        })
        ronda_actual = partida['mano_actual']['rondas'][-1]

        ronda_anterior = partida['mano_actual']['rondas'][-2] if numero_de_ronda > 1 else {}

        if numero_de_ronda == 1 or numero_de_ronda != 1 and ronda_anterior['ganador'] == 'usuario' or ronda_anterior[
            'ganador'] == 'empate':

            esperando_carta = True

            while esperando_carta:
                input_usuario = pedir_accion_usuario(cartas_usuario, partida, numero_de_ronda)

                if input_usuario['accion'] == 'jugar_carta':
                    cartas_usuario.remove(input_usuario['carta'])
                    ronda_actual['carta_usuario'] = input_usuario['carta']

                    print(f"Jugaste {formatear_carta(ronda_actual['carta_usuario'])}")

                    esperando_carta = False

                    respuesta_computadora = responder_a_usuario(input_usuario, cartas_computadora, partida,
                                                                numero_de_ronda)

                    if respuesta_computadora['accion'] == "jugar_carta":
                        cartas_computadora.remove(respuesta_computadora['carta'])
                        ronda_actual['carta_computadora'] = respuesta_computadora['carta']
                        print(f"La computadora jugo {formatear_carta(ronda_actual['carta_computadora'])}")

                if input_usuario['accion'] == 'cantar_truco':
                    print("CANTASTE TRUCO")
                    mano_actual['truco'] = {
                        "cantado_por": "usuario",
                        "nivel": 0,
                    }
                    respuesta_computadora = responder_a_usuario(input_usuario, cartas_computadora, partida,
                                                                numero_de_ronda)
                    if respuesta_computadora['accion'] == 'aceptar':
                        print('ACEPTADO')
                        mano_actual['truco'].update({
                            "nivel": 1
                        })
                    elif respuesta_computadora['accion'] == 'rechazar':
                        print("RECHAZADO")
                        mano_actual['truco'].update({
                            "rechazado_por": "computadora"
                        })
                        ronda_actual['ganador'] = 'usuario'
                        continuar = False
                        esperando_carta = False

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

        if mano_actual['truco'].get('rechazado_por') is not None:
            break

        carta_ganadora = determinar_carta_mayor(ronda_actual['carta_usuario'],
                                                ronda_actual['carta_computadora'])

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

    ganador_mano = determinar_ganador_de_la_mano(mano_actual)

    puntos_a_sumar = determinar_puntos(mano_actual)

    partida['puntos'][ganador_mano] += puntos_a_sumar

    print(f"Gana {ganador_mano} sumando {puntos_a_sumar} puntos")

    print("|", end="")
    print(" PUNTOS ".center(85, '='), end='|\n')
    print("|---  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30", end='|\n')
    print(f"|TU: {" *" * partida['puntos']['usuario']} ", end='')
    print("|".rjust(81 - partida['puntos']['usuario'] * 2))
    print(f"|PC: {" *" * partida['puntos']['computadora']} ", end='')
    print("|".rjust(81 - partida['puntos']['computadora'] * 2))
    print("|", end="")
    print("".center(85, '='), end='|\n')

    return {
        "accion": "none"
    }


def determinar_puntos(mano):
    puntos = 1

    if mano['truco']:
        puntos += mano['truco']['nivel']

    return puntos


def determinar_ganador_de_la_mano(mano):
    if mano['truco'].get('rechazado_por') is not None:
        return mano['truco']['cantado_por']

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
