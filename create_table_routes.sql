--DROP TABLE raw_routes;
CREATE TABLE raw_routes
(
id INTEGER PRIMARY KEY,
airline VARCHAR(250), 
airline_id INTEGER, 
src_airport VARCHAR(250), 
src_airport_id INTEGER, 
dst_airport VARCHAR(250), 
dst_airport_id INTEGER, 
codeshare VARCHAR(5), 
stops INTEGER, 
airplane VARCHAR(50), 
airlines_id INTEGER, 
airports_id INTEGER, 
airports_id1 INTEGER, 
airports_id2 INTEGER, 
airports_id3 INTEGER
);