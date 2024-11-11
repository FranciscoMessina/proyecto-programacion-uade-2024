from mazo import determinar_carta_mayor
from utilidades import formatear_carta, noop
from variables import get_current_round


def determinar_ganador_ronda():
    """
    Función que determina el ganador de la ronda actual y lo imprime en consola.
    :return:
    """
    carta_usuario = get_current_round()['carta_usuario']
    carta_computadora = get_current_round()['carta_computadora']

    ronda_actual = get_current_round()

    carta_ganadora = determinar_carta_mayor(carta_usuario, carta_computadora)

    # Verificamos a quien pertenece la carta ganadora, si es empate se indica como tal.
    # Y guardamos el ganador de la ronda.
    if carta_ganadora == carta_usuario:
        ronda_actual['ganador'] = 'usuario'
    elif carta_ganadora == carta_computadora:
        ronda_actual['ganador'] = 'computadora'
    else:
        ronda_actual['ganador'] = 'empate'

    # Se determina que carta gana

    if carta_ganadora == 'empate':
        print(
            f"{formatear_carta(ronda_actual['carta_usuario'])} empata con {formatear_carta(ronda_actual['carta_computadora'])}")
    else:
        print(f"Gano {formatear_carta(carta_ganadora)}, jugada por {ronda_actual['ganador']}")

    return noop
