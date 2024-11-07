from random import choice

from utilidades import dev_print

# En este archivo definimos variables, y funciones de utilidad para
# acceder a ellas desde diferentes partes del código.


# Guarda toda la información respecto a la partida actual.
partida_actual: dict = {}

USUARIO = 'usuario'
COMPUTADORA = 'computadora'


def init_game(max_points):
    """
    Función utlizada para inicializar la partida.
    Debe ser llamada antes de cualquier paso del juego.
    Configura los puntos maximos de la partida a jugar.

    :param max_points: Puntos maximos para la partida a iniciar.
    :return:
    """
    global partida_actual
    partida_actual = {
        "puntos_maximos": max_points,
        "puntos": {
            "usuario": 0,
            "computadora": 0
        },
        "manos_jugadas": 0,
        "siguiente_en_empezar": choice(['computadora','usuario']),
        "mano_actual": {}
    }

    return partida_actual

def reset_game():
    """
    Resetea la partida actual.
    :return:
    """
    global partida_actual
    partida_actual = {}

    return partida_actual

def init_hand(user_cards, computer_cards):
    """
    Inicializa una nueva mano en la partida actual.
    Debe ser llamado previo al inicio de cada mano.

    :param user_cards: Mano de cartas del jugador
    :param computer_cards: Mano de cartas de la computadora
    :return:
    """
    partida_actual['mano_actual'] = {
        "acciones": [],
        "cartas_usuario": user_cards,
        "cartas_computadora": computer_cards,
        "rondas": [],
        "truco": {
            "activo": False,
            "cantando_por": None,
            "rechazado_por": None,
            "esperando": False,
            "nivel": 0
        },
        "envido": {
            "activo": False,
            "cantado_por": None,
            "rechazado_por": None,
            "esperando": False,
            "puntos": 0,
            "envido_envido": False,
            "envido_envido_cantado_por": None,
            "envido_envido_rechazado_por": None,
            "envido_envido_esperando": False,
            "real_envido": False,
            "real_envido_cantado_por": None,
            "real_envido_rechazado_por": None,
            "real_envido_esperando": False,
            "falta_envido": False,
            "falta_envido_cantado_por": None,
            "falta_envido_rechazado_por": None,
            "falta_envido_esperando": False
        }
    }

    return partida_actual['mano_actual']


def get_current_game():
    """
    Devuelve la partida actual y verifica que la misma haya sido inicializada

    :return: partida_actual
    """
    if partida_actual == {}:
        raise Exception(
            "No hay partida actual, por favor recorda inicializar una partida antes de intentar acceder a la misma")

    return partida_actual


def quien_es_mano():
    return get_current_game()['siguiente_en_empezar']

def truco_needs_answer():
    truco = get_current_hand()['truco']

    if truco['rechazado_por'] is not None:
        return False

    return truco['esperando']


def envido_needs_answer():
    envido = get_current_hand()['envido']

    if envido['rechazado_por'] is not None:
        return False

    return envido['esperando']

def envido_envido_needs_answer():
    envido = get_current_hand()['envido']

    if envido['envido_envido_rechazado_por'] is not None:
        return False

    return envido['envido_envido_esperando']

def real_envido_needs_answer():
    envido = get_current_hand()['envido']

    if envido['real_envido_rechazado_por'] is not None:
        return False

    return envido['real_envido_esperando']

def falta_envido_needs_answer():
    envido = get_current_hand()['envido']

    if envido['falta_envido_rechazado_por'] is not None:
        return False

    return envido['falta_envido_esperando']

def envido_rechazado_por():
    return get_current_hand()['envido']['rechazado_por']

def envido_envido_rechazado_por():
    return get_current_hand()['envido']['envido_envido_rechazado_por']

def real_envido_rechazado_por():
    return get_current_hand()['envido']['real_envido_rechazado_por']

def falta_envido_rechazado_por():
    return get_current_hand()['envido']['falta_envido_rechazado_por']

def envido_cantado_por():
    return get_current_hand()['envido']['cantado_por']

def envido_envido_cantado_por():
    return get_current_hand()['envido']['envido_envido_cantado_por']

def real_envido_cantado_por():
    return get_current_hand()['envido']['real_envido_cantado_por']

def falta_envido_cantado_por():
    return get_current_hand()['envido']['falta_envido_cantado_por']

def envido_puntos():
    return get_current_hand()['envido']['puntos']

def next_play_by():
    """
    Funcion para determinar quien tiene que ser el proximo jugador en actuar en diferentes casos.
    :return:
    """
    current_hand = get_current_hand()


    if truco_needs_answer():
        dev_print(f"TRUCO NECESITA RESPUESTA CANTADO POR {current_hand['truco']['cantado_por']}")
        return USUARIO if current_hand['truco']['cantado_por'] == COMPUTADORA else COMPUTADORA

    if envido_needs_answer():
        dev_print(f"ENVIDO NECESITA RESPUESTA CANTADO POR {current_hand['envido']['cantado_por']}")
        return USUARIO if current_hand['envido']['cantado_por'] == COMPUTADORA else COMPUTADORA

    dev_print(f"NEXT PLAY BY")

    current_round = get_current_round()
    dev_print(current_round)

    carta_usuario = current_round.get('carta_usuario')
    carta_computadora = current_round.get('carta_computadora')

    dev_print(f"Carta Usuario: {carta_usuario}")
    dev_print(f"Carta Computadora: {carta_computadora}")

    if carta_usuario is None and carta_computadora is None:
        dev_print(f"NO HAY CARTAS JUGADAS")
        return get_current_game()['siguiente_en_empezar']
    elif carta_usuario is None:
        return USUARIO
    else:
        return COMPUTADORA





def get_current_hand():
    return get_current_game()['mano_actual']


def get_user_points():
    return get_current_game()['puntos']['usuario']


def get_computer_points():
    return get_current_game()['puntos']['computadora']


def get_max_points():
    return get_current_game()['puntos_maximos']


def get_user_cards():
    return get_current_hand()['cartas_usuario']


def get_computer_cards():
    return get_current_hand()['cartas_computadora']


def is_first_round():
    return len(get_current_hand()['rondas']) == 1


def is_last_action_in_round():
    return (get_current_round().get('carta_usuario') is not None and get_current_round().get(
        'carta_computadora') is not None)


def add_action(action):
    get_current_hand()['acciones'].append(action)


def get_current_round():
    return get_current_hand()['rondas'][-1]


def get_previous_round():
    return get_current_hand()['rondas'][-2] if len(get_current_hand()['rondas']) > 1 else {}
