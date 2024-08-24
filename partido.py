#puntos del partido
bandera=True
while bandera== True:
    partida= int(input("elija duracion del juego,escriba 1 para 15 o 2 para 30: " ))
    if partida == 1:
        bandera=False
        puntos=15
    elif partida == 2:
        bandera=False
        puntos=30
    else:
        print("seleccione un numero valido")
        
print("la partida sera a",puntos, "puntos")