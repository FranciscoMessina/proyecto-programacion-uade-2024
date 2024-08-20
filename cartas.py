import random

mazo_truco = [
    {"id": "espada_1", "nombre": "Ancho de Espada", "palo": "espada", "valor": 1, "poder": 14, "envido":1},
    {"id": "espada_2", "nombre": "Dos de Espada", "palo": "espada", "valor": 2, "poder": 9,"envido":2},
    {"id": "espada_3", "nombre": "Tres de Espada", "palo": "espada", "valor": 3, "poder": 10,"envido":3},
    {"id": "espada_4", "nombre": "Cuatro de Espada", "palo": "espada", "valor": 4, "poder": 1,"envido":4},
    {"id": "espada_5", "nombre": "Cinco de Espada", "palo": "espada", "valor": 5, "poder": 2,"envido":5},
    {"id": "espada_6", "nombre": "Seis de Espada", "palo": "espada", "valor": 6, "poder": 3,"envido":6},
    {"id": "espada_7", "nombre": "Siete de Espada", "palo": "espada", "valor": 7, "poder": 12,"envido":7},
    {"id": "espada_10", "nombre": "Diez de Espada", "palo": "espada", "valor": 10, "poder": 5,"envido":0},
    {"id": "espada_11", "nombre": "Once de Espada", "palo": "espada", "valor": 11, "poder": 6,"envido":0},
    {"id": "espada_12", "nombre": "Doce de Espada", "palo": "espada", "valor": 12, "poder": 7,"envido":0},
    {"id": "basto_1", "nombre": "Ancho de Basto", "palo": "basto", "valor": 1, "poder": 13,"envido":1},
    {"id": "basto_2", "nombre": "Dos de Basto", "palo": "basto", "valor": 2, "poder": 9,"envido":2},
    {"id": "basto_3", "nombre": "Tres de Basto", "palo": "basto", "valor": 3, "poder": 10,"envido":3},
    {"id": "basto_4", "nombre": "Cuatro de Basto", "palo": "basto", "valor": 4, "poder": 1,"envido":4},
    {"id": "basto_5", "nombre": "Cinco de Basto", "palo": "basto", "valor": 5, "poder": 2,"envido":5},
    {"id": "basto_6", "nombre": "Seis de Basto", "palo": "basto", "valor": 6, "poder": 3,"envido":6},
    {"id": "basto_7", "nombre": "Siete de Basto", "palo": "basto", "valor": 7, "poder": 4,"envido":7},
    {"id": "basto_10", "nombre": "Diez de Basto", "palo": "basto", "valor": 10, "poder": 5,"envido":0},
    {"id": "basto_11", "nombre": "Once de Basto", "palo": "basto", "valor": 11, "poder": 6,"envido":0},
    {"id": "basto_12", "nombre": "Doce de Basto", "palo": "basto", "valor": 12, "poder": 7,"envido":0},
    {"id": "oro_1", "nombre": "Uno de Oro", "palo": "oro", "valor": 1, "poder": 8,"envido":1},
    {"id": "oro_2", "nombre": "Dos de Oro", "palo": "oro", "valor": 2, "poder": 9,"envido":2},
    {"id": "oro_3", "nombre": "Tres de Oro", "palo": "oro", "valor": 3, "poder": 10,"envido":3},
    {"id": "oro_4", "nombre": "Cuatro de Oro", "palo": "oro", "valor": 4, "poder": 1,"envido":4},
    {"id": "oro_5", "nombre": "Cinco de Oro", "palo": "oro", "valor": 5, "poder": 2,"envido":5},
    {"id": "oro_6", "nombre": "Seis de Oro", "palo": "oro", "valor": 6, "poder": 3,"envido":6},
    {"id": "oro_7", "nombre": "Siete de Oro", "palo": "oro", "valor": 7, "poder": 11,"envido":7},
    {"id": "oro_10", "nombre": "Diez de Oro", "palo": "oro", "valor": 10, "poder": 5,"envido":0},
    {"id": "oro_11", "nombre": "Once de Oro", "palo": "oro", "valor": 11, "poder": 6,"envido":0},
    {"id": "oro_12", "nombre": "Doce de Oro", "palo": "oro", "valor": 12, "poder": 7,"envido":0},
    {"id": "copa_1", "nombre": "Uno de Copa", "palo": "copa", "valor": 1, "poder": 8,"envido":1},
    {"id": "copa_2", "nombre": "Dos de Copa", "palo": "copa", "valor": 2, "poder": 9,"envido":2},
    {"id": "copa_3", "nombre": "Tres de Copa", "palo": "copa", "valor": 3, "poder": 10,"envido":3},
    {"id": "copa_4", "nombre": "Cuatro de Copa", "palo": "copa", "valor": 4, "poder": 1,"envido":4},
    {"id": "copa_5", "nombre": "Cinco de Copa", "palo": "copa", "valor": 5, "poder": 2,"envido":5},
    {"id": "copa_6", "nombre": "Seis de Copa", "palo": "copa", "valor": 6, "poder": 3,"envido":6},
    {"id": "copa_7", "nombre": "Siete de Copa", "palo": "copa", "valor": 7, "poder": 4,"envido":7},
    {"id": "copa_10", "nombre": "Diez de Copa", "palo": "copa", "valor": 10, "poder": 5,"envido":0},
    {"id": "copa_11", "nombre": "Once de Copa", "palo": "copa", "valor": 11, "poder": 6,"envido":0},
    {"id": "copa_12", "nombre": "Doce de Copa", "palo": "copa", "valor": 12, "poder": 7,"envido":0}
]


#hola agussss

def repartir_cartas(mazo):
    cartas=[]
    for x in range (0,3):
        carta=random.choice(mazo)
        cartas.append(carta["nombre"])
    return cartas

a=repartir_cartas(mazo_truco)
print("sus cartas son las siguientes: ",a)

