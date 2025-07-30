import json

with open("airports.json", mode="r", encoding="utf-8") as read_file:
    airports_data = json.load(read_file)

csv_file = open("airports.csv", mode="w", encoding="utf-8")
csv_file.write("id, airport, city, country, iata, icao, latitude, longitude, elevation, utc, dst, region\n")

for airport in airports_data:
    row_data = [
        str(airport.get("id", "")),
        str(airport.get("airport", "")).replace(",", ";"),
        str(airport.get("city", "")).replace(",", ";"),
        str(airport.get("country", "")),
        str(airport.get("iata", "")),
        str(airport.get("icao", "")),
        str(airport.get("latitude", "")),
        str(airport.get("longitude", "")),
        str(airport.get("elevation", "")),
        str(airport.get("utc", "")),
        str(airport.get("dst", "")),
        str(airport.get("region", ""))
    ]
    csv_line = ",".join(row_data) + "\n"
    csv_file.write(csv_line)

print(airports_data)

#for airport in airports_data:
    #print (f'id: {airline["id"]}, name: {airline["name"]}')
    #csv_file.write (f'{airport["id"]},{airport["airport"]},{airport["city"]},'
                   # f'{airport["country"]},{airport["iata"]},{airport["icao"]},{airport["latitude"]},{airport["longitude"]},'
                   # f'{airport["elevation"]},{airport["utc"]},{airport["dst"]},{airport["region"]}\n')
