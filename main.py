from guardado import hay_partida_guardada, mostrar_historial
from partido import nueva_partida, continuar_partida
from utilidades import Colors, pedir_eleccion


def mensaje_bienvenida():
    print(rf"""{Colors.BLUE}
 _    _              _____    ______       ___     ___    ___    _  _    
| |  | |     /\     |  __ \  |  ____|     |__ \   / _ \  |__ \  | || |   
| |  | |    /  \    | |  | | | |__           ) | | | | |    ) | | || |_  
| |  | |   / /\ \   | |  | | |  __|         / /  | | | |   / /  |__   _| 
| |__| |  / ____ \  | |__| | | |____       / /_  | |_| |  / /_     | |   
 \____/  /_/    \_\ |_____/  |______|     |____|  \___/  |____|    |_|   {Colors.RESET}
"""
          f"""
--------- PROGRAMACIÓN 1 ---------- PROF: {Colors.YELLOW}{Colors.BOLD}JULIA MONASTERIO{Colors.RESET} -----------

------------------------ {Colors.PURPLE}BORRA AGUSTÍN{Colors.RESET} -------------------------------
------------------------ {Colors.PURPLE}MARGARETTO AGUSTÍN{Colors.RESET} --------------------------
------------------------ {Colors.PURPLE}MESSINA FRANCISCO{Colors.RESET} ---------------------------
------------------------ {Colors.PURPLE}PELLACCINI FRANCO{Colors.RESET} ---------------------------
    """)


def jugar_al_truco():
    mensaje_bienvenida()

    print('Bienvenido al truco!')

    continuar = True

    def cerrar_programa():
        global continuar
        continuar = False

    while continuar:
        print('Elegi una de las opciones:')

        respuesta = pedir_eleccion([
            ['Comenzar nueva partida', nueva_partida],
            ['Salir del programa', cerrar_programa]
        ])

        respuesta()


jugar_al_truco()
