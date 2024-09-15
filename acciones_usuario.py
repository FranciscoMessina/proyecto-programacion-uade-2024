from utilidades import formatear_carta, pedir_eleccion

#Esta funcion proporciona una lista con las acciones que el jugador puede tomar
def pedir_accion_usuario(cartas, partida, numero_ronda):
    opciones = []
    for carta in cartas:
        opciones.append([f"Jugar {formatear_carta(carta)}", {"carta": carta, "accion": "jugar_carta"}])

    if partida['mano_actual']['truco'].get('nivel') is None:
        opciones.append(["Cantar truco", {"accion": "cantar_truco"}])

    return pedir_eleccion(opciones)
