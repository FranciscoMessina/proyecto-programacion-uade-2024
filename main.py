from historial import ver_historial
from partido import nueva_partida
from utilidades import Colores, pedir_eleccion, dev_print


def mensaje_bienvenida():
    """
    Imprime en terminal un mensaje de bienvenida e información del proyecto para el usuario
    :return:
    """
    print(rf"""{Colores.BLUE}
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
    {Colores.RESET}""")
    print(f" PROGRAMACIÓN 1 ".center(69, '-'))
    print("")
    print(f" PROF: {Colores.YELLOW}{Colores.BOLD}JULIA MONASTERIO{Colores.RESET} ".center(82, '-'))
    print("")
    print(f" {Colores.PURPLE}BORRA AGUSTÍN{Colores.RESET} ".center(78, '-'))
    print(f" {Colores.PURPLE}MARGARETO AGUSTÍN{Colores.RESET} ".center(78, '-'))
    print(f" {Colores.PURPLE}MESSINA FRANCISCO{Colores.RESET} ".center(78, '-'))
    print(f" {Colores.PURPLE}PELACCINI FRANCO{Colores.RESET} ".center(78, '-'))

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
    Menu principal del juego, le muestra al usuario las opciones disponibles
    :return:
    """
    mensaje_bienvenida()

    continuar = True

    def cerrar_programa():
        print("Gracias por usar nuestro programa, esperamos verlo pronto.")
        # Esto hace que en vez de buscar la variable en el scope local de la funcion `cerrar_programa` lo busque en el scope anterior,
        # que en este caso es la funcion `jugar_al_truco`. De esta manera se puede modificar la variable `continuar` y salir del bucle.
        # La diferencia con la keyword `global` es que esa buscaría la variable en el scope global del archivo, y no lo encontraría.
        nonlocal continuar
        continuar = False

    while continuar:
        print(f'{Colores.UNDERLINE}Elegi una de las opciones:{Colores.RESET}\n')
        dev_print("MODO DEBUG ACTIVADO: para desactivar, cambiar la variable DEV a False en utilidades.py")

        respuesta = pedir_eleccion([
            ['Comenzar nueva partida', nueva_partida],
            ['Salir del programa', cerrar_programa],
            ['Ver historial', ver_historial],
        ], True)

        respuesta()


jugar_al_truco()
