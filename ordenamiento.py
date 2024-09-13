def ordenar_burbujas(mano):
    for i in range(len(mano)):
        for j in range(len(mano)-1):
            if mano[j][3] > mano[j+1][3]:
                mano[j], mano[j + 1] = mano[j + 1], mano[j]
    return mano
