from colores import Colors
from guardado import hay_partida_guardada, mostrar_historial
from partido import nueva_partida, continuar_partida


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

    while continuar:
        eleccion = int(input(
            'Elegi una de las opciones: \n 1) Jugar una nueva partida \n 2) Salir del programa \n más opciones próximamente'))

        if eleccion == 1:
            nueva_partida()
        elif eleccion == 2:
            continuar = False
            print('Gracias por jugar!')
        else:
            print('Elegí una opción válida')


jugar_al_truco()
