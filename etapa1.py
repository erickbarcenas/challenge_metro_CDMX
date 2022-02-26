#!/usr/bin/python
# -*- coding: utf-8 -*-



from functions.text import simplify


from functions.common_etapa1 import get_line_coordinates, get_name_coordinate, join_data, get_stations, order_data



def etapa1():

    data = join_data()
    #key_stations = get_stations(data)
    key_stations = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '12': [], 'A': [], 'B': []}
    #print(key_stations)

    # demo = []
    for line_name in key_stations:
        list_found = order_data(data)[line_name]
        
        #pass
        #print(list_found)# .sort()
        
        print(f"\nLinea {line_name}")

        

        temp_list_stations = []

        

        for item in list_found:
            # data is a tuple
            # subway | position | station | coordinate
            position = item[1]#item["position"]
            station = simplify(item[2]) #item["station"]
            coordinate = item[3] #item["coordinate"]

            
            temp_station = (position, station, coordinate)
            temp_list_stations.append(temp_station)
            print(f"{position} - {station}: {coordinate}")
        #"""

        key_stations[line_name] = temp_list_stations



        #demo.append(tt)

    return key_stations

        

etapa1()

