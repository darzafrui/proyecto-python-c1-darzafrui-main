from tv_shows import *

def test_show_con_peor_valoracion (tv_shows):
    nombre_show_mas_bajo = get_show_por_puntuacion(tv_shows, get_valoración_minima_de_shows(tv_shows))
    print("La puntuacion más baja de los shows es " ,get_valoración_minima_de_shows(tv_shows), " y corresponde a ", nombre_show_mas_bajo)

def test_contar_edades_minimas(tv_shows):
    print("El filtrado de shows por edad es: ",contar_edades_minimas(tv_shows))

def test_get_media_valoraciones(tv_shows):
    print("La media de valoraciones de todos los shows es de " + str(get_media_valoraciones(tv_shows)) + " sobre 10" )


def test_filtra_por_edades_minimas(tv_shows):
    minima_edad_recomendada = input("Introduce la edad por la que desea filtrar los shows (all,7+,13+,16+,18+): ")
    print(filtra_por_edades_minimas(tv_shows,minima_edad_recomendada))
    

def test_ordena_por_puntuacion(tv_shows):
    mayor = input("Intruce en que orden quieres que devuelva las puntuaciones, empezando por(abajo o arriba): ")
    print(ordena_por_puntuacion(tv_shows,mayor))

def main():
    tv_shows = lee_datos("./data/tv_shows_data_22.csv")
    #print(tv_shows)

    #print(len(tv_shows))
    #print(tv_shows[0])
    #print(tv_shows[1])
    #print(tv_shows[2])
    #print(tv_shows[3216])
    #print(tv_shows[3217])
    #print(tv_shows[-1])

    #print(test_filtra_por_edades_minimas(tv_shows)) #EJERCICIO 1 parte 1
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    #print(test_contar_edades_minimas(tv_shows)) #EJERCICIIO 1 parte 2
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    #print(test_get_media_valoraciones(tv_shows)) #EJERICIO 2
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    #print(test_show_con_peor_valoracion(tv_shows)) #EJERCICIO 3
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    #print(test_ordena_por_puntuacion(tv_shows)) #EJERICIO 4
    #print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
    