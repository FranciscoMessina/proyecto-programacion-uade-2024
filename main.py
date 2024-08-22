from colores import Colors

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


    eleccion_puntos = print('Hasta cuantos puntos queres jugar? \n 1) 15 \n 2) 30')

    puntos = 15 if eleccion_puntos == 1 else 30
    partida = {
        "objetivo": puntos
    }


jugar_al_truco()