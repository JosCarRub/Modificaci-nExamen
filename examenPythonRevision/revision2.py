import random

nombreA = "play2.txt"
a = []
def cargar_lista(nombreArchivo):
    listaCanciones = []
    try:
        with open(nombreArchivo,"r") as archivo:
            for linea in archivo:
                titulo,artista,genero = linea.strip().split("-")
                diccionario = {"nombre" : titulo, "artista": artista, "genero": genero}
                listaCanciones.append(diccionario)
                a.append(diccionario)
                
    except FileNotFoundError:
        print(FileNotFoundError)
    finally:
        return print(listaCanciones)
    

def buscar_cancion(listaCanciones,cancion):
    for indice,Ncancion in enumerate(listaCanciones):
            if cancion == Ncancion["nombre"]:
                return indice
    return -1

def agregar_cancion(listaCanciones,nuevaCancion,artista,genero):
    if buscar_cancion(listaCanciones,nuevaCancion):
        print("La canción ya está registrada")
    else:
        diccionario = {"nombre" : nuevaCancion, "artista": artista, "genero": genero}
        listaCanciones.append(diccionario)
        print("La canción ha sido añadida")
        return listaCanciones

def eliminar_cancion(listaCanciones,titulo):
    if buscar_cancion(listaCanciones,titulo) >= 0:
        listaCanciones.remove(buscar_cancion(listaCanciones,titulo))
        print(f"La canción {titulo} ha sido eliminada")
    else:
        print("La canción no existe en la lista")
    return print(listaCanciones)

def guardar_lista(listaCanciones,nombreArchivo):
    with open(nombreArchivo,"w") as archivo:
        for i in listaCanciones:
            archivo.write(i["nombre"] + " - " + i["artista"] + " - " + i["genero"] + "\n")
    


cargar_lista(nombreA)

buscar_cancion(a,"Yesterday")

a = agregar_cancion(a,"La tarara","Los Cantores de Hispalis","Ragga Techno")

eliminar_cancion(a,"bebe")

guardar_lista(a,nombreA)






