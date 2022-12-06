# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<22\>/\<23\>) 
Autor/a: \<Darío Zafra Ruiz\>   uvus:\<YCW8136\>

Aquí debes añadir la descripción del dataset y un enunciado del dominio del proyecto.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<tv_shows.py\>**: Contiene funciones para trabajar con los datos de los shows de televisión .
  * **\<test_tv_shows.py\>**: Contiene funciones de test para probar las funciones del módulo tv_shows.py.En este módulo esta el main.
  * **\<gráficas.py\>**: Contiene funciones para dibujar gráficas
* **/data**: Contiene el dataset del proyecto
    * **\<tv_shows_data_22.csv\>**: contiene los datos de los tv shows del proyecto.
    
## Estructura del *dataset*

Aquí debes describir la estructura del dataset explicando qué representan los datos que contiene y la descripción de cada una de las columnas.

El dataset está compuesto por \<12\> columnas, con la siguiente descripción:

* **\<row_ID>**: de tipo \<int\>, es un identificador entero. 
* **\<title>**: de tipo \<str\>, representa el título del show de televisión.
* **\<minima_edad_recomendada>**: de tipo \<int\>, representa la edad mínima que se recomienda para ver dicho título.
* **\<netflix>**: de tipo \<int\>, representa la disponibilidad que hay en netflix.
* **\<hulu>**: de tipo \<int\>, representa la disponibilidad que hay en hulu.
* **\<prime_video>**: de tipo \<int\>,representa la disponibilidad que hay en Prime Video.
* **\<disney>**: de tipo \<int\>, representa la disponibilidad que hay en Disney Plus.
* **\<fecha_salida>**: de tipo \<date\>, representa la fehca de publicación de dicho título.
* **\<espanyol>**: de tipo \<bool\>, representa la disponibilidad que hay de dicho show en español como idioma.
* **\<puntuacion_sobre_diez>**: de tipo \<float\>, representa la valoracion sobre 10 del show.
...

## Tipos implementados

Descrbe aquí la o las namedtuple que defines en tu proyecto.
Info = namedtuple('Info','row_ID, title, minima_edad_recomendada, netflix, hulu, prime_video, disney, fecha_salida, español, puntuacion_sobre_diez')
Info(int, str, int, int, int, int, int, datetime.date, bool, float)

## Funciones implementadas
Añade aquí descripciones genéricas de las funciones, que luego debes acompañar con comentarios de tipo documentación en el código.

### \<tv_shows.py\>

* **<lee_datos>**: lee los datos del fichero csv y devuelve una lista de tuplas de tipo Info con los datos del fichero. Para implementar esta función se han definido las siguientes funciones auxiliares en el módulo tv_shows.py:
  * **<with open >**: abre y lee el archivo.
    * **<for in >**: realiza un bucle.

* **<parse_espanyol>**: convierte el valor asociado a la columna "espanyol" a un boolean.
    
* **<filtra_por_edades_minimas>**: el programa pide introducir la edad minima por la que desea filtrar los titulos de los shows, los cuales se califican en "all","7+","13+","16+","18+". Para ello he utilizado:
  * **<for in >**: un blucle para recorrer el archivo extrayendo un valor
    * **<if else>** : filtra a traves de una condición
  * **<print>**: printea por pantalla el filtro hecho

* **<get_media_valoraciones>**: el programa recorre todas las valoraciones obteniendo su valor, con ellos hace una media ponderada y devuelve dicho valor:
  * **<sum >**: suma todos los valores obtenidos
  * **<7>**: divide
  * **<len>**: cuenta la cantidades de valores, en este caso, de puntuaciones que hay

* **<get_valoracion_minima_de_shows>**: coge las valoraciones obtenidas anteriormente y extrae el valor minimo de ellas
  * **<min>**: obtiene el minimo valor de algun conjunto de ellos

* **<get_show_por_puntuacion>**: extrae el show que tiene la valoracion minima, obtenida anteriorimente
  * **<for in >**: un blucle para recorrer el archivo extrayendo una columna
    * **<if else>** : filtra a traves de una condición

* **<ordena_por_puntuacion>**: este porgrama filtra las puntuacines, y las ordena segun el valor que introduzcas:
  * **<for in >**: un blucle para recorrer el archivo extrayendo un valor
    * **<if else>** : filtra a traves de una condición
  * **<.sort>**: ordena valores
  * **<key lambda>**: aclara al programa por que columna quiere que filtre los valores, en este caso, las puntuaciones

* **<contar_edades_minimas>**: crea un diccionario el cual las claves son las edades minimas que hay y los valores la cantidad de shows clasificados por cada edad:
  * **< dict() >**: esta funcion crea un diccionario clave valor
    * **<for in>** :vcrea un bucle recorriendo el dichero
      * **<if else>**: filtra por edades contantabilizandolas

* **<get_max_common_edad_minima>**: devuelve la clave que tiene asocidada el valor maximo de shows que contiene el diccionario de la funcion anterior, es decir "contar_edades_minimas".

* **<calcular_porcentaje>**:recibe un valor sacado de un bucle for, y lo trabaja para sacar un porcentaje.
* **<get_porcentaje_espanyol_por_edad>**: calcula el porcentaje de peliculas en espanyol que hay por cada edad mininma recomendada.

* **<top_n_large_title_por_anyo>**: devuelve un diccionario el cual toma como clave los distintos anyos los cuales aparecen en las fechas de salidas de los shows y como valor los titulos mas largos, devuelve tantos titulos como "n" marque.

* **<agrupacion_por_anyo_titulo>**: devuelve un diccionario en que el las claves son los anyos y el valor todos los titulos de shows que salieron ese anyo.

* **<grafica_frecuencia_shows_por_edad>**: consiste en una gráfica tipo sectores en la cual los diferentes sectores son las distintas edades mínimas que hay por shows, y en lo que se basa dichos sectores son los porcentajes en los que aparacen en los shows dichas edades.

### \<test_tv_shows.py\>

Cada funcion del module "tv_shows" tiene en el modulo de test su correspundiente testeo, generalmente estas contienen un printeo con caracteres aclarando y embelleciendo las funciones. Hay dos en concretos que contienen:

* **<input>**: esta funcion hace que tengas que introducir un valor en la terminal que toma como parametro en la funcion

* **<main>**: ejecuta la funcion del modulo de tv_shows-py
