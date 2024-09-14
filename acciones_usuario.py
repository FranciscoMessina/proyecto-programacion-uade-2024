from utilidades import formatear_carta, pedir_eleccion


def pedir_accion_usuario(cartas, partida, numero_ronda):
    opciones = []
    for carta in cartas:
        opciones.append([f"Jugar {formatear_carta(carta)}", {"carta": carta, "accion": "jugar_carta"}])

    if partida['mano_actual']['truco'] is None:
        opciones.append(["Cantar truco", {"accion": "cantar_truco"}])

    return pedir_eleccion(opciones)
