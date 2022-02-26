#!/usr/bin/python

import sys
#from lxml import etree as ET
from functions.common_etapa1 import etapa1

if len(sys.argv) == 4:
    inputs = list(sys.argv)

    filename = inputs[1]
    start = inputs[2]
    end = inputs[3]

    #print("-------------------------------")
    subway_network = etapa1(show_text=0)

    keys_subway_network = list(subway_network.keys())

    inputs = [start, end]

    for value_idx, value in enumerate(inputs):
        for idx, line in enumerate(list(subway_network.values())):
            for station in line:
                if station[1].lower() == value.lower():
                    print(f"------ Linea {keys_subway_network[idx]} ------ ")
                    if value_idx == 0:
                        print(f"Origen: {value}")
                    else:
                        print(f"Destino: {value}")
            # print(line)

    print("-------------------------------")

    #find(filename, xpath)

    
    

else:
    print("The number of arguments is invalid, please check the documentation!")
