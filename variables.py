from random import choice

partida_actual: dict = {}

USUARIO = 'usuario'
COMPUTADORA = 'computadora'


def init_game(max_points):
    global partida_actual
    partida_actual = {
        "puntos_maximos": max_points,
        "puntos": {
            "usuario": 0,
            "computadora": 0
        },
        "manos_jugadas": 0,
        "siguiente_en_empezar": choice(["usuario"]),
        "mano_actual": {
            "acciones": [],
            "cartas_usuario": [],
            "cartas_computadora": [],
            "rondas": [],
            "truco": {
                "activo": False,
                "cantando_por": None,
                "rechazado_por": None,
                "nivel": 0
            },
            "envido": {
                "activo": False,
                "cantado_por": None,
                "rechazado_por": None,
                "nivel": 0
            }
        }
    }

    return partida_actual


def init_hand(user_cards, computer_cards):
    partida_actual['mano_actual'] = {
        "acciones": [],
        "cartas_usuario": user_cards,
        "cartas_computadora": computer_cards,
        "rondas": [],
        "truco": {
            "activo": False,
            "cantando_por": None,
            "rechazado_por": None,
            "nivel": 0
        },
        "envido": {
            "activo": False,
            "cantado_por": None,
            "rechazado_por": None,
            "nivel": 0
        }
    }

    return partida_actual['mano_actual']


def get_current_game():
    if partida_actual == {}:
        raise Exception(
            "No hay partida actual, por favor recorda inicializar una partida antes de intentar acceder a la misma")

    return partida_actual


def get_user_points():
    return partida_actual['puntos']['usuario']


def get_computer_points():
    return partida_actual['puntos']['computadora']


def get_max_points():
    return partida_actual['puntos_maximos']


def get_user_cards():
    return partida_actual['mano_actual']['cartas_usuario']


def get_computer_cards():
    return partida_actual['mano_actual']['cartas_computadora']


def get_current_hand():
    return partida_actual['mano_actual']


def is_first_round():
    return len(get_current_hand()['rondas']) == 1


def is_last_action_in_round():
    return (get_current_round().get('carta_usuario') is not None and get_current_round().get(
        'carta_computadora') is not None)


def add_action(action):
    partida_actual['mano_actual']['acciones'].append(action)


def get_current_round():
    return get_current_hand()['rondas'][-1]


def get_previous_round():
    return get_current_hand()['rondas'][-2] if len(get_current_hand()['rondas']) > 1 else {}
