DROP TABLE raw_airports;
CREATE TABLE raw_airports
(
id INTEGER PRIMARY KEY,
airport VARCHAR(250),
city VARCHAR(250),
country VARCHAR(250),
iata VARCHAR(5),
icao VARCHAR(5),
latitude NUMERIC(9,6),
longitude NUMERIC(9,6),
elevation INTEGER,
utc INTEGER,
dst VARCHAR (5),
region VARCHAR (250)
);