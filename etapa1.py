from lxml import etree as ET
#from .functions import string_to_list

tree = ET.parse("./data/Metro_CDMX_Clean.xml")




coordinates = tree.xpath("/Document/Folder[1]/Placemark")

names = tree.xpath("/Document/Folder[2]/Placemark")


def string_to_list(your_str):
    out = []
    buff = []
    for c in your_str:
        if c == '\n':
            out.append(''.join(buff))
            buff = []
        else:
            buff.append(c)
    else:
        if buff:
            out.append(''.join(buff))

    res = []
    for item in out:
        res.append(item.strip())


    return res
  

def get_line_coordinates(coordinates):
    res = []
    for element in coordinates:
        name = element.find("name").text
        coordinates_str = element.find("LineString").find("coordinates").text
        coordinates_lines = string_to_list(coordinates_str)
        #print(f"name: {name} \n coordinates: {coordinates_arr}")

        obj = {
            "subway": name,
            "coordinates_lines": coordinates_lines
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
        # print(obj)
        name_coordinate.append(obj)
    return name_coordinate


#


# Subway line with its stations in coordinates
lines_stations_in_coordinates = get_line_coordinates(coordinates)

"""

"""

# Subway station with its coordinates
stations = get_name_coordinate(names)


def join_data():

    data = []
    for line in stations:
        station = line["station"]
        coordinate = line["coordinate"]
        
        
        for idx_station, obj in enumerate(lines_stations_in_coordinates):
            subway = obj["subway"] # <=== static
            coordinates_lines = obj["coordinates_lines"]

            # print(coordinates_lines)
            
            code = 0
            try:
                idx = coordinates_lines.index(coordinate)

                obj_station = {
                    "subway": subway.split(" ")[1],
                    "station": station,
                    "coordinate": coordinate
                }
                
                data.append(obj_station)
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
  for item in data:
    if item["subway"] not in thisdict:
      thisdict[f"{item['subway']}"] = []
  return thisdict


def order_data(data):
  key_stations = get_stations(data)
  stations = []
  
  for key in key_stations:

    for item in data:
      if item["subway"] == key:
        # print("ok")
        key_stations[key].append(item)
  return key_stations

data = join_data()


key_stations = get_stations(data)
for line_name in key_stations:
  list_found = order_data(data)[line_name]
  print(f"\nLinea {line_name}")
  for item in list_found:
    station = item["station"]
    coordinate = item["coordinate"]

    print(f"{station}: {coordinate}")