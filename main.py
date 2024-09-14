from guardado import hay_partida_guardada, mostrar_historial
from mazo import mazo_truco
from partido import nueva_partida, continuar_partida
from utilidades import Colors, pedir_eleccion, imprimir_carta_ascii


def mensaje_bienvenida():
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


def jugar_al_truco():
    mensaje_bienvenida()

    print(rf"""
             .------..------..------..------..------.
             |T.--. ||R.--. ||U.--. ||C.--. ||O.--. |
             | :/\: || :(): || (\/) || :/\: || :/\: |
             | (__) || ()() || :\/: || :\/: || :\/: |
             | '--'T|| '--'R|| '--'U|| '--'C|| '--'O|
             `------'`------'`------'`------'`------'
""")

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
