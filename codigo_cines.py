import json
with open ('cines.json','r') as fichero:
    doc=json.load(fichero)

#def prueba(doc):
lista = []
lista = (doc.get("cines"))
lista2 = []
lista2 = (doc.get("cines").get("sesiones"))
for cine in lista.keys():
    for sesiones in lista2.keys():
        print(cine)
        print(sesiones)
#    return lista 

#prueba(doc)



#Listar información: Listar las películas que tiene cada cine y sus sesiones.
#def listar_pelisysesiones(doc):
#    cines = []
#    for cine in doc["cines"]:
#        cines.append(cine["cines"])
#    return cines 

#Contar información: Lista los cines y cuéntame cuantas películas hay en cada una de ellos.


#Buscar o filtrar información: Pide por teclado una película y te dice el director de esa película.
#def director_pelicula(doc,nombre_pelicula):
#    datos = []
#    for i in doc:
#        for pelicula in i["cines"].keys():
#            if pelicula["cines"].keys() == nombre_pelicula:
#                datos(pelicula["cines"].keys()["director"])
#    return datos 

#Buscar información relacionada: Pedir por teclado una sesión, y que te muestre los cines, las películas y la hora a la que es la película.


#Ejercicio libre: Pide por teclado una película y te muestra la sinopsis

#nombre_pelicula = input("Nombre Pelicula: ")
#for dato in director_pelicula(doc,nombre_pelicula):
#    print("Director: ",i["director"])