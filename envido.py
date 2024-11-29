from mazo import obtener_numero
from utilidades import Colores, player_color
from variables import COMPUTADORA, USUARIO, get_computer_cards, get_current_hand, get_current_game, \
    get_current_round, get_user_cards, quien_es_mano


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


def determinar_ganador_envido():
    #   Si el envido fue rechazado el jugador que lo canto gana automáticamente el último nivel cantado
    if get_current_hand()['envido']['rechazado_por'] is not None:
        return USUARIO if get_current_hand()['envido']['rechazado_por'] == COMPUTADORA else COMPUTADORA

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

    print(" Envido ".center(60, '-'))
    print(f"{Colores.GREEN}Usuario{Colores.RESET}: {envido_usuario}")
    print(f"{Colores.RED}Computadora{Colores.RESET}: {envido_compu}")
    print("".center(60, '-'))

    if envido_usuario == envido_compu:
        print(
            f'Gana {player_color[quien_es_mano()]}{quien_es_mano().upper()}, por ser mano.')
        # Si los puntos de envido son iguales, gana el jugador que es mano.
        return quien_es_mano()

    # if jugador == USUARIO:
    if envido_usuario > envido_compu:
        print(f'Gana {Colores.GREEN}Usuario{Colores.RESET}!')

        return USUARIO
    else:
        print(f'Gana {Colores.RED}Computadora{Colores.RESET}!')

        return COMPUTADORA


puntos_por_envido = {
    'envido': 2,
    'envido_2': 2,
    'real_envido': 3,
}

envidos_cantables_despues = {
    "envido": ['envido_2', "real_envido", "falta_envido"],
    "envido_2": ["real_envido", "falta_envido"],
    "real_envido": ["falta_envido"],
    "falta_envido": []
}


def calcular_puntos_por_envido():
    """
    Calcula los puntos que se obtienen al ganar él envido
    :return: puntos a sumar al ganador del envido
    """
    envido = get_current_hand()['envido']

    cantados = envido['cantados']

    puntos_a_sumar = 0

    print(cantados)

    if envido['rechazado_por'] is not None:
        # Caso de que se haya rechazado alguno de los envidos
        # Aca sacamos el último elemento del array de cantado, que es el que se rechazó
        cantados.pop()

        print(cantados)

        # y ahora calculamos los puntos que sumarian todos los otros que fueron sabemos que fueron aceptados.
        for cantado in cantados:
            if cantado in puntos_por_envido:
                puntos_a_sumar += puntos_por_envido[cantado]




    else:
        for cantado in cantados:
            if cantado in puntos_por_envido:
                puntos_a_sumar += puntos_por_envido[cantado]

        if 'falta_envido' in cantados:
            # Calcular puntos correspondientes para el falta envido
            puntos_a_sumar = 30

    # Si en el calculo de los puntos por alguna razon quedo en 0, es porque solo se canto envido y fue rechazado,
    # en ese caso simplemente devolvemos 1 y estamos.
    return puntos_a_sumar if puntos_a_sumar > 0 else 1
