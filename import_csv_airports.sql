COPY raw_airports(id, airport, city, country, iata, icao, latitude, longitude, elevation, utc, dst, region)
FROM 'C:\Users\Kseniia\PycharmProjects\itmo_project_1\airports.csv'
DELIMITER ','
CSV HEADER;