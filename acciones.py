from usuario import pedir_accion_usuario
from computadora import actuar_computadora
from envido import determinar_ganador_envido, calcular_puntos_por_ganar_envido
from utilidades import formatear_carta, noop, dev_print, player_color, Colores
from variables import get_current_game, get_current_hand, get_current_round, is_last_action_in_round, add_action, \
    USUARIO, \
    next_play_by, truco_rechazado_por, truco_cantado_por, envido_cantado_por, get_max_points, get_user_points, \
    get_computer_points


def jugar_carta(carta, jugador):
    """
    Funcion que se llama para jugar una carta, crea y devuelve una funcion que al ser llamada
    ejecuta la logica para jugar una carta.

    :param carta: Carta a jugar
    :param jugador: Jugador que juega la carta
    :return:
    """

    dev_print('Jugar Carta Builder')

    def _jugar_carta():
        mano_actual = get_current_hand()
        ronda_actual = get_current_round()

        dev_print('Jugar Carta Execution')

        if jugador == USUARIO:
            mano_actual['cartas_usuario'].remove(carta)
            ronda_actual.update({
                "carta_usuario": carta,
            })
        else:
            mano_actual['cartas_computadora'].remove(carta)
            ronda_actual.update({
                "carta_computadora": carta,
            })

        print(f"{player_color[jugador]}{jugador.capitalize()}{Colores.RESET}: Juego {formatear_carta(carta)}")

        if is_last_action_in_round():
            dev_print('LAST ACTION IN ROUND')
            # add_action(determinar_ganador_ronda)
        else:
            add_action(pedir_accion_usuario if next_play_by() == USUARIO else actuar_computadora)

        return noop

    return _jugar_carta


niveles_nombre_truco = {
    1: "Truco",
    2: "Retruco",
    3: "Vale Cuatro"
}


def cantar_truco(jugador, nivel):
    """
    Funcion que se llama para cantar truco, crea y devuelve una funcion que al ser llamada
    ejecuta la logica para cantar el truco.

    :param jugador: Jugador que va a cantar el truco
    :return:
    """

    dev_print('Cantar Truco Builder')

    def _cantar_truco():
        mano_actual = get_current_hand()

        truco = mano_actual['truco']

        # Si el truco ya fue rechazado, no permitimos que se cante
        if truco_rechazado_por() is not None:
            print(
                f"{Colores.RED}No se puede cantar {niveles_nombre_truco[nivel]}, ya fue rechazado!{Colores.RESET}")

            add_action(pedir_accion_usuario if next_play_by() == USUARIO else actuar_computadora)

            return noop

        # Si se trata de cantar el mismo nivel de truco que ya fue cantado, no permitimos que se cante
        if truco['nivel'] == nivel:
            print(
                f"{Colores.RED}No se puede volver a cantar {niveles_nombre_truco[nivel]} en la misma mano! {Colores.RESET}")

            add_action(pedir_accion_usuario if next_play_by() == USUARIO else actuar_computadora)

            return noop

        if truco['nivel'] - nivel != -1:
            print(
                f"{Colores.RED}No se puede cantar {niveles_nombre_truco[nivel]}, ya que el nivel de truco anterior no fue cantado!{Colores.RESET}")

            add_action(pedir_accion_usuario if next_play_by() == USUARIO else actuar_computadora)

            return noop

        if truco_cantado_por() is not None:
            if truco_cantado_por() == jugador:
                print(
                    f"{Colores.RED}No se puede cantar {niveles_nombre_truco[nivel]}, ya que el nivel de truco anterior fue cantado por el mismo jugador!{Colores.RESET}")

                add_action(pedir_accion_usuario if next_play_by() == USUARIO else actuar_computadora)

                return noop

        truco.update({
            "activo": False,
            "cantado_por": jugador,
            "nivel": nivel,
            "esperando": True
        })

        dev_print('Cantar Truco Execution')

        print(f"{player_color[jugador]}{jugador.capitalize()}{Colores.RESET}: {niveles_nombre_truco[nivel]}!")

        add_action(pedir_accion_usuario if next_play_by() == USUARIO else actuar_computadora)

        return noop

    return _cantar_truco


def aceptar_truco(jugador):
    """
    Funcion que se llama para aceptar el truco, crea y devuelve una funcion que al ser llamada
    ejecuta la logica para aceptar el truco.

    :param jugador: Jugador que va a aceptar el truco
    :return:
    """

    dev_print('Aceptar Truco Builder')

    def _aceptar_truco():
        mano_actual = get_current_hand()
        mano_actual['truco'].update({
            "activo": True,
            "esperando": False,
        })

        dev_print('Aceptar Truco Execution')

        print(
            f"{player_color[jugador]}{jugador.capitalize()}{Colores.RESET}: Quiero! ({niveles_nombre_truco[mano_actual['truco']['nivel']]})")

        if is_last_action_in_round():
            dev_print('LAST ACTION IN TRUCO')
            # add_action(determinar_ganador_ronda)
        else:
            dev_print('NOT LAST ACTION IN TRUCO')
            add_action(pedir_accion_usuario if next_play_by() == USUARIO else actuar_computadora)

        return noop

    return _aceptar_truco


def rechazar_truco(jugador):
    """
    Funcion que se llama para rechazar el truco, crea y devuelve una funcion que al ser llamada
    ejecuta la logica para rechazar el truco.

    :param jugador: Jugador que va a rechazar el truco
    :return:
    """

    dev_print('Rechazar Truco Builder')

    def _rechazar_truco():
        mano_actual = get_current_hand()
        mano_actual['truco'].update({
            "activo": False,
            "rechazado_por": jugador,
            "esperando": False
        })

        dev_print('Rechazar Truco Execution')

        print(
            f"{player_color[jugador]}{jugador.capitalize()}{Colores.RESET}: No quiero! ({niveles_nombre_truco[mano_actual['truco']['nivel']]})")

        return noop

    return _rechazar_truco


envidos_a_nombres = {
    'envido': 'Envido',
    'envido_2': 'Envido (x 2)',
    'real_envido': 'Real Envido',
    'falta_envido': 'Falta Envido'
}


def cantar_envido(jugador, que_envido):
    """
    Funcion que se llama para cantar envido, crea y devuelve una funcion que al ser llamada

    :param jugador: Jugador que va a cantar el envido
    :return:
    """

    dev_print('Cantar Envido Builder')

    def _cantar_envido():
        mano_actual = get_current_hand()
        envido = mano_actual['envido']

        # Si ya se cantó ese envido, no se puede volver a cantar.
        # Aunque técnicamente él envido envido, si es un doble canto de envido, lo
        # manejamos como un envido separado para evitar dificultades.
        if que_envido in envido['cantados']:
            print(
                f"{Colores.RED}No se puede volver a cantar {envidos_a_nombres[que_envido]} en la misma mano!{Colores.RESET}")

            add_action(pedir_accion_usuario if next_play_by() == USUARIO else actuar_computadora)

            return noop

        # Un mismo jugador no puede cantar dos envidos seguidos.
        if jugador == envido_cantado_por():
            print(
                f"{Colores.RED}No puede cantar el siguiente envido el mismo jugador que canto el anterior!{Colores.RESET}")

            add_action(pedir_accion_usuario if next_play_by() == USUARIO else actuar_computadora)

            return noop

        # Si no se canto "envido" o se canto cualquier otro envido ademas de ese, no se puede cantar "envido_2"
        if que_envido == 'envido_2' and envido['cantados'] != ['envido']:
            print(
                f"{Colores.RED}Solo se puede cantar {envidos_a_nombres[que_envido]} si se canto Envido y ningún otro nivel!{Colores.RESET}")

            add_action(pedir_accion_usuario if next_play_by() == USUARIO else actuar_computadora)

            return noop

        envido.update({
            "activo": False,
            "cantado_por": jugador,
            "puntos": 1,
            "esperando": True
        })
        envido['cantados'].append(que_envido)

        dev_print('Cantar Envido Execution')

        print(f"{player_color[jugador]}{jugador.capitalize()}{Colores.RESET}: {envidos_a_nombres[que_envido]}!")

        add_action(pedir_accion_usuario if next_play_by() == USUARIO else actuar_computadora)

        return noop

    return _cantar_envido


def aceptar_envido(jugador):
    """
    Funcion que se llama para aceptar el envido, crea y devuelve una funcion que al ser llamada
    ejecuta la logica para aceptar el envido.

    :param jugador: Jugador que va a aceptar el envido
    :return:
    """

    dev_print('Aceptar Envido Builder')

    def _aceptar_envido():
        mano_actual = get_current_hand()

        cantados = mano_actual['envido']['cantados']

        mano_actual['envido'].update({
            "activo": True,
            "esperando": False,
        })

        add_action(sumar_puntos_envido(jugador))

        dev_print('Aceptar Envido Execution')

        print(
            f"{player_color[jugador]}{jugador.capitalize()}{Colores.RESET}: Quiero! ({envidos_a_nombres[cantados[-1]]})")

        # aca falta agregar la accion para determinar el ganador del envido, y sumar los puntos correspondientes
        # add_action()
        add_action(pedir_accion_usuario if next_play_by() == USUARIO else actuar_computadora)

        return noop

    return _aceptar_envido


def rechazar_envido(jugador):
    """
    Funcion que se llama para rechazar el envido, crea y devuelve una funcion que al ser llamada
    ejecuta la logica para rechazar el envido.

    :param jugador: Jugador que va a rechazar el envido
    :return:
    """

    dev_print('Rechazar Envido Builder')

    def _rechazar_envido():
        mano_actual = get_current_hand()

        mano_actual['envido'].update({
            "activo": False,
            "rechazado_por": jugador,
            "esperando": False
        })

        cantados = mano_actual['envido']['cantados']

        add_action(sumar_puntos_envido(jugador))

        dev_print('Rechazar Envido Execution')

        print(
            f"{player_color[jugador]}{jugador.capitalize()}{Colores.RESET}: No quiero! ({envidos_a_nombres[cantados[-1]]})")

        # Aca falta agregar la accion para calcular los puntos en base a que nivel de envido estemos,
        # y que se sumen a los puntos del jugador que lo había cantado.
        # add_action()

        # Después se deberia llamar a la accion para pedir la proxima accion del jugador o computadora
        add_action(pedir_accion_usuario if next_play_by() == USUARIO else actuar_computadora)

        return noop

    return _rechazar_envido


def sumar_puntos_envido(jugador):
    def _sumar_puntos():
        envido = get_current_hand()['envido']
        partida = get_current_game()

        puntos_a_sumar = calcular_puntos_por_ganar_envido()

        ganador_del_envido = determinar_ganador_envido()

        max_points = get_max_points()

        if ganador_del_envido == USUARIO:
            puntos_usuario = get_user_points()

            if puntos_usuario + puntos_a_sumar > max_points:
                puntos_a_sumar = max_points - puntos_usuario
        else:
            puntos_computadora = get_computer_points()

            if puntos_computadora + puntos_a_sumar > max_points:
                puntos_a_sumar = max_points - puntos_computadora

        print(
            f"{player_color[ganador_del_envido]}{ganador_del_envido.capitalize()}{Colores.RESET} gana {puntos_a_sumar} puntos!")

        partida['puntos'][ganador_del_envido] += puntos_a_sumar

        return noop

    return _sumar_puntos
