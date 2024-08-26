def calcular_envido(mano):
    palos = {
        'espada': [],
        'basto': [],
        'oro': [],
        'copa': []
    }
    for carta in mano:
        palos[carta['palo']].append(carta)

    max_envido = 0

    for cartas in palos.values():
        if len(cartas) > 1:
            valores = [carta['valor'] if carta['valor'] <= 7 else 0 for carta in cartas]
            print(valores)
            envido = 20 + sum(sorted(valores, reverse=True)[:2])
            max_envido = max(max_envido, envido)
        elif len(cartas) == 1:
            valor = cartas[0]['valor']
            if valor > 7:
                valor = 0
            max_envido = max(max_envido, valor)

    return max_envido


