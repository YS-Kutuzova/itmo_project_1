COPY raw_routes(id, airline, airline_id, src_airport, src_airport_id, dst_airport, dst_airport_id, codeshare, stops, airplane, airlines_id, 
airports_id, airports_id1, airports_id2, airports_id3)
FROM 'C:\Users\Kseniia\PycharmProjects\itmo_project_1\routes.csv'
DELIMITER ','
CSV HEADER;