from mazo import obtener_numero


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
            # Si hay mas de una carta de un mismo palo, se calcula el envido, tomando las dos cartas con mayor valor y se le suman 20 puntos
            # Armamos una lista por compresion, con los numeros de las cartas, si el numero es mayor a 7, se toma como 0
            valores = [obtener_numero(carta) if obtener_numero(carta) <= 7 else 0 for carta in cartas]
            # Ordenamos la lista en reversa y tomamos los dos primeros valores
            envido = 20 + sum(sorted(valores, reverse=True)[:2])
            # Comparamos el nuevo envido calculado con el previo maximo envido. Y guardamos el mayor valor.
            max_envido = max(max_envido, envido)
        elif len(cartas) == 1:
            # En este caso solo hay una carta de un palo, se toma el valor de la carta y si es mayor a 7, se toma como 0
            valor = obtener_numero(cartas[0])
            if valor > 7:
                valor = 0

            # Comparamos el nuevo envido calculado con el previo maximo envido. Y guardamos el mayor valor.
            max_envido = max(max_envido, valor)

    return max_envido
