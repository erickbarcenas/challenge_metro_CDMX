import sys
from lxml import etree as ET


from functions.text import simplify
from functions.string_to_list import string_to_list

# Get the name of the line and the list of coordinates of each station
def get_line_coordinates(coordinates):
    res = []
    for element in coordinates:
        name = element.find("name").text
        coordinates_str = element.find("LineString").find("coordinates").text
        coordinates_lines = string_to_list(coordinates_str)
        #print(f"name: {name} \n coordinates: {coordinates_arr}")

        # add index to coordinate
        """
        obj_list_with_idx = []
        for idx, item in enumerate(coordinates_lines):
            build = {
                'index': idx,
                'coordinates': obj_list_with_idx
            }
            obj_list_with_idx.append(build)
        """



        obj = {
            "subway": name, # station name
            "coordinates_lines": coordinates_lines # Coordinate array
        }

        res.append(obj)
    return res



def get_name_coordinate(names):
    name_coordinate = []

    for element in names:
        name = element.find("name").text
        coordinate = element.find("Point").find("coordinates").text

        obj = {
            "station": name,
            "coordinate": str(coordinate).strip()
        }
        #print(obj)
        name_coordinate.append(obj)
    return name_coordinate




def join_data():

    tree = ET.parse(sys.argv[1])
    # tree = ET.parse("./data/Metro_CDMX_Clean.xml")

    coordinates = tree.xpath("/Document/Folder[1]/Placemark")

    names = tree.xpath("/Document/Folder[2]/Placemark")

    # Subway line with its stations in coordinates
    lines_stations_in_coordinates = get_line_coordinates(coordinates)

    # Subway station with its coordinates
    stations = get_name_coordinate(names)

    data = []
    for line in stations:
        station = line["station"]  # nombre de la estación
        coordinate = line["coordinate"] # coordenada de la estación
        
        
        for idx_station, obj in enumerate(lines_stations_in_coordinates):  # linea del metro
            subway = obj["subway"] # <=== static
            coordinates_lines = obj["coordinates_lines"]  # arreglo de coordenadas

            #index = coordinates_lines["index"]
            #coordinates = coordinates_lines["coordinates"]


            # print(coordinates_lines)
            
            code = 0
            try:
                idx = coordinates_lines.index(coordinate)

                """
                obj_station = {
                    "subway": subway.split(" ")[1],
                    "position": idx,
                    "station": station,
                    "coordinate": coordinate
                }
                """

                # creating a tuple
                # subway | position | station | coordinate

                tuple_station = (subway.split(" ")[1], idx, station, coordinate,)
                
                data.append(tuple_station)
                """
                for item in coordinates_lines:
                    if item == :
                        code = 200
                        print(code)
                    else:
                        pass
                """

            except Exception as ex:
                #code = 404
                #print(code)
                pass
            
        
        #print(station, coordinate)

        #station_coordinates.coordinate.index(station)

    return data

def get_stations(data):
  thisdict = {}
  #data is a tuple
  # subway | position | station | coordinate

  for item in data:
    if item[0] not in thisdict:
      thisdict[f"{item[0]}"] = []
  return thisdict


# metro stations are added to the keys of a dictionary in the form of an array
def order_data(data):

    # data is a tuple
    # subway | position | station | coordinate

    key_stations = get_stations(data)
  
    for key in key_stations:

        for item in data:
            if item[0] == key:
            # print("ok")
                key_stations[key].append(item)
                
    

    res = []
    for key in key_stations:
        
        key_stations[key] = sorted(key_stations[key], key=lambda line_list: line_list[1])
        #print()
        #key_stations = 
        

    
    #sort_key_stations = sorted(key_stations, key=lambda line_list: line_list[1])
    # 
    #print(key_stations)
    return key_stations










def etapa1(show_text):

    data = join_data()
    #key_stations = get_stations(data)
    key_stations = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '12': [], 'A': [], 'B': []}
    #print(key_stations)

    # demo = []
    for line_name in key_stations:
        list_found = order_data(data)[line_name]
        
        #pass
        #print(list_found)# .sort()
        
        if show_text == 1:
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
            
            if show_text == 1:
                print(f"{position} - {station}: {coordinate}")
                pass
            else:
                pass
        #"""

        key_stations[line_name] = temp_list_stations



        #demo.append(tt)

    return key_stations