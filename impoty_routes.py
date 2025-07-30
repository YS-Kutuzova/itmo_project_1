import json

with open("routes.json", mode="r", encoding="utf-8") as read_file:
    routes_data = json.load(read_file)

csv_file = open("routes.csv", mode="w", encoding="utf-8")
csv_file.write("id,airline,airline_id,src_airport,src_airport_id,dst_airport,dst_airport_id,"
               "codeshare,stops,airplane,airlines_id,airports_id,airports_id1,airports_id2,airports_id3\n")

current_id = 1

for route in routes_data:
    csv_line = (
        f"{current_id}," 
        f"{route.get('airline', '')},"
        f"{route.get('airline_id', '')},"
        f"{route.get('src_airport', '')},"
        f"{route.get('src_airport_id', '')},"
        f"{route.get('dst_airport', '')},"
        f"{route.get('dst_airport_id', '')},"
        f"{route.get('codeshare', '')},"
        f"{route.get('stops', '')},"
        f"{route.get('airplane', '')},"
        f"{route.get('airlines_id', '')},"
        f"{route.get('airports_id', '')},"
        f"{route.get('airports_id1', '')},"
        f"{route.get('airports_id2', '')},"
        f"{route.get('airports_id3', '')}"
    )

    csv_file.write(csv_line + "\n")
    current_id += 1

print(routes_data)
