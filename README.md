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

```
python etapa1.py
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
python etapa2.py
```

# Notas
1. Convertir el archivo kml a xml por medio de una
página https://anyconv.com/es/convertidor-de-kml-a-xml/ 

