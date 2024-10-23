from envido import calcular_envido

from utilidades import formatear_carta, pedir_eleccion, Colores
from variables import get_current_hand, get_user_cards, is_first_round, USUARIO


def pedir_accion_usuario():
    """
    Muestra al usuario las acciones disponibles y le pide que elija una de ellas

    :return: la accion que se va a ejecutar
    """
    opciones = []

    mano_actual = get_current_hand()
    cartas = get_user_cards()

    if mano_actual['truco'].get('cantado_por') == "computadora" and mano_actual["truco"].get('nivel') == 0:
        # Si la computadora canta truco se le da la opcion al usuario de aceptar
        from acciones import aceptar_truco, rechazar_truco
        opciones.append(["Quiero", aceptar_truco(USUARIO)])
        opciones.append(["No quiero", rechazar_truco(USUARIO)])

    else:
        for carta in cartas:
            # Por cada carta en su mano agregamos la opcion de jugarla.
            from acciones import jugar_carta
            opciones.append([f"Jugar {formatear_carta(carta)}", jugar_carta(carta, USUARIO)])

    if mano_actual['truco'].get('activo') is False:
        # Si no se ha cantado truco aun, se le da la opcion de cantar truco
        from acciones import cantar_truco
        opciones.append(["Cantar truco", cantar_truco(USUARIO)])

    if is_first_round():
        puntos_envido = calcular_envido(cartas)
        print(f"Tenes {Colores.BOLD}{Colores.BLUE}{puntos_envido}{Colores.RESET} de envido")
        if mano_actual['envido'].get("activo") is False and mano_actual['envido'].get("cantado_por") is None:
            from acciones import cantar_envido
            opciones.append(["Cantar envido", cantar_envido(USUARIO)])

        if mano_actual['envido'].get("cantado_por") == "computadora":
            from acciones import aceptar_envido, rechazar_envido
            opciones.append(["Quiero", aceptar_envido(USUARIO)])

            opciones.append(["No quiero", rechazar_envido(USUARIO)])

    """    
    if partida['mano_actual']['truco'].get('nivel') == 1:
        opciones.append(["Cantar retruco", {"accion": "cantar_retruco"}])

    if partida['mano_actual']['truco'].get('nivel') == 2:
        opciones.append(["Cantar vale 4", {"accion": "cantar_vale_4"}])
    """
    return pedir_eleccion(opciones)
