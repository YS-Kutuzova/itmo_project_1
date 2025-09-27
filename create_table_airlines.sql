--DROP TABLE raw_airlines;
CREATE TABLE raw_airlines
(
id INTEGER PRIMARY KEY,
name VARCHAR(250),
altname VARCHAR(250),
iata VARCHAR(5),
icao VARCHAR(5),
callsign VARCHAR(250),
country VARCHAR(250),
active boolean
);