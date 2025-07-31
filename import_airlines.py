import json
import re

"""
Unfortunately deleted
"""


with open("airlines.json", mode="r", encoding="utf-8") as read_file:
    airlines_data = json.load(read_file)

csv_file = open("airlines.csv", mode="w", encoding="utf-8")
csv_file.write("id,name,altname,iata,icao,callsign,country,active\n")

for airline in airlines_data:
    for key,value in airline.items():
        #if value == '\\N' or value == '..,':
        if value == '\\N' or (type(value) == str and len(re.findall(r'[\.,]{2,}', value)) > 0):
            airline[key] = ''

print(airlines_data)

for airline in airlines_data:
    #print (f'id: {airline["id"]}, name: {airline["name"]}')
    csv_file.write (f'{airline["id"]},{airline["name"]},{airline["alt_name"]},'
                    f'{airline["iata"]},{airline["icao"]},{airline["callsign"]},{airline["country"]},{airline["active"]}\n')
