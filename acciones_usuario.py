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

    if partida['mano_actual']['truco'].get('cantado_por') == "computadora" and partida["mano_actual"]["truco"].get('nivel') == 0:
        # Si la computadora canta truco se le da la opcion al usuario de aceptar
        opciones.append(["Quiero", {"accion": "aceptar_truco"}])
        opciones.append(["No quiero", {"accion": "rechazar_truco"}])

    else:
        for carta in cartas:
            # Por cada carta en su mano agregamos la opcion de jugarla.
            opciones.append([f"Jugar {formatear_carta(carta)}", {"carta": carta, "accion": "jugar_carta"}])

        if partida['mano_actual']['truco'].get('nivel') is None:
            # Si no se ha cantado truco aun, se le da la opcion de cantar truco
            opciones.append(["Cantar truco", {"accion": "cantar_truco"}])
        """    
        if partida['mano_actual']['truco'].get('nivel') == 1:
            opciones.append(["Cantar retruco", {"accion": "cantar_retruco"}])

        if partida['mano_actual']['truco'].get('nivel') == 2:
            opciones.append(["Cantar vale 4", {"accion": "cantar_vale_4"}])
        """
    return pedir_eleccion(opciones)

def accion_usuario_envido(partida, puntos_envido):
    opciones = []
    if partida['mano_actual']['envido'].get('cantado_por') is not None:
        print(f"Tenes {puntos_envido} de envido,")
        opciones.append(["Aceptar envido", {"accion": "aceptar_envido"}])
        opciones.append(["No aceptar envido", {"accion": "no_aceptar_envido"}])

    else:
        print(f"Tenes {puntos_envido} de envido,")
        opciones.append(["Cantar envido", {"accion": "cantar_envido"}])
        opciones.append(["No cantar envido", {"accion": "no_cantar_envido"}])


    return pedir_eleccion(opciones)

def accion_usuario_envido(partida, puntos_envido):
    opciones = []
    if partida['mano_actual']['envido'].get('cantado_por') is not None:
        print(f"Tenes {puntos_envido} de envido,")
        opciones.append(["Aceptar envido", {"accion": "aceptar_envido"}])
        opciones.append(["No aceptar envido", {"accion": "no_aceptar_envido"}])

    else:
        print(f"Tenes {puntos_envido} de envido,")
        opciones.append(["Cantar envido", {"accion": "cantar_envido"}])
        opciones.append(["No cantar envido", {"accion": "no_cantar_envido"}])

    return pedir_eleccion(opciones)