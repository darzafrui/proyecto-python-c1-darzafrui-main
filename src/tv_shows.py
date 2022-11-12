import csv
from collections import namedtuple, defaultdict
from datetime import datetime
from time import strptime
from unittest import result

tv_shows = namedtuple('Info','row_ID, title, minima_edad_recomendada, netflix, hulu, prime_video, disney, fecha_salida, español, puntuacion_sobre_diez')

fichero = './data/tv_shows_data_22.csv'

def lee_datos(fichero):
    resultado = []
    with open (fichero, encoding = 'utf-8' ) as f:
        lector = csv.reader(f)
        next(lector)
        for row_ID, title, minima_edad_recomendada, netflix, hulu, prime_video, disney, fecha_salida, español, puntuacion_sobre_diez  in lector:
            row_ID = int(row_ID)
            title = str(title)
            minima_edad_recomendada = str(minima_edad_recomendada)
            netflix = int(netflix)
            hulu = int(hulu)
            prime_video = int(prime_video)
            disney = int(disney)
            fecha_salida = datetime.strptime(fecha_salida, "%d/%m/%Y").date()
            español = bool(español)
            puntuacion_sobre_diez = float(puntuacion_sobre_diez)
            tupla = tv_shows(row_ID, title, minima_edad_recomendada, netflix, hulu, prime_video, disney, fecha_salida, español, puntuacion_sobre_diez)
            resultado.append(tupla)
    return resultado


#EJERCICIO 1
def filtra_por_edades_minimas(fichero,minima_edad_recomendada):
#devuelve fila filtrada por un columna    
    result = []
    for a in fichero:
        if a[2] in minima_edad_recomendada:
            result.append(a.title)
    print("Todos los titulos que contienen",minima_edad_recomendada,"como edad permisiva son_:", result)
    return result
    
def contar_edades_minimas(fichero):
#devuelve la cantidad de shows filtrada por la edad, es decir, por columnas.
    minima_edad_recomendada=[p.minima_edad_recomendada for p in fichero]
    result = dict()
    for minima_edad_recomendada in minima_edad_recomendada:
        clave = minima_edad_recomendada
        if clave in result:
            result[clave] = result[clave]+1
        else:
            result[clave] = 1

    return result

#EJERCICIO 2:
def get_media_valoraciones(fichero):
#obtengo la media de las valoraciones de cada show
    result = []
    valoraciones = [p.puntuacion_sobre_diez for p in fichero]
    result = (sum(valoraciones)/len(valoraciones))
    return result


#EJERCICIO 3
def get_valoración_minima_de_shows(fichero):
    result = 0
    valoraciones = [p.puntuacion_sobre_diez for p in fichero]
    result = min(valoraciones)
    return result

def get_show_por_puntuacion(fichero, puntuacion):
    show_minimo = [a.title for a in fichero if a.puntuacion_sobre_diez == puntuacion] 
    return show_minimo
    

#EJERCICIO 4


def ordena_por_puntuacion(fichero, mayor):
    titulo_val = [(a.title, a.puntuacion_sobre_diez) for a in fichero]
    if mayor == "arriba":
        control = True
    else:
        control = False
    titulo_val.sort(key=lambda x: x[1], reverse=control)
    return titulo_val
