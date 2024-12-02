import pytest

from acciones import jugar_carta, cantar_truco, aceptar_truco, rechazar_truco, cantar_envido
from envido import calcular_puntos_por_ganar_envido
from mano import determinar_puntos_ganador, determinar_ganador_de_la_mano
from mazo import mazo_truco
from ronda import determinar_ganador_ronda
from variables import reset_game, init_game, default_game_init, partida_actual, USUARIO, COMPUTADORA, get_current_round, \
    init_hand, next_play_by, truco_cantado_por, truco_needs_answer, truco_rechazado_por, \
    envido_cantado_por, envido_needs_answer, get_current_game


@pytest.fixture
def reset_game_data():
    print("Reset game data")
    if partida_actual != {}:
        reset_game()


def init_game_for_test(cartas_usuario, cartas_computadora, max_points=30):
    game_init = default_game_init()
    game_init['puntos_maximos'] = max_points
    init_game(game_init)

    mano_actual = init_hand(cartas_usuario, cartas_computadora)

    mano_actual['rondas'].append({
        "ganador": None
    })

    return mano_actual


def test_jugar_carta(reset_game_data):
    ancho_de_espada = mazo_truco[0]
    siete_de_oro = mazo_truco[26]

    init_game_for_test([ancho_de_espada], [siete_de_oro])

    jugar_carta(ancho_de_espada, USUARIO)()
    jugar_carta(siete_de_oro, COMPUTADORA)()

    ronda_actual = get_current_round()

    assert ancho_de_espada == ronda_actual['carta_usuario']
    assert siete_de_oro == ronda_actual['carta_computadora']

    assert True


def test_ganador_ronda(reset_game_data):
    ancho_de_espada = mazo_truco[0]
    ancho_de_basto = mazo_truco[10]
    siete_de_oro = mazo_truco[26]
    siete_de_copa = mazo_truco[36]

    mano_actual = init_game_for_test(
        [ancho_de_espada, siete_de_copa],
        [ancho_de_basto, siete_de_oro]
    )

    ronda_actual = get_current_round()

    jugar_carta(ancho_de_espada, USUARIO)()
    jugar_carta(siete_de_oro, COMPUTADORA)()

    determinar_ganador_ronda()

    assert ronda_actual['ganador'] == USUARIO

    jugar_carta(ancho_de_basto, COMPUTADORA)()
    jugar_carta(siete_de_copa, USUARIO)()

    determinar_ganador_ronda()

    assert ronda_actual['ganador'] == COMPUTADORA


def test_cantar_truco(reset_game_data):
    mano_actual = init_game_for_test([], [])

    cantar_truco(USUARIO, 1)()

    assert truco_cantado_por() == USUARIO
    assert mano_actual['truco']['nivel'] == 1
    assert truco_needs_answer() == True

    assert next_play_by() == COMPUTADORA

    cantar_truco(COMPUTADORA, 1)()

    # Si por alguna razon se volviese a cantar el mismo nivel de truco, no se debería sobreescribir,
    # ya que ya fue cantado anteriormente
    assert truco_cantado_por() == USUARIO
    # Verificamos que el proximo turno le corresponda a la computadora, ya que su accion no es ejecutada por ser inválida.
    assert next_play_by() == COMPUTADORA


def test_niveles_de_truco(reset_game_data):
    mano_actual = init_game_for_test([], [])

    truco = mano_actual['truco']

    cantar_truco(USUARIO, 1)()

    assert truco_cantado_por() == USUARIO
    assert truco['nivel'] == 1

    # Si tratamos de cantar un nivel de truco que no es el siguiente, no debería permitirlo
    cantar_truco(USUARIO, 3)()
    # Se deberia mantener el el nivel anterior
    assert truco['nivel'] == 1

    # Si el mismo usuario que canto el nivel anterior trata de cantar el siguien, no se debe permitir.
    cantar_truco(USUARIO, 2)()
    # Se deberia mantener el el nivel anterior
    assert truco['nivel'] == 1

    cantar_truco(COMPUTADORA, 2)()

    assert truco_cantado_por() == COMPUTADORA
    assert truco['nivel'] == 2
    assert truco_needs_answer() == True

    assert next_play_by() == USUARIO

    cantar_truco(USUARIO, 3)()

    assert truco_cantado_por() == USUARIO
    assert truco['nivel'] == 3

    pass


def test_aceptar_truco(reset_game_data):
    mano_actual = init_game_for_test([], [])

    cantar_truco(USUARIO, 1)()

    aceptar_truco(COMPUTADORA)()

    assert truco_needs_answer() == False
    assert mano_actual['truco']['activo'] == True

    pass


def test_rechazar_truco(reset_game_data):
    init_game_for_test([], [])

    cantar_truco(USUARIO, 1)()

    rechazar_truco(COMPUTADORA)()

    assert truco_needs_answer() == False
    assert truco_rechazado_por() == COMPUTADORA

    # Si ya fue rechazado al cantar otro truco, no debería cambiar el estado de la partida, manteniéndose igual a antes.
    cantar_truco(USUARIO, 1)()
    cantar_truco(COMPUTADORA, 2)()
    cantar_truco(USUARIO, 3)

    assert truco_needs_answer() == False
    assert truco_rechazado_por() == COMPUTADORA

    pass


def test_puntos_por_ganar_mano(reset_game_data):
    mano_actual = init_game_for_test([], [])

    puntos = determinar_puntos_ganador()

    # Si no se canto truco, debería ganar un solo punto
    assert puntos == 1

    cantar_truco(USUARIO, 1)()
    aceptar_truco(COMPUTADORA)()

    puntos = determinar_puntos_ganador()

    # Si se cantó truco y fue aceptado, debería ganar 2 puntos
    assert puntos == 2

    cantar_truco(COMPUTADORA, 2)()
    aceptar_truco(USUARIO)()

    puntos = determinar_puntos_ganador()

    # Si se cantó retruco y fue aceptado, debería ganar 3 puntos
    assert puntos == 3

    cantar_truco(USUARIO, 3)()
    aceptar_truco(COMPUTADORA)()

    puntos = determinar_puntos_ganador()

    # Si se cantó vale cuatro y fue aceptado, debería ganar 4 puntos
    assert puntos == 4


def test_ganador_mano(reset_game_data):
    mano_actual = init_game_for_test([], [])

    mano_actual['rondas'] = [{"ganador": USUARIO}, {"ganador": COMPUTADORA}, {"ganador": USUARIO}]

    ganador = determinar_ganador_de_la_mano()
    # Si el mismo usuario gano 2 rondas, debería ser el ganador de la mano
    assert ganador == USUARIO

    mano_actual['rondas'] = [{"ganador": "empate"}, {"ganador": USUARIO}]

    ganador = determinar_ganador_de_la_mano()

    # Si se empató la primera ronda, debería ganar el que gano la segunda
    assert ganador == USUARIO

    mano_actual['rondas'] = [{"ganador": USUARIO}, {"ganador": "empate"}]

    ganador = determinar_ganador_de_la_mano()

    # Si se empató la segunda ronda, debería ganar el que gano la primera
    assert ganador == USUARIO

    mano_actual['rondas'] = [{"ganador": USUARIO}, {"ganador": COMPUTADORA}, {"ganador": "empate"}]

    ganador = determinar_ganador_de_la_mano()
    # Si se empató la tercera ronda, debería ganar el que gano la primera
    assert ganador == USUARIO

    mano_actual['rondas'] = [{"ganador": "empate"}, {"ganador": "empate"}, {"ganador": USUARIO}]

    ganador = determinar_ganador_de_la_mano()

    # Si se empataron las dos primeras rondas, debería ganar el que gano la tercera
    assert ganador == USUARIO


def test_cantar_envidos(reset_game_data):
    mano_actual = init_game_for_test([], [])

    envido = mano_actual['envido']

    cantar_envido(USUARIO, 'envido_2')()
    # Si se trata de cantar Envido Envido, sin haber cantado envido antes, no se puede, y no se actualiza el estado de la partida.
    assert envido_cantado_por() is None
    assert envido_needs_answer() == False

    cantar_envido(USUARIO, 'envido')()
    # Si se canta envido, debería actualizarse el estado de la partida.
    assert envido_cantado_por() == USUARIO
    assert envido_needs_answer() == True
    assert next_play_by() == COMPUTADORA
    assert 'envido' in envido['cantados']

    cantar_envido(COMPUTADORA, 'envido')()
    # Si se canta un envido que ya fue cantado no se deberia actualizar el estado de la partida
    assert envido_cantado_por() == USUARIO
    assert envido_needs_answer() == True
    assert next_play_by() == COMPUTADORA
    assert ['envido'] == envido['cantados']

    cantar_envido(COMPUTADORA, 'real_envido')()
    # Si se canta un real envido, debería actualizarse el estado de la partida.
    assert envido_cantado_por() == COMPUTADORA
    assert envido_needs_answer() == True
    assert next_play_by() == USUARIO
    assert 'real_envido' in envido['cantados']

    cantar_envido(COMPUTADORA, 'falta_envido')()
    # Si un mismo jugador canta dos envidos seguidos, no debería actualizarse el estado de la partida.
    assert envido_cantado_por() == COMPUTADORA
    assert envido_needs_answer() == True
    assert next_play_by() == USUARIO
    assert 'falta_envido' not in envido['cantados']

    cantar_envido(USUARIO, 'envido_2')()
    # Si se trata de cantar Envido Envido, después de haber cantado algún envido además del inicial
    # , no se puede, y no se actualiza el estado de la partida.
    assert envido_cantado_por() == COMPUTADORA
    assert envido_needs_answer() == True
    assert next_play_by() == USUARIO
    assert 'envido_2' not in envido['cantados']


def test_puntos_por_envido(reset_game_data):
    mano_actual = init_game_for_test([], [])

    # Si se canta envido y es aceptado, debería sumar 2 puntos
    mano_actual['envido'] = {
        'cantados': ['envido'],
        'rechazado_por': None,
    }

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == 2

    # Si se canta envido y es rechazado, debería sumar 1 punto
    mano_actual['envido'] = {
        'cantados': ['envido'],
        'rechazado_por': USUARIO,
    }

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == 1

    # Si se cantan estos envidos y son aceptados, debería sumar 4 puntos
    mano_actual['envido'] = {
        'cantados': ['envido', 'envido_2'],
        'rechazado_por': None,
    }

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == 4

    # Si se cantan estos envidos y el último es rechazado, debería sumar 2 puntos
    mano_actual['envido'] = {
        'cantados': ['envido', 'envido_2'],
        'rechazado_por': USUARIO,
    }

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == 2

    # Si se cantan estos envidos y son aceptados, debería sumar 7 puntos
    mano_actual['envido'] = {
        'cantados': ['envido', 'envido_2', 'real_envido'],
        'rechazado_por': None,
    }

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == 7

    # Si se cantan estos envidos y el último es rechazado, debería sumar 4 puntos
    mano_actual['envido'] = {
        'cantados': ['envido', 'envido_2', 'real_envido'],
        'rechazado_por': USUARIO,
    }

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == 4

    # Si se cantan estos envidos y son aceptados, debería sumar 5 puntos
    mano_actual['envido'] = {
        'cantados': ['envido', 'real_envido'],
        'rechazado_por': None,
    }

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == 5

    # Si se cantan estos envidos y el último es rechazado, debería sumar 2 puntos
    mano_actual['envido'] = {
        'cantados': ['envido', 'real_envido'],
        'rechazado_por': USUARIO,
    }

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == 2

    # Si se cantan estos envidos y el último es rechazado, debería sumar 7 puntos
    mano_actual['envido'] = {
        'cantados': ['envido', 'envido_2', 'real_envido', 'falta_envido'],
        'rechazado_por': USUARIO,
    }

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == 7

    # Si se cantan estos envidos y el último es rechazado, debería sumar 4 puntos
    mano_actual['envido'] = {
        'cantados': ['envido', 'envido_2', 'falta_envido'],
        'rechazado_por': USUARIO,
    }

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == 4

    # Si se cantan estos envidos y el último es rechazado, debería sumar 2 puntos
    mano_actual['envido'] = {
        'cantados': ['envido', 'falta_envido'],
        'rechazado_por': USUARIO,
    }

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == 2

    # Si el falta envido fue aceptado:
    # Si se cantan estos envidos y el último es rechazado, debería sumar 4 puntos
    mano_actual['envido'] = {
        'cantados': ['falta_envido'],
        "rechazado_por": None
    }

    current_game = get_current_game()
    # En una partida a 15
    current_game['puntos_maximos'] = 15

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == 15

    # En una partida a 30
    current_game['puntos_maximos'] = 30

    # Si ambos están en las malas
    current_game['puntos'] = {
        USUARIO: 12,
        COMPUTADORA: 14
    }

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == 30

    # Si alguno está en las buenas
    current_game['puntos'] = {
        USUARIO: 16,
        COMPUTADORA: 14
    }

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == abs(16 - 14)

    # Si alguno está en las buenas
    current_game['puntos'] = {
        USUARIO: 25,
        COMPUTADORA: 12
    }

    puntos = calcular_puntos_por_ganar_envido()

    assert puntos == abs(25 - 12)
