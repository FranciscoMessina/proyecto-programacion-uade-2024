from utilidades import formatear_carta, pedir_eleccion


def pedir_accion_usuario(cartas, partida, numero_ronda):
    """
    Muestra al usuario la acciones disponibles y le pide que elija una de ellas

    :param cartas: cartas que tiene el jugador
    :param partida: estado actual de la partida
    :param numero_ronda:  numero de la ronda actual
    :return: valor de la accion que el jugador desea tomar
    """
    opciones = []
    for carta in cartas:
        # Por cada carta en su mano agregamos la opcion de jugarla.
        opciones.append([f"Jugar {formatear_carta(carta)}", {"carta": carta, "accion": "jugar_carta"}])

    if partida['mano_actual']['truco'].get('nivel') is None:
        # Si no se ha cantado truco aun, se le da la opcion de cantar truco
        opciones.append(["Cantar truco", {"accion": "cantar_truco"}])


    return pedir_eleccion(opciones)

def accion_usuario_envido(partida, puntos_envido):
    opciones = []
    print(f"Tenes {puntos_envido} de envido,")
    if partida['mano_actual']['rondas'][0]['ganador'] is None:
        # Si no se ha cantado truco aun, se le da la opcion de cantar truco
        opciones.append(["Cantar envido", {"accion": "cantar_envido"}])
        opciones.append(["No cantar envido", {"accion": "no_cantar_envido"}])

    return pedir_eleccion(opciones)