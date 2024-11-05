import json
def guardar_partida(partida):
    with open("guardar_partida.json",'w') as archivo:


        json.dump(partida,archivo)
#ejemplo de prueba
partida = {'puntos':3, 'ganador':"usuario"}
guardar_partida(partida)
# #Se implementa mas adelante en el desarrollo
# def hay_partida_guardada():
#     try:
#         with open('partida_guardada.json', 'r+') as archivo:
#             if archivo:
#                 return True
#     except FileNotFoundError:
#         return False


# def cargar_partida_guardada():
#     with open('partida_guardada.json', 'r+') as archivo:
#         if archivo:
#             return json.load(archivo)


# def guardar_partida(partida):
#     try:
#         with open('partida_guardada.json', 'w') as archivo:
#             json.dump(partida, archivo)

#             return True
#     except FileNotFoundError:
#         return False

# # partido de historial
# # {
# # ganador: 'Computadora' o 'Jugador',
# # puntos_jugador: int,
# # puntos_computadora: int,
# # fecha: str
# # }
# def buscar_historial():
#     with open('historial.json', 'r+') as archivo:
#         if archivo:
#             return json.load(archivo)



# def guardar_partida_en_historial(partido):
#     try:
#         with open('historial.json', 'w') as archivo:
#             json.dump(partido, archivo)

#             return True
#     except FileNotFoundError:
#         return False

# def mostrar_historial():
#     pass


# hay_partida_guardada()
