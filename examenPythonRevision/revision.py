import random

def cargar_lista(nombreArchivo):
    diccionarioCanciones = {}
    with open(nombreArchivo,"r") as archivo:
        for linea in archivo:
            titulo,artista = linea.strip().split("-")
            diccionarioCanciones[titulo] = artista
    return diccionarioCanciones

def agregar_cancion(diccionarioCanciones,nuevaCancion,artista):
    diccionarioCanciones[nuevaCancion] = artista

def eliminar_cancion(diccionarioCanciones, titulo):
    if titulo in diccionarioCanciones:
        del(diccionarioCanciones[titulo])

def contar_canciones(diccionarioCanciones):
    return len(diccionarioCanciones)

def buscar_por_artista(diccionarioCanciones,nombreArtista):
    listaCancionesArtista = []
    for titulo,artista in diccionarioCanciones.items():
        if artista == nombreArtista:
            listaCancionesArtista.append(titulo)
    return listaCancionesArtista

def ordenar_alfabeticamente(diccionarioCanciones):
    listaCancionesOrdenada = []
    for canciones in diccionarioCanciones.keys():
        listaCancionesOrdenada.append(canciones)
    tuplaOrdenada = tuple(sorted(listaCancionesOrdenada))
    return tuplaOrdenada

def crear_lista_aleatoria(diccionarioCanciones,n):
    listaAleatoria = []
    listaDefi = []
    for canciones in diccionarioCanciones.keys():
        listaAleatoria.append(canciones)
    for x in range(0,n):
        numRandom = random.randint(0,len(diccionarioCanciones) - 1)
        listaDefi.append(listaAleatoria[numRandom])

    return listaDefi

def guardar_lista(diccionarioCanciones,nombreArchivo):
    with open(nombreArchivo,"w") as archivo:
        for titulo,cancion in diccionarioCanciones.items():
            archivo.write(f"{titulo} - {cancion}\n")

