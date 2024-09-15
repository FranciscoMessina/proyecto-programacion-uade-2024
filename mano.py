from acciones_usuario import pedir_accion_usuario
from computadora import responder_a_usuario, actuar_computadora
from mazo import repartir_cartas, mazo_truco, determinar_carta_mayor
from utilidades import formatear_carta


def jugar_mano(partida):
    """
    Juega una mano de truco, esta funcion es ejecutada las veces necesarias para llegar a los puntos maximos de la partida
    :param partida: estado actual de la partida
    :return:
    """
    # Antes de comenzar una nueva mano se verifica si alguno de los jugadores llego a los puntos maximos,
    # en ese caso se termina la partida
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

    # Aca empieza una nueva mano.
    print(f"Iniciando una nueva mano".center(60, "-"))

    # Se reparten las cartas a cada jugadora
    cartas_usuario, cartas_computadora = repartir_cartas(mazo_truco)

    # Se incrementa la cantidad de manos jugadas
    partida['manos_jugadas'] += 1

    # se actualiza el estado de la partida, reiniciando la Mano Actual
    partida['mano_actual'] = {
        'rondas': [],
        "truco": {},
        "envido": {},
    }

    # variable de utilidad para acceder mas facilmente a la mano_actual
    mano_actual = partida['mano_actual']

    continuar = True
    numero_de_ronda = 1
    # Generalmente las manos del truco constan de 3 rondas, pero hay situaciones en las cuales se terminan antes
    # por eso tenemos un while con una condicion de corte en 4 rondas y una bandera: continuar.
    # Esta ultima puede ser modificada dentro de la ronda para darle un final temprano.
    while continuar and numero_de_ronda < 4:
        # Este es el inicio de una nueva ronda en la mano actual.
        # Agregamos a la lista de rondas de la mano una nueva ronda.
        mano_actual['rondas'].append({
            "ganador": None,
        })

        # Guardamos en una variable de utilidad la ronda actual para acceder mas facilmente a ella.
        ronda_actual = partida['mano_actual']['rondas'][-1]
        # Guardamos en una variable de utilidad la ronda anterior para acceder mas facilmente a ella.
        # Si es la primera ronda, la ronda anterior es un diccionario vacio.
        ronda_anterior = partida['mano_actual']['rondas'][-2] if numero_de_ronda > 1 else {}

        # Si la ronda la gano el usuario o hubo empate la siguiente ronda la empieza el usuario
        # Por ahora tambien si es la primera ronda siempre comienza el usuario, lo mismo si la ronda anterior fue empate.
        if numero_de_ronda == 1 or numero_de_ronda != 1 and ronda_anterior['ganador'] == 'usuario' or ronda_anterior[
            'ganador'] == 'empate':

            # Bandera para determinar el final del turno del jugador, que es cuando juega una carta
            esperando_carta = True

            while esperando_carta:
                # Pedimos al usuario que elija que hacer en su turno
                input_usuario = pedir_accion_usuario(cartas_usuario, partida, numero_de_ronda)

                if input_usuario['accion'] == 'jugar_carta':
                    # Si elije jugar una carta, sacamos la misma de su mano actual.
                    cartas_usuario.remove(input_usuario['carta'])
                    # Guardamos la carta jugada en la ronda actual
                    ronda_actual['carta_usuario'] = input_usuario['carta']

                    print(f"Jugaste {formatear_carta(ronda_actual['carta_usuario'])}")

                    # Cambiamos la bandera para que siga la ronda.
                    esperando_carta = False

                    # Pedimos respuesta a la computadora
                    respuesta_computadora = responder_a_usuario(input_usuario, cartas_computadora, partida,
                                                                numero_de_ronda)

                    if respuesta_computadora['accion'] == "jugar_carta":
                        # Si la computadora juega una carta, la sacamos de su mano.
                        cartas_computadora.remove(respuesta_computadora['carta'])
                        # Guardamos la carta jugada en la ronda actual
                        ronda_actual['carta_computadora'] = respuesta_computadora['carta']

                        print(f"La computadora jugo {formatear_carta(ronda_actual['carta_computadora'])}")

                if input_usuario['accion'] == 'cantar_truco':
                    # logica de cantar truco
                    print("CANTASTE TRUCO")
                    # Actualizamos la propiedad truco de la mano actual
                    mano_actual['truco'] = {
                        "cantado_por": "usuario",
                        # Indica el nivel del truco, 0 es sin cantar, 1 es truco, 2 es retruco, 3 vale cuatro
                        "nivel": 0,
                    }

                    respuesta_computadora = responder_a_usuario(input_usuario, cartas_computadora, partida,
                                                                numero_de_ronda)
                    if respuesta_computadora['accion'] == 'aceptar':
                        # Si la computadora acepta, cambiamos el nivel del truco a 1
                        print('ACEPTADO')
                        mano_actual['truco'].update({
                            "nivel": 1
                        })
                    elif respuesta_computadora['accion'] == 'rechazar':
                        # Si la computadora rechaza, agregamos a la propiedad truco de la mano actual quien lo rechazo
                        print("RECHAZADO")
                        mano_actual['truco'].update({
                            "rechazado_por": "computadora"
                        })
                        # Como al rechazar un truco termina, tanto la ronda como la mano, indicamos que esta ronda fue ganada por el usuario
                        ronda_actual['ganador'] = 'usuario'
                        # Actualizamos las bandera para que finalice la mano
                        continuar = False
                        esperando_carta = False
        # Si la ronda la gana la compu, la compu empieza y tira una carta
        elif ronda_anterior['ganador'] == 'computadora':
            # Por ahora la computadora siempre juega una carta al azar
            accion_computadora = actuar_computadora(cartas_computadora, partida, numero_de_ronda)

            if accion_computadora['accion'] == "jugar_carta":
                # Esto es codigo repetido, que vamos a refactorizar para la proxima entrega
                print(f"La computadora jugo {formatear_carta(accion_computadora['carta'])}")
                cartas_computadora.remove(accion_computadora['carta'])
                ronda_actual['carta_computadora'] = accion_computadora['carta']

            esperando_carta = True
            # Aca se repite el flujo de accionar como si el usuario fuese primero, va a ser refactorizado para evitar tanta duplicacion.
            while esperando_carta:
                respuesta_usuario = pedir_accion_usuario(cartas_usuario, partida, numero_de_ronda)

                if respuesta_usuario['accion'] == "jugar_carta":
                    cartas_usuario.remove(respuesta_usuario['carta'])
                    ronda_actual['carta_usuario'] = respuesta_usuario['carta']
                    print(f"Jugaste {formatear_carta(ronda_actual['carta_usuario'])}")
                    esperando_carta = False
                elif respuesta_usuario['accion'] == 'cantar_truco':
                    print("CANTASTE TRUCO")
                    mano_actual['truco'] = {
                        "cantado_por": "usuario",
                        "nivel": 0,
                    }
                    respuesta_computadora = responder_a_usuario(respuesta_usuario, cartas_computadora, partida,
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
        # Aca verificamos si se canto truco y si fue rechazado, de ser asi salimos del ciclo de rondas
        if mano_actual['truco'].get('rechazado_por') is not None:
            break
        # Se determina que carta gana
        carta_ganadora = determinar_carta_mayor(ronda_actual['carta_usuario'],
                                                ronda_actual['carta_computadora'])

        # Verificamos a quien pertenece la carta ganadora, si es empate se indica como tal.
        # Y guardamos el ganador de la ronda.
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

    # Determinamos quien gano la ronda actual
    ganador_mano = determinar_ganador_de_la_mano(mano_actual)

    # Determinamos cuantos puntos se lleva el ganador de la mano
    puntos_a_sumar = determinar_puntos(mano_actual)

    # Sumamos los puntos al ganador de la mano
    partida['puntos'][ganador_mano] += puntos_a_sumar

    print(f"Gana {ganador_mano} sumando {puntos_a_sumar} puntos")
    # Printea un grafico que muestra los puntos de cada jugador
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
    """
    Calcula cuantos puntos hay que sumar al ganador de la mano
    :param mano: mano actual
    :return:
    """
    # Siempre se suma 1 punto por ganar la mano
    puntos = 1

    if mano['truco']:
        # Si hubiese truco, se suman los puntos correspondientes al nivel del truco
        puntos += mano['truco']['nivel']

    return puntos


def determinar_ganador_de_la_mano(mano):
    """
    Determina quien gano la mano actual
    :param mano: mano actual
    :return:
    """

    # Si se canto truco, y fue rechazado, automatica gana el que lo canto
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
        # Sumamos cuantas rondas gano cada jugador
        rondas_ganadas[ronda['ganador']] += 1

    # Empata la primera, gana el siguiente ganador.
    if ronda_1['ganador'] == 'empate':
        return ronda_2['ganador'] if ronda_2['ganador'] != 'empate' else ronda_3['ganador']

    # Si se empata cualquier ronda menos la primera, gana el que gano la primera.
    if rondas_ganadas['empate'] > 0 and ronda_1['ganador'] != 'empate':
        return ronda_1['ganador']

    return "usuario" if rondas_ganadas['usuario'] > rondas_ganadas['computadora'] else 'computadora'
