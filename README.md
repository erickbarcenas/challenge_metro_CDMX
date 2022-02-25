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
1. Convertir el archivo kml a xml por medio de una
página https://anyconv.com/es/convertidor-de-kml-a-xml/ 

