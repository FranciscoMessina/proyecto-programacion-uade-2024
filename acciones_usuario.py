from utilidades import formatear_carta, pedir_eleccion
from guardado import guardar_partida

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

    if partida['mano_actual']['guardado'].get('nivel') is None:
            # Si no se ha cantado truco aun, se le da la opcion de cantar truco
            opciones.append(["Guardar Partida", {"accion":"guardar_partida"}])




    return pedir_eleccion(opciones)
