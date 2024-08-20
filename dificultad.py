def dificultad(num):
    while  num>0 and num<3:
        if num == 1:
            return("usted selecciono la dificultad facil")
        elif num == 2:
            return("usted selecciono la dificultad normal")
    


bandera=True
while bandera== True:
    dif=int(input("ingrese 1 para la dificultad facil o 2 para la dificultad normal: "))
    if dif>0 and dif<3:
        bandera=False
    else:
        print("ingrese un numero valido")


elegir_dificultad=dificultad(dif)
print(elegir_dificultad)