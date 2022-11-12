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
* **\<español>**: de tipo \<bool\>, representa la disponibilidad que hay de dicho show en español como idioma.
* **\<puntuacion_sobre_diez>**: de tipo \<float\>, representa la valoracion sobre 10 del show.
...

## Tipos implementados

Descrbe aquí la o las namedtuple que defines en tu proyecto.
Info = namedtuple('Info','row_ID, title, minima_edad_recomendada, netflix, hulu, prime_video, disney, fecha_salida, español, puntuacion_sobre_diez')
Info(int, str, int, int, int, int, int, datetime.date, bool, float)

## Funciones implementadas
Añade aquí descripciones genéricas de las funciones, que luego debes acompañar con comentarios de tipo documentación en el código

### \<tv_shows.py\>

* **<lee_datos>**: lee los datos del fichero csv y devuelve una lista de tuplas de tipo Info con los datos del fichero. Para implementar esta función se han definido las siguientes funciones auxiliares en el módulo tv_shows.py:
  * **<with open >**: abre y lee el archivo.
    * **<for in >**: realiza un bucle.

### \<test_tv_shows.py\>

* **<main>**: ejecuta la funcion del modulo de tv_shows-py
