from tv_shows import *

def test_show_con_peor_valoracion (tv_shows):
    nombre_show_mas_bajo = get_show_por_puntuacion(tv_shows, get_valoración_minima_de_shows(tv_shows))
    print("La puntuacion más baja de los shows es " ,get_valoración_minima_de_shows(tv_shows), " y corresponde a ", nombre_show_mas_bajo)

def test_contar_edades_minimas(tv_shows):
    print("El numero de tuplas por edad es ",contar_edades_minimas(tv_shows))

def test_get_media_valoraciones(tv_shows):
    print("La media de valoraciones de todos los shows es de " + str(get_media_valoraciones(tv_shows)) + " sobre 10" )

def test_filtra_por_edades_minimas(tv_shows):
    minima_edad_recomendada = input("Introduce la edad por la que desea filtrar los shows (all,7+,13+,16+,18+): ")
    print(filtra_por_edades_minimas(tv_shows,minima_edad_recomendada))
    
def test_ordena_por_puntuacion(tv_shows):
    mayor = input("Intruce en que orden quieres que devuelva las puntuaciones, empezando por(abajo o arriba): ")
    print(ordena_por_puntuacion(tv_shows,mayor))

def test_get_max_common_edad_minimas(tv_shows):
    funcion = get_max_common_edad_minima(tv_shows)
    print("La edad minima que mas veces se repite, y por tanto más shows tiene es :", funcion)

def test_get_porcentaje_espanyol_por_edad(tv_shows):
    funcion = get_porcentaje_espanyol_por_edad(tv_shows)
    print("El porcentaje de shows en espanyol filtrado por edades es:",funcion)

def test_top_n_large_title_por_anyo(tv_shows):
    funcion = top_n_large_title_por_anyo(tv_shows)
    print("Los titulos (por defecto, 4 titulos) mas largos clasfisicados por anyos son:", funcion)

def test_agrupacion_por_anyo_titulo(tv_shows):
    funcion =  agrupacion_por_anyo_titulo(tv_shows)
    print("Diccionario que agrupa los títulos por anyos:", funcion)

def test_grafica_frecuencia_shows_por_edad(tv_shows):
    funcion =  grafica_frecuencia_shows_por_edad(tv_shows)
    print("Gráfica relacion peliculas.", funcion)



def main():
    tv_shows = lee_datos("./data/tv_shows_data_22.csv")
    #print(tv_shows)

    #print("El total de registros que contiene el data set es:", len(tv_shows))
    #print("Este es el primer registro:",tv_shows[0])
    #print("Este es el segundo registro:", tv_shows[1])
    #print("Este es el tercer registro:", tv_shows[2])
    #print("Este es el antipenúltimo registro:", tv_shows[3216])
    #print("Este es el penúltimo registro:" , tv_shows[3217])
    #print("Este es el útimo registro:", tv_shows[-1])

    #print(test_filtra_por_edades_minimas(tv_shows)) #EJERCICIO 1 
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    #print(test_get_media_valoraciones(tv_shows)) #EJERICIO 2
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    #print(test_show_con_peor_valoracion(tv_shows)) #EJERCICIO 3
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    #print(test_ordena_por_puntuacion(tv_shows)) #EJERICIO 4
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    #print(test_contar_edades_minimas(tv_shows)) #EJERCICIO 5
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    #print(test_get_max_common_edad_minimas(tv_shows)) #EJERCICIO 6
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    #print(test_get_porcentaje_espanyol_por_edad(tv_shows)) #EJERCICIO 7
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    #print(test_top_n_large_title_por_anyo(tv_shows)) #EJERCICIO 8
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    #print(test_agrupacion_por_anyo_titulo(tv_shows)) #EJERCICIO 9
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    #print(test_grafica_frecuencia_shows_por_edad(tv_shows)) #EJERCICIO 10
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")



if __name__ == "__main__":
    main()
    