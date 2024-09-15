# Calcula el envido(aun no se usa)
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
    for carta in mano:
        palos[carta[1]].append(carta)

    max_envido = 0

    for cartas in palos.values():
        if len(cartas) > 1:
            valores = [carta[2] if carta[2] <= 7 else 0 for carta in cartas]
            envido = 20 + sum(sorted(valores, reverse=True)[:2])
            max_envido = max(max_envido, envido)
        elif len(cartas) == 1:
            valor = cartas[0][2]
            if valor > 7:
                valor = 0
            max_envido = max(max_envido, valor)

    return max_envido
