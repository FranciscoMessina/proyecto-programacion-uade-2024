from envido import calcular_envido

from utilidades import formatear_carta, pedir_eleccion, Colores, dev_print
from variables import envido_cantado_por, envido_envido_needs_answer, falta_envido_cantado_por, falta_envido_needs_answer, \
get_current_hand, get_user_cards, is_first_round, USUARIO, COMPUTADORA, envido_needs_answer, real_envido_cantado_por, real_envido_needs_answer, truco_needs_answer


def pedir_accion_usuario():

    """
    Muestra al usuario las acciones disponibles y le pide que elija una de ellas

    :return: la accion que se va a ejecutar
    """
    # Por que estan todos los import adentro de la funcion? Porque si los importamos en el inicio del archivo, tenemos un problema con
    # dependencias circulares, como en los archivos de acciones.py se importan funciones de este archivo, y en este se importan funciones de acciones.py
    # entonces si importamos al inicio del archivo, se importan antes de que se definan las funciones, y da error.
    # Pero al importarlo dentro de la funcion (asumo que), se importan recien cuando se ejecuta la funcion, y ahi ya estan definidas las otras funciones
    from acciones import cantar_truco, cantar_envido, cantar_real_envido, cantar_falta_envido, aceptar_truco, rechazar_truco, aceptar_envido, \
        rechazar_envido, jugar_carta, aceptar_real_envido, aceptar_envido_envido, \
        rechazar_envido_envido, rechazar_real_envido, cantar_envido_envido, aceptar_falta_envido, rechazar_falta_envido
    dev_print("Inicio Pedir Accion Usuario")

    opciones = []

    mano_actual = get_current_hand()
    cartas = get_user_cards()
    puntos_envido = calcular_envido(cartas)

    if falta_envido_needs_answer():
        print(f"Tenes {Colores.BOLD}{Colores.BLUE}{puntos_envido}{Colores.RESET} de envido")
        
        dev_print('AU- Responder a falta envido')
        
        opciones.append(["Quiero", aceptar_falta_envido(USUARIO)])
        opciones.append(["No quiero", rechazar_falta_envido(USUARIO)])

    elif real_envido_needs_answer():
        print(f"Tenes {Colores.BOLD}{Colores.BLUE}{puntos_envido}{Colores.RESET} de envido")

        dev_print('AU- Responder a real envido')

        opciones.append(["Quiero", aceptar_real_envido(USUARIO)])
        opciones.append(["No quiero", rechazar_real_envido(USUARIO)])
        opciones.append(["Cantar falta envido", cantar_falta_envido(USUARIO)])

    elif envido_envido_needs_answer():
        print(f"Tenes {Colores.BOLD}{Colores.BLUE}{puntos_envido}{Colores.RESET} de envido")

        dev_print('AU- Responder a envido envido')

        opciones.append(["Quiero", aceptar_envido_envido(USUARIO)])
        opciones.append(["No quiero", rechazar_envido_envido(USUARIO)])
        opciones.append(["Cantar real envido", cantar_real_envido(USUARIO)])

    elif envido_needs_answer():
        print(f"Tenes {Colores.BOLD}{Colores.BLUE}{puntos_envido}{Colores.RESET} de envido")

        dev_print('AU- Responder a envido')

        opciones.append(["Quiero", aceptar_envido(USUARIO)])
        opciones.append(["No quiero", rechazar_envido(USUARIO)])
        opciones.append(["Cantar envido envido", cantar_envido_envido(USUARIO)])
        opciones.append(["Cantar real envido", cantar_real_envido(USUARIO)])
        opciones.append(["Cantar falta envido", cantar_falta_envido(USUARIO)])

    elif truco_needs_answer():
        dev_print('AU- Responder a truco')

        opciones.append(["Quiero", aceptar_truco(USUARIO)])
        opciones.append(["No quiero", rechazar_truco(USUARIO)])

        if mano_actual['truco'].get('nivel') == 1:
            opciones.append(["Cantar Retruco", cantar_truco(USUARIO, 2)])
        elif mano_actual['truco'].get('nivel') == 2:
            opciones.append(["Cantar Vale cuatro", cantar_truco(USUARIO, 3)])

    else:
        dev_print('AU- Opciones normales')

        for carta in cartas:
            # Por cada carta en su mano agregamos la opcion de jugarla.
            opciones.append([f"Jugar {formatear_carta(carta)}", jugar_carta(carta, USUARIO)])
        if mano_actual['truco'].get('activo') is False:
            # Si no se ha cantado truco aun, se le da la opcion de cantar truco
            if mano_actual['truco'].get('nivel') == 0:
                opciones.append(["Cantar truco", cantar_truco(USUARIO, 1)])
        if mano_actual['truco'].get('activo') is True:
            if mano_actual['truco'].get('nivel') == 1 and mano_actual['truco'].get('cantado_por') == COMPUTADORA:
                opciones.append(["Cantar Retruco", cantar_truco(USUARIO, 2)])
            elif mano_actual['truco'].get('nivel') == 2 and mano_actual['truco'].get('cantado_por') == COMPUTADORA:
                opciones.append(["Cantar Vale cuatro", cantar_truco(USUARIO, 3)])

        if is_first_round():
            print(f"Tenes {Colores.BOLD}{Colores.BLUE}{puntos_envido}{Colores.RESET} de envido")

            if mano_actual['envido'].get("activo") is False and envido_cantado_por() is None and \
            real_envido_cantado_por() is None and falta_envido_cantado_por() is None:


                opciones.append(["Cantar envido", cantar_envido(USUARIO)])
                opciones.append(["Cantar real envido", cantar_real_envido(USUARIO)])
                opciones.append(["Cantar falta envido", cantar_falta_envido(USUARIO)])

    return pedir_eleccion(opciones)


def mostrar_mano_usuario():
    """
    Muestra las cartas del usuario en consola
    :return:
    """
    cartas = get_user_cards()

    puntos_envido = calcular_envido(cartas)
    print("Tu mano".center(50, '-'))
    for i, carta in enumerate(cartas):
        print(f" {formatear_carta(carta)}", end=', ')

    print(f"\n Tenés {Colores.BOLD}{Colores.BLUE}{puntos_envido}{Colores.RESET} puntos de envido")
    print("".center(50, '-'))
    print('\n')
