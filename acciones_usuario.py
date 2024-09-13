from utilidades import formatear_carta, pedir_eleccion


def pedir_accion_usuario(cartas, partida, numero_ronda):
    opciones = []
    for carta in cartas:
        opciones.append([f"Jugar {formatear_carta(carta)}", {"carta": carta, "accion": "jugar_carta"}])

    return pedir_eleccion(opciones)
