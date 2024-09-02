def agregar_ronda(dic, i, j1, j2):
    dic[f"ronda_{i}"] = [j1,j2]
    i +=1
    return i

def rellenar_mano(list, j1, j2, mano):
    if mano == 3:
        list.pop(2)
        list.pop(1)
        list.pop(0)
        mano = 0
    list.append([j1,j2])
    mano +=1
    return mano, list

def sumar(list):
    m1 = list[0]
    m2 = list[1]
    m3 = list[2]
    j1 = m1[0] + m2[0] + m3[0]
    j2 = m1[1] + m2[1] + m3[1]
    return j1, j2

def input_mano():
    j1 = int(input("Ingrese el valor de la mano del jugador 1: "))
    j2 = int(input("Ingrese el valor de la mano del jugador 2: "))
    return j1, j2

def main():
    rondas = {}
    manos = []
    n_rondas = 1
    mano = 0
    j1, j2 = input_mano()
    mano, manos = rellenar_mano(manos, j1, j2, mano)
    j1, j2 = input_mano()
    mano, manos = rellenar_mano(manos, j1, j2, mano)
    j1, j2 = input_mano()
    mano, manos = rellenar_mano(manos, j1, j2, mano)
    if mano == 3:
        rj1, rj2= sumar(manos)
    j1, j2 = input_mano()
    mano, manos = rellenar_mano(manos, j1, j2, mano)
    print(mano)
    print(manos)
    print(rj1)
    print(rj2)
    n_rondas = agregar_ronda(rondas, n_rondas, rj1, rj2)
    print(rondas)

main()