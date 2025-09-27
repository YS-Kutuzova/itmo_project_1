COPY raw_airlines(id, name, altname, iata, icao, callsign, country, active)
FROM 'C:\Users\Kseniia\PycharmProjects\itmo_project_1\airlines.csv'
DELIMITER ','
CSV HEADER;