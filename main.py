from partido import nueva_partida
from utilidades import Colors, pedir_eleccion


def mensaje_bienvenida():
    """
    Imprime en terminal un mensaje de bienvenida e informacion del proyecto para el usuario
    :return:
    """
    print(rf"""{Colors.BLUE}
   ▄         ▄       ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄        ▄▄▄▄▄▄▄▄▄▄▄
  ▐░▌       ▐░▌     ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░▌      ▐░░░░░░░░░░░▌
  ▐░▌       ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀▀▀
  ▐░▌       ▐░▌     ▐░▌       ▐░▌     ▐░▌       ▐░▌     ▐░▌
  ▐░▌       ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌       ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄
  ▐░▌       ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌       ▐░▌     ▐░░░░░░░░░░░▌
  ▐░▌       ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌       ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀
  ▐░▌       ▐░▌     ▐░▌       ▐░▌     ▐░▌       ▐░▌     ▐░▌
  ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌       ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄▄▄
  ▐░░░░░░░░░░░▌     ▐░▌       ▐░▌     ▐░░░░░░░░░░▌      ▐░░░░░░░░░░░▌
   ▀▀▀▀▀▀▀▀▀▀▀       ▀         ▀       ▀▀▀▀▀▀▀▀▀▀        ▀▀▀▀▀▀▀▀▀▀▀
    {Colors.RESET}""")
    print(f" PROGRAMACIÓN 1 ".center(69, '-'))
    print("")
    print(f" PROF: {Colors.YELLOW}{Colors.BOLD}JULIA MONASTERIO{Colors.RESET} ".center(82, '-'))
    print("")
    print(f" {Colors.PURPLE}BORRA AGUSTÍN{Colors.RESET} ".center(78, '-'))
    print(f" {Colors.PURPLE}MARGARETO AGUSTÍN{Colors.RESET} ".center(78, '-'))
    print(f" {Colors.PURPLE}MESSINA FRANCISCO{Colors.RESET} ".center(78, '-'))
    print(f" {Colors.PURPLE}PELLACCINI FRANCO{Colors.RESET} ".center(78, '-'))

    print(rf"""
                 .------..------..------..------..------.
                 |T.--. ||R.--. ||U.--. ||C.--. ||O.--. |
                 | :/\: || :(): || (\/) || :/\: || :/\: |
                 | (__) || ()() || :\/: || :\/: || :\/: |
                 | '--'T|| '--'R|| '--'U|| '--'C|| '--'O|
                 `------'`------'`------'`------'`------'
    """)


def jugar_al_truco():
    """
    Menu principal del juego, se elige si comenzar una nueva partida o salir del programa
    :return:
    """
    mensaje_bienvenida()

    continuar = True

    while continuar:

        print('Elegi una de las opciones: \n'.center(65))

        respuesta = pedir_eleccion([
            ['Comenzar nueva partida', {"accion": nueva_partida}],
            ['Salir del programa', {"accion": "cerrar_programa"}]
        ], True)

        if respuesta['accion'] == 'cerrar_programa':
            print("Gracias por usar nuestro programa, esperamos verlo pronto.")
            continuar = False
        else:
            respuesta['accion']()


jugar_al_truco()
