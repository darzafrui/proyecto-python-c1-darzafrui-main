#-------------------------------------------------------------------------ENTREGA 1 ------------------------------------------------------------------------------------------------
import csv
from collections import namedtuple, defaultdict
from matplotlib import pyplot as plt
from datetime import datetime
from time import strptime
from unittest import result

tv_shows = namedtuple('Info','row_ID, title, minima_edad_recomendada, netflix, hulu, prime_video, disney, fecha_salida, espanyol, puntuacion_sobre_diez')

fichero = './data/tv_shows_data_22.csv'

def lee_datos(fichero):
    resultado = []
    with open (fichero, encoding = 'utf-8' ) as f:
        lector = csv.reader(f)
        next(lector)
        for row_ID, title, minima_edad_recomendada, netflix, hulu, prime_video, disney, fecha_salida, espanyol, puntuacion_sobre_diez  in lector:
            row_ID = int(row_ID)
            title = str(title)
            minima_edad_recomendada = str(minima_edad_recomendada)
            netflix = int(netflix)
            hulu = int(hulu)
            prime_video = int(prime_video)
            disney = int(disney)
            fecha_salida = datetime.strptime(fecha_salida, "%d/%m/%Y").date()
            espanyol = parse_espanyol(espanyol)
            puntuacion_sobre_diez = float(puntuacion_sobre_diez)
            tupla = tv_shows(row_ID, title, minima_edad_recomendada, netflix, hulu, prime_video, disney, fecha_salida, espanyol, puntuacion_sobre_diez)
            resultado.append(tupla)
    return resultado

def parse_espanyol(string):
    if(string=='VERDADERO'):
        espanyol=True
    else:
        espanyol=False
    return espanyol



#-------------------------------------------------------------------------ENTREGA 2 ------------------------------------------------------------------------------------------------


#BLOQUE I
#EJERCICIO 1 (1)
def filtra_por_edades_minimas(fichero,minima_edad_recomendada):
#devuelve fila filtrada por un columna    
    result = []
    for a in fichero:
        if a[2] in minima_edad_recomendada:
            result.append(a.title)
    print("Todos los titulos que contienen",minima_edad_recomendada,"como edad permisiva son_:", result)
    return result
    

#EJERCICIO 2 (3)
def get_media_valoraciones(fichero):
#obtengo la media de las valoraciones de cada show
    result = []
    valoraciones = [p.puntuacion_sobre_diez for p in fichero]
    result = (sum(valoraciones)/len(valoraciones))
    return result


#BLOQUE II
#EJERCICIO 3 (5)
def get_valoración_minima_de_shows(fichero):
    result = 0
    valoraciones = [p.puntuacion_sobre_diez for p in fichero]
    result = min(valoraciones)
    return result

def get_show_por_puntuacion(fichero, puntuacion):
    show_minimo = [a.title for a in fichero if a.puntuacion_sobre_diez == puntuacion] 
    return show_minimo
    

#EJERCICIO 4 (8)
def ordena_por_puntuacion(fichero, mayor):
    titulo_val = [(a.title, a.puntuacion_sobre_diez) for a in fichero]
    if mayor == "arriba":
        control = True
    else:
        control = False
    titulo_val.sort(key=lambda x: x[1], reverse=control)
    return titulo_val


#-------------------------------------------------------------------------ENTREGA 3 ------------------------------------------------------------------------------------------------

#BLOQUE III
#EJERCICIO 5 (1)
def contar_edades_minimas(fichero):
#devuelve un diccionario el cual tiene como clave las diferentes edades y como valor el numero de tuplas que contienen dicha edad.
    minima_edad_recomendada=[p.minima_edad_recomendada for p in fichero]
    result = dict()
    for minima_edad_recomendada in minima_edad_recomendada:
        clave = minima_edad_recomendada
        if clave in result:
            result[clave] = result[clave]+1
        else:
            result[clave] = 1
    return result


#EJERCICIO 6 (3)
def get_max_common_edad_minima(fichero):
    edad_max_common = max(contar_edades_minimas(fichero).keys(), key = lambda k:contar_edades_minimas(fichero)[k])
    return edad_max_common


#EJERCICIO 7 (6)
def calcular_porcentaje(fichero,edad):
    cont=0
    cont_esp=0
    for p in fichero:
        if p.minima_edad_recomendada==edad:
            if p.español:
                cont+=1
                cont_esp+=1
            else:
                cont+=1
    return cont_esp*100/cont

def get_porcentaje_espanyol_por_edad(fichero):
    dict={}
    minima_edad_recomendada={p.minima_edad_recomendada for p in fichero}
    for edad in minima_edad_recomendada:
        dict[edad]=calcular_porcentaje(fichero,edad)
    return dict
    

#EJERCICIO 8 (8)
def top_n_large_title_por_anyo(fichero, n = 4):
    dict = {}
    anyos = {t.fecha_salida.year for t in fichero}
    for p in anyos:
        dict[p] = sorted([t.puntuacion_sobre_diez for t in fichero if t.fecha_salida.year == p], reverse=False)[:n]
    return dict


#EJERCICIO 9 (10)
def agrupacion_por_anyo_titulo(fichero):
    aux = dict()
    for n in fichero:
        anyo = n.fecha_salida.year
        if anyo not in aux:
            aux[anyo] = {(n.title, n.español)}
        else:
            aux[anyo].add((n.title, n.español))
    return aux

#BLOQUE IV
#EJERCICIO 10 (gráfica)
def grafica_frecuencia_shows_por_edad(fichero):
    e = ['all','7+','13+','16+','18+']
    dicc = []
    for p in e:
        dicc.append(len(filtra_por_edades_minimas(fichero,p)))
    plt.pie(dicc, labels= e, autopct='%1.1f%%', shadow=True, startangle=3220)
    plt.title('Gráfica de porcentaje de edades')
    plt.show()