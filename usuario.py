from envido import calcular_envido, envidos_cantables_despues

from utilidades import formatear_carta, pedir_eleccion, Colores, dev_print, instrucciones
from variables import get_current_hand, get_user_cards, is_first_round, \
    USUARIO, COMPUTADORA, envido_needs_answer, truco_needs_answer, envido_rechazado_por, envido_cantado_por


def pedir_accion_usuario():
    """
    Muestra al usuario las acciones disponibles y le pide que elija una de ellas

    :return: la accion que se va a ejecutar
    """
    # Por qué están todos los import adentro de la funcion? Porque si los importamos en el inicio del archivo, tenemos un problema con
    # dependencias circulares, como en los archivos de acciones.py se importan funciones de este archivo, y en este se importan funciones de acciones.py
    # entonces si importamos al inicio del archivo, se importan antes de que se definan las funciones, y da error.
    # Pero al importarlo dentro de la funcion (asumo que), se importan recien cuando se ejecuta la funcion, y ahi ya estan definidas las otras funciones
    from acciones import cantar_truco, cantar_envido, aceptar_truco, \
        rechazar_truco, aceptar_envido, rechazar_envido, jugar_carta, envidos_a_nombres, niveles_nombre_truco
    dev_print("Inicio Pedir Accion Usuario")

    opciones = []

    mano_actual = get_current_hand()
    cartas = get_user_cards()
    puntos_envido = calcular_envido(cartas)

    if envido_needs_answer():

        cantados = mano_actual['envido']['cantados']

        print(f"Tenes {Colores.BOLD}{Colores.BLUE}{puntos_envido}{Colores.RESET} de envido\n")

        print(f"La {Colores.RED}COMPUTADORA{Colores.RESET} canto {envidos_a_nombres[cantados[-1]]}")

        dev_print('AU- Responder a envido')

        opciones.append(["Quiero", aceptar_envido(USUARIO)])
        opciones.append(["No quiero", rechazar_envido(USUARIO)])

        for envido in envidos_cantables_despues[cantados[-1]]:
            opciones.append([f"Cantar {envidos_a_nombres[envido]}", cantar_envido(USUARIO, envido)])


    elif truco_needs_answer():
        dev_print('AU- Responder a Truco')

        print(f"La {Colores.RED}COMPUTADORA{Colores.RESET} canto {niveles_nombre_truco[mano_actual['truco']['nivel']]}")

        opciones.append(["Quiero", aceptar_truco(USUARIO)])
        opciones.append(["No quiero", rechazar_truco(USUARIO)])
        if envido_cantado_por() is None and envido_rechazado_por() is None and is_first_round() and \
                mano_actual['truco']['nivel'] == 1:
            opciones.append(["El envido va primero", cantar_envido(USUARIO, 'envido')])

        if mano_actual['truco'].get('nivel') == 1:
            opciones.append(["Cantar Retruco", cantar_truco(USUARIO, 2)])
        elif mano_actual['truco'].get('nivel') == 2:
            opciones.append(["Cantar Vale Cuatro", cantar_truco(USUARIO, 3)])

    else:
        dev_print('AU- Opciones normales')
        opciones.append('------ Cartas ------')
        for carta in cartas:
            # Por cada carta en su mano agregamos la opcion de jugarla.
            opciones.append([f"Jugar {formatear_carta(carta)}", jugar_carta(carta, USUARIO)])

        opciones.append('----- Acciones -----')
        if mano_actual['truco'].get('activo') is False:
            # Si no se ha cantado truco aun, se le da la opcion de cantar truco
            if mano_actual['truco'].get('nivel') == 0:
                opciones.append(["Cantar truco", cantar_truco(USUARIO, 1)])
        if mano_actual['truco'].get('activo') is True:
            if mano_actual['truco'].get('nivel') == 1 and mano_actual['truco'].get('cantado_por') == COMPUTADORA:
                opciones.append(["Cantar Retruco", cantar_truco(USUARIO, 2)])
            elif mano_actual['truco'].get('nivel') == 2 and mano_actual['truco'].get('cantado_por') == COMPUTADORA:
                opciones.append(["Cantar Vale cuatro", cantar_truco(USUARIO, 3)])

        if is_first_round() and envido_rechazado_por() is None and envido_cantado_por() is None:
            print(f"Tenes {Colores.BOLD}{Colores.BLUE}{puntos_envido}{Colores.RESET} de envido \n")

            opciones.append(["Cantar envido", cantar_envido(USUARIO, 'envido')])
            opciones.append(["Cantar real envido", cantar_envido(USUARIO, 'real_envido')])
            opciones.append(["Cantar falta envido", cantar_envido(USUARIO, 'falta_envido')])

    return pedir_eleccion(opciones)


def mostrar_mano_usuario():
    """
    Muestra las cartas del usuario en consola
    :return:
    """
    cartas = get_user_cards()

    puntos_envido = calcular_envido(cartas)
    print(" Tu mano ".center(50, '-'))
    print("")
    for i, carta in enumerate(cartas):
        print(f" {formatear_carta(carta)}", end=', ')

    if len(cartas) == 3:
        print(f"\n Tenés {Colores.BOLD}{Colores.BLUE}{puntos_envido}{Colores.RESET} puntos de envido")
    print('')
    print("".center(50, '-'))
    print('\n')
