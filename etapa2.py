#!/usr/bin/python

import sys
#from lxml import etree as ET



if len(sys.argv) == 4:
    data = list(sys.argv)

    filename = data[1]
    start = data[2]
    end = data[3]

    #print("-------------------------------")
    print("Linea B")
    print("-------------------------------")

    print(f"Inicio: {start}")
    print(f"Fin: {end}")

    print("-------------------------------")

    #find(filename, xpath)

else:
    print("The number of arguments is invalid, please check the documentation!")
