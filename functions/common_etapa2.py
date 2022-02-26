def get_details_direction(inputs, subway_network):

  keys_subway_network = list(subway_network.keys())
  values_subway_network = list(subway_network.values())

  result_start = {}
  result_end = {}

  # inputs = ["Copilco", "Universidad"]

  for value_idx, value in enumerate(inputs): # subway stations given as input
    for idx, line in enumerate(values_subway_network): # list with all metro stations
      for station in line: # list with all stations on the line
        if station[1].lower() == value.lower(): # 
                                                # find the line given as input
          
          
          
          with_direction = ""
          if 1:
            with_direction_right = values_subway_network[idx][-1][1]
            with_direction = with_direction_right
          else:
            with_direction_left = values_subway_network[idx][-1][1]
            with_direction = with_direction_left

          key_line = keys_subway_network[idx]
          idx_station = station[0]

          station_id = station[0]

          if value_idx == 0:

            result_start["line_number"] = keys_subway_network[idx]
            result_start["direction"] = ""
            result_start["station"] = value
            result_start["station_id"] = station_id
            

            # print(f"\nLinea {keys_subway_network[idx]} - Direccion: {with_direction}  ------ ")
            # print(f"Origen: {value}")
          elif value_idx == 1:
            
            result_end["line_number"] = keys_subway_network[idx]
            result_end["direction"] = ""
            result_end["station"] = value
            result_end["station_id"] = station_id

            # print(f"\nLinea {keys_subway_network[idx]} - Direccion: {with_direction}  ------ ")
            # print(f"Destino: {value}")
          # print(line)

  if result_start["line_number"] == result_end["line_number"]:
    # show direction
    # print("show direction")
    direction = ""
    if result_start["station_id"] < result_end["station_id"]:
      # print("right")
      direction = subway_network[result_end['line_number']][-1][1]
      result_start["direction"] = direction

    if result_start["station_id"] > result_end["station_id"]:
      #print("left")
      direction = subway_network[result_start['line_number']][0][1]
      result_start["direction"] = direction

  return {
      "start": result_start,
      "end": result_end
  }


def show_datails(details, str_param):
  with_direction = details["direction"]

  line_number = details["line_number"]
  station = details["station"]

  complement = ''
  if len(with_direction) > 0:
    complement = f"- Direccion: {with_direction}"

  print(f"\nLinea {line_number} {complement}")
  print(f"{str_param}: { station }")


# -------------------------------------------------------

def create_couples(list_stations):
  couples = []
  for idx, item in enumerate(list_stations):

    if idx + 1 < len(list_stations):
      couple = [list_stations[idx][1], list_stations[idx + 1][1]]
      couples.append(couple)
  return couples

def create_couple(list_stations):
  couples = []
  for idx, item in enumerate(list_stations):

    if idx + 1 < len(list_stations):
      couple = [list_stations[idx][1], list_stations[idx + 1][1]]
      couples.append(couple)
  return couples

def create_dict_key_stations(subway_network, type_return):

  key_stations = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '12': [], 'A': [], 'B': []}
  lits_stations = []

  for key_line in key_stations:
    #for station in subway_network[key_line]:
    couples = create_couples(subway_network[key_line])
    if type_return == "dict":
      key_stations[key_line] = couples
    else:
      lits_stations.append(couples)

  if type_return == "dict":
      return key_stations
  else:
      return lits_stations
  

def create_dataframe(key_stations):
  import pandas as pd
  data_cleaned = []
  for list_pairs in key_stations:
    for item in list_pairs:
      data_cleaned.append(item)

  return pd.DataFrame(data_cleaned, columns = ['Origen', 'Destino'])