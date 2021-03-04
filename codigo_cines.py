import json
with open ('cines.json','r') as fichero:
    doc=json.load(fichero)

#Listar información: Listar las películas que tiene cada cine y sus sesiones.
def listar_pelisysesiones(doc):
    cines = []
    for cine in doc["cines"]:
        cines.append(cine["cines"])
    return cines 

#Contar información: Lista los cines y cuéntame cuantas películas hay en cada una de ellos.


#Buscar o filtrar información: Pide por teclado una película y te dice el director de esa película.


#Buscar información relacionada: Pedir por teclado una sesión, y que te muestre los cines, las películas y la hora a la que es la película.


#Ejercicio libre: Pide por teclado una película y te muestra la sinopsis
