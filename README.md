# Mexico City Metro Challenge

El reto consiste en crear un programa que dada la estación 'X'  y estación 'Y' se encuentre la ruta más óptima 
para transportarse dentro del metro de la CDMX.


Deberá instalar python si aún no lo ha hecho.
Después instalar lo requerimientos.

```
pip install -r requirements.txt
```

Se compone de 2 etapas sucesivas.

## Etapa 1

A partir el archivo .kml proporcionado, obtener la descripción de la todas las líneas del metro. Cada línea tiene un nombre y una lista de estaciones. Cada estación tiene un nombre y unas coordenadas geográficas (latitud y longitud). 

### Ejemplo

Base

```
python etapa1.py tu_archivo.kml
```

Entrada

```
python etapa1.py Metro_CDMX.kml
```

Salida
```
Linea 1
1 - Observatorio: -99.2005488,19.3982501,0
2 - Tacubaya: -99.187097,19.4031605,0
3 - Juanacatlan: -99.1821724,19.4129053,0
4 - Chapultepec: -99.1762608,19.420813,0
5 - Sevilla: -99.1706067,19.421926,0
6 - Insurgentes: -99.1627908,19.4236259,0
7 - Cuauhtemoc: -99.154653,19.425867,0
8 - Balderas: -99.149074,19.42741,0
9 - Salto del Agua: -99.1422343,19.4267827,0
10 - Isabel la Catolica: -99.1374546,19.4265399,0
11 - Pino Suarez: -99.132911,19.4257912,0
12 - Merced: -99.1246551,19.4254927,0
13 - Candelaria: -99.1194355,19.4288468,0
14 - San Lazaro: -99.1148007,19.4302734,0
15 - Moctezuma: -99.1102624,19.4272178,0
16 - Balbuena: -99.102264,19.4232414,0
17 - Boulevard Puerto Aereo: -99.0960038,19.4197101,0
18 - Gomez Farias: -99.0903497,19.4164114,0
19 - Zaragoza: -99.0823781,19.412288,0
20 - Pantitlan: -99.0722072,19.4153591,0
...
...
...
Linea B
1 - Guerrero: -99.1453725,19.4451408,0
2 - Garibaldi: -99.1392624,19.4427583,0
3 - Lagunilla: -99.1313499,19.4433754,0
4 - Tepito: -99.1233194,19.4425205,0
5 - Morelos: -99.1182554,19.4389745,0
6 - San Lazaro: -99.1148007,19.4302734,0
7 - Ricardo Flores Magon: -99.1036642,19.436607,0
8 - Romero Rubio: -99.0943193,19.4408057,0
9 - Oceania: -99.0871739,19.4457529,0
10 - Deportivo Oceania: -99.079417,19.450963,0
11 - Bosque de Aragon: -99.0692568,19.4581051,0
12 - Villa de Aragon: -99.0613174,19.4616861,0
13 - Nezahualcoyotl: -99.0545368,19.4730559,0
14 - Impulsora: -99.0488827,19.4858612,0
15 - Rio de los Remedios: -99.0466619,19.4909688,0
16 - Muzquiz: -99.041968,19.5017045,0
17 - Tecnologico: -99.0359974,19.5153316,0
18 - Olimpica: -99.0333796,19.5213181,0
19 - Plaza Aragon: -99.0301716,19.5284976,0
20 - Ciudad Azteca: -99.027347266674,19.5344532308002,0


```


## Etapa 2

Basándose en la etapa anterior, crear un programa que a partir de los nombres de un par de estaciones, te de instrucciones precisas para trasladarte de una estación a otra, incluyendo todos los detalles necesarios para cada segmento de la ruta en caso de que la ruta se componga de varios segmentos.

Para cada segmento debe indicar:

- Línea a la que corresponde el segmento.
- Estación de origen.
- Estación destino.
- Número de estaciones que hay que viajar.


### Ejemplo 1

Introducir los nombres de las estaciones sin acento (de preferencia).

Base

```
python etapa2.py tu_archivo.kml estacion_origen estacion_destino
```

Entrada

```
python etapa2.py Metro_CDMX.kml guerrero garibaldi
```

Salida


```
Linea B - Dirección: Ciudad Azteca
-------------------------------
Inicio: guerrero
Fin: garibaldi
```


### Ejemplo 2

Introducir los nombres de las estaciones sin acento (de preferencia).


Entrada

```
python etapa2.py Metro_CDMX.kml Eugenia Zaragoza
```

Salida


```
Linea 3 - Dirección: Indios Verdes
-------------------------------
Inicio: Eugenia
Fin: Balderas

-------------------------------
Transbordar
-------------------------------


Linea 1 - Dirección: Pantitlán
-------------------------------
Inicio: Balderas
Fin: Zaragoza

```

# Notas
1. Se quitan los acentos.

