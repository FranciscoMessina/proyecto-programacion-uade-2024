from mazo import obtener_numero
from variables import COMPUTADORA, USUARIO, envido_puntos, get_computer_cards, get_current_hand, get_current_game, get_current_round, get_user_cards


def calcular_envido(mano):
    """
    Calcula los puntos de envido que tiene una mano
    :param mano: Lista con 3 cartas
    :return: el maximo envido posible de la mano
    """
    palos = {
        'espada': [],
        'basto': [],
        'oro': [],
        'copa': []
    }
    # Separa las cartas de la mano por palo
    for carta in mano:
        palos[carta[1]].append(carta)

    max_envido = 0

    for cartas in palos.values():
        # Iteramos por las cartas de cada palo
        if len(cartas) > 1:
            # Si hay más de una carta de un mismo palo, se calcula él envido, tomando las dos cartas con mayor valor y se le suman 20 puntos
            # Armamos una lista por compresión, con los números de las cartas, si el número es mayor a 7, se toma como 0
            valores = [obtener_numero(carta) if obtener_numero(carta) <= 7 else 0 for carta in cartas]
            # Ordenamos la lista en reversa y tomamos los dos primeros valores
            envido = 20 + sum(sorted(valores, reverse=True)[:2])
            # Comparamos el nuevo envido calculado con el previo máximo envido. Y guardamos el mayor valor.
            max_envido = max(max_envido, envido)
        elif len(cartas) == 1:
            # En este caso solo hay una carta de un palo, se toma el valor de la carta y si es mayor a 7, se toma como 0
            valor = obtener_numero(cartas[0])
            if valor > 7:
                valor = 0

            # Comparamos el nuevo envido calculado con el previo máximo envido. Y guardamos el mayor valor.
            max_envido = max(max_envido, valor)

    return max_envido


def envido(jugador):
    # Hay que modificar esto para que no reciba parámetros, sino que tome las manos de la partida actual
    # y solo devuelva como una string el ganador "usuario" o "computadora"
    cartas_usuario = get_user_cards()
    cartas_computadora = get_computer_cards()
    envido_usuario = calcular_envido(cartas_usuario)
    envido_compu = calcular_envido(cartas_computadora)

    # En estos casos alguno de los jugadores ya jugó una carta,
    # por lo que hay que agregarla a la mano para calcular él envido.
    if len(cartas_usuario) == 2:
        carta_jugada = get_current_round().get('carta_usuario')
        cartas_usuario.append(carta_jugada)
        envido_usuario = calcular_envido(cartas_usuario)
        cartas_usuario.pop()
    elif len(cartas_computadora) == 2:
        carta_jugada = get_current_round().get('carta_computadora')
        cartas_computadora.append(carta_jugada)
        envido_compu = calcular_envido(cartas_computadora)
        cartas_computadora.pop()


    partida_actual = get_current_game()

    puntos = envido_puntos()

    if jugador == USUARIO:
        if envido_usuario > envido_compu:
            print(f"TENES {envido_usuario} DE ENVIDO Y LA COMPUTADORA TIENE {envido_compu}, GANASTE {puntos} PUNTOS")
            partida_actual['puntos']['usuario'] += puntos
        elif envido_compu > envido_usuario:
            print(
                f"TENES {envido_usuario} DE ENVIDO Y LA COMPUTADORA TIENE {envido_compu}, LA COMPUTADORA GANA {puntos} PUNTOS")
            partida_actual['puntos']['computadora'] += puntos
    elif jugador == COMPUTADORA:
        if envido_compu > envido_usuario:
            print(f"LA COMPUTADORA TIENE {envido_compu} DE ENVIDO Y VOS TENES {envido_usuario}, GANA {puntos} PUNTOS")
            partida_actual['puntos']['computadora'] += puntos
        elif envido_usuario > envido_compu:
            print(f"LA COMPUTADORA TIENE {envido_compu} DE ENVIDO Y VOS TENES {envido_usuario}, GANASTE {puntos} PUNTOS")
            partida_actual['puntos']['usuario'] += puntos
    return partida_actual


def calcular_puntos_envido():
    """
    Calcula los puntos que se obtienen al ganar él envido
    :return: puntos a sumar al ganador del envido
    """
    envido = get_current_hand()['envido']

    puntos_envido = 0

    if envido['rechazado_por'] is not None:
        puntos_envido = + envido['nivel']
    elif envido['activo']:
        # Calcular los puntos basándonos en el nivel del envido o algo por el estilo
        puntos_envido = + envido['nivel']

    return puntos_envido
