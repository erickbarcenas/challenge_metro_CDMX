#!/usr/bin/python

import sys
import pandas as pd
import numpy as np
import networkx as nx

#from lxml import etree as ET
from functions.common_etapa1 import etapa1
from functions.common_etapa2 import get_details_direction, show_datails

from functions.common_etapa2 import create_dict_key_stations, create_dataframe

if len(sys.argv) == 4:
    inputs = list(sys.argv)

    filename = inputs[1]
    start = inputs[2]
    end = inputs[3]

    #print("-------------------------------")
    subway_network = etapa1(show_text=0)

    inputs = [start, end]
    res = get_details_direction(inputs, subway_network)

    start_details = res["start"]
    show_datails(start_details, str_param="Origen")

    
    #df = pd.read_excel('metro.xlsx')
    print("\n----  Estaciones intermedias ----")
    #
    key_stations = create_dict_key_stations(subway_network, type_return="list")
    df = create_dataframe(key_stations)
    
    METRO = nx.from_pandas_edgelist(df,source='Origen',target='Destino') #edge_attr='Longitud de interestación'
    djk_path= nx.dijkstra_path(METRO, source=start, target=end ) #weight='Longitud de interestación'
    
    djk_path.pop()
    djk_path.reverse()
    djk_path.pop()
    #print(djk_path)
    djk_path.reverse()

    for station in djk_path:
        print(station)
    


    end_details = res["end"]
    show_datails(end_details, str_param="Destino")
    print("-------------------------------")

    #find(filename, xpath)

    
    

else:
    print("The number of arguments is invalid, please check the documentation!")
