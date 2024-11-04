from acciones_usuario import pedir_accion_usuario
from computadora import actuar_computadora
from ronda import determinar_ganador_ronda
from envido import envido
from utilidades import formatear_carta, noop, dev_print
from variables import envido_cantado_por, envido_envido_cantado_por, envido_envido_rechazado_por, envido_puntos, envido_rechazado_por, falta_envido_cantado_por, falta_envido_rechazado_por, get_computer_cards, get_computer_points, get_current_game, get_current_hand, get_current_round, get_user_cards, is_last_action_in_round, add_action, USUARIO, COMPUTADORA, real_envido_cantado_por, real_envido_rechazado_por


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

        print(f"{jugador.capitalize()} jugo {formatear_carta(carta)}")

        if is_last_action_in_round():
            dev_print('LAST ACTION IN ROUND')
            add_action(determinar_ganador_ronda)
        else:
            add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

        return noop

    return _jugar_carta


def cantar_truco(jugador, nivel):
    """
    Funcion que se llama para cantar truco, crea y devuelve una funcion que al ser llamada
    ejecuta la logica para cantar el truco.

    :param jugador: Jugador que va a cantar el truco
    :return:
    """

    niveles_nombre = {
        1: "Truco",
        2: "Retruco",
        3: "Vale Cuatro"
    }

    dev_print('Cantar Truco Builder')

    def _cantar_truco():
        mano_actual = get_current_hand()
        mano_actual['truco'].update({
            "activo": False,
            "cantado_por": jugador,
            "nivel": nivel,
            "esperando": True
        })

        dev_print('Cantar Truco Execution')

        print(f"{jugador.capitalize()} canta {niveles_nombre[nivel]}")

        add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

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

        print(f"{jugador.capitalize()} quiere el truco")

        if is_last_action_in_round():
            dev_print('LAST ACTION IN TRUCO')
            add_action(determinar_ganador_ronda)
        else:
            dev_print('NOT LAST ACTION IN TRUCO')
            add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

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

        print(f"{jugador.capitalize()} no quiere el truco")

        return noop

    return _rechazar_truco


def cantar_envido(jugador):
    """
    Funcion que se llama para cantar envido, crea y devuelve una funcion que al ser llamada

    :param jugador: Jugador que va a cantar el envido
    :return:
    """

    dev_print('Cantar Envido Builder')

    def _cantar_envido():
        mano_actual = get_current_hand()
        mano_actual['envido'].update({
            "activo": False,
            "cantado_por": jugador,
            "puntos": 1,
            "esperando": True
        })

        dev_print('Cantar Envido Execution')

        print(f"{jugador.capitalize()} canta envido")

        add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

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
        mano_actual['envido'].update({
            "activo": True,
            "esperando": False,
            "puntos": 2,
        })

        add_action(sumar_puntos_envido(jugador))

        dev_print('Aceptar Envido Execution')

        print(f"{jugador.capitalize()} acepta el envido")

        # aca falta agregar la accion para determinar el ganador del envido, y sumar los puntos correspondientes
        # add_action()
        add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

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

        add_action(sumar_puntos_envido(jugador))

        dev_print('Rechazar Envido Execution')

        print(f"{jugador.capitalize()} no quiere el envido")

        # aca falta agregar la accion para calcular los puntos en base a que nivel de envido estemos,
        # y que se sumen a los puntos del jugador que lo habia cantado.
        # add_action()

        # Despues se deberia llamar a la accion para pedir la proxima accion del jugador o computadora
        add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

        return noop

    return _rechazar_envido

def cantar_envido_envido(jugador):

    def _cantar_envido_envido():

        mano_actual = get_current_hand()
        mano_actual['envido'].update({
            "envido_envido_cantado_por": jugador,
            "envido_envido_esperando": True,
            "puntos": 2,
            "esperando": False
        })

        print(f"{jugador.capitalize()} canta envido envido")

        add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

        return noop
    
    return _cantar_envido_envido

def aceptar_envido_envido(jugador):
    
    def _aceptar_envido_envido():
        mano_actual = get_current_hand()
        mano_actual['envido'].update({
            "envido_envido": True,
            "envido_envido_esperando": False,
            "puntos": 4
        })

        add_action(sumar_puntos_envido(jugador))

        print(f"{jugador.capitalize()} acepta el envido envido")

        add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

        return noop

    return _aceptar_envido_envido


def rechazar_envido_envido(jugador):
    
    def _rechazar_envido_envido():
        mano_actual = get_current_hand()
        mano_actual['envido'].update({
            "envido_envido_rechazado_por": jugador,
            "envido_envido_esperando": False
        })

        add_action(sumar_puntos_envido(jugador))


        print(f"{jugador.capitalize()} no quiere el envido envido")

        add_action(pedir_accion_usuario if jugador == COMPUTADORA else actuar_computadora)

        return noop

    return _rechazar_envido_envido

def sumar_puntos_envido(jugador):
  
    
    def _sumar_puntos():
        juego_actual = get_current_game()
        envido_rechazado = envido_rechazado_por()
        envido_envido_rechazado = envido_envido_rechazado_por()
        real_envido_rechazado = real_envido_rechazado_por()
        falta_envido_rechazado = falta_envido_rechazado_por()
        envido_cantado = envido_cantado_por()
        envido_envido_cantado = envido_envido_cantado_por()
        real_envido_cantado = real_envido_cantado_por()
        falta_envido_cantado = falta_envido_cantado_por()
        puntos = envido_puntos()
        #puntos_computadora = get_computer_points()
        #puntos_usuario = get_computer_points()

        if envido_envido_rechazado != None:
            if envido_envido_rechazado == jugador and jugador == USUARIO:
                juego_actual['puntos']['computadora'] += puntos
            else:
                juego_actual['puntos']['usuario'] += puntos
        elif envido_rechazado != None:
            if envido_rechazado == jugador and jugador == USUARIO:
                juego_actual['puntos']['computadora'] += puntos
            else:
                juego_actual['puntos']['usuario'] += puntos
        elif envido_envido_cantado == USUARIO:
            envido(USUARIO)
        elif envido_envido_cantado == COMPUTADORA:
            envido(COMPUTADORA)
        elif envido_cantado == USUARIO:
            envido(USUARIO)
        elif envido_cantado == COMPUTADORA:
            envido(COMPUTADORA)

        return noop
    
    return _sumar_puntos
