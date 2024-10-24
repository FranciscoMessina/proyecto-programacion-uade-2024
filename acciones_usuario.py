from envido import calcular_envido

from utilidades import formatear_carta, pedir_eleccion, Colores, dev_print
from variables import get_current_hand, get_user_cards, is_first_round, USUARIO, envido_needs_answer, truco_needs_answer


def pedir_accion_usuario():
    """
    Muestra al usuario las acciones disponibles y le pide que elija una de ellas

    :return: la accion que se va a ejecutar
    """
    dev_print("Inicio Pedir Accion Usuario")

    opciones = []

    mano_actual = get_current_hand()
    cartas = get_user_cards()

    if envido_needs_answer():
        dev_print('AU- Responder a envido')
        from acciones import aceptar_envido, rechazar_envido
        opciones.append(["Quiero", aceptar_envido(USUARIO)])
        opciones.append(["No quiero", rechazar_envido(USUARIO)])

    elif truco_needs_answer():
        dev_print('AU- Responder a truco')
        from acciones import aceptar_truco, rechazar_truco
        opciones.append(["Quiero", aceptar_truco(USUARIO)])
        opciones.append(["No quiero", rechazar_truco(USUARIO)])

    else:
        dev_print('AU- Opciones normales')
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

    return pedir_eleccion(opciones)
