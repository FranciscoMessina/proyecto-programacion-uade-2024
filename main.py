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

    print('TRUCOOO')


    hay_partidas_guardadas = hay_partida_guardada()

    if hay_partidas_guardadas:
        print('Tenes una partida en progreso guardada, queres continuar con ella?')
        eleccion = int(input(' 1) Si \n 2) No\n'))
        if eleccion == 1:
            continuar_partida()
        else:
            pass


    eleccion = int(input('Elegi una de las opciones: \n 1) Jugar una nueva partida \n 2) Ver el historial de partidas\n'))

    if eleccion == 1:
        nueva_partida()
    elif eleccion == 2:
        mostrar_historial()


jugar_al_truco()