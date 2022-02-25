# Mexico City Metro Challenge

El reto consiste en crear un servicio para usar el sistema de transporte metro dentro de la CDMX.

Deberá instalar python si aún no lo ha hecho.
Después instalar lo requerimientos.

```
pip install -r requirements.txt
```

Se compone de 2 etapas sucesivas.

## Etapa 1

A partir el archivo .kml proporcionado, obtener la descripción de la todas las líneas del metro. Cada línea tiene un nombre y una lista de estaciones. Cada estación tiene un nombre y unas coordenadas geográficas (latitud y longitud). 

### Ejemplo

Entrada
```
python etapa1.py Metro_CDMX.kml
```

Salida
```
Linea A
1 - Pantitlan: -99.0722072,19.4153591,0
2 - Agricola Oriental: -99.0698737,19.4047948,0
3 - Canal de San Juan: -99.0593863,19.3987332,0
4 - Tepalcates: -99.0463722,19.3912849,0
5 - Guelatao: -99.0356326,19.3851316,0
6 - Penon Viejo: -99.0170825,19.3733205,0
7 - Acatitla: -99.0056777,19.3647171,0
8 - Santa Maria: -98.9952278137207,19.3613566081823,0
9 - Los Reyes: -98.9768708,19.3590285,0
10 - La Paz: -98.9609921,19.3506572,0
...
...
...
Linea 9
1 - Tacubaya: -99.187097,19.4031605,0
2 - Patriotismo: -99.1788948,19.4062317,0
3 - Chilpancingo: -99.1684502,19.406171,0
4 - Centro Medico: -99.1552055,19.4066618,0
5 - Lazaro Cardenas: -99.1448736,19.407021,0
6 - Chabacano: -99.1357434,19.4084883,0
7 - Jamaica: -99.1217637,19.4091258,0
8 - Mixiuhca: -99.1128802,19.4085693,0
9 - Velodromo: -99.1030419,19.4085693,0
10 - Ciudad Deportiva: -99.0912294,19.4084529,0
11 - Puebla: -99.0824747,19.4072234,0
12 - Pantitlan: -99.0722072,19.4153591,0

```


## Etapa 2

Basándose en la etapa anterior, crear un programa que a partir de los nombres de un par de estaciones, te de instrucciones precisas para trasladarte de una estación a otra, incluyendo todos los detalles necesarios para cada segmento de la ruta en caso de que la ruta se componga de varios segmentos.

Para cada segmento debe indicar:

- Línea a la que corresponde el segmento.
- Estación de origen.
- Estación destino.
- Número de estaciones que hay que viajar.


### Ejemplo

```
python etapa2.py Metro_CDMX.kml origen destino
```

# Notas
1. Se quitan los acentos.

