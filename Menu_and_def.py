import psycopg2

def print_routes_data():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="FlightsPyProject",
            user="postgres",
            password="8852"
        )
        cursor = connection.cursor()

        query = """
        SELECT 
            raw_airlines.name AS airline_name,
            raw_airlines.active AS airline_active, 
            dep_airports.airport AS departure_airport_name, 
            dep_airports.city AS departure_city,
            dep_airports.country AS departure_country,
            arr_airports.airport AS arrival_airport_name,
            arr_airports.city AS arrival_city,
            arr_airports.country AS arrival_country,
            raw_routes.id AS route_number, 
            raw_routes.src_airport AS departure_airport_code,
            raw_routes.dst_airport AS arrival_airport_code,
            raw_routes.airplane AS airplane
        FROM raw_routes
        JOIN raw_airlines ON raw_routes.airline_id = raw_airlines.id
        JOIN raw_airports AS dep_airports ON raw_routes.src_airport_id = dep_airports.id
        JOIN raw_airports AS arr_airports ON raw_routes.dst_airport_id = arr_airports.id
        WHERE raw_airlines.active = TRUE
        ORDER BY raw_routes.id ASC
        LIMIT 80 OFFSET 30;
        """

        cursor.execute(query)
        routes = cursor.fetchall()
        return routes

    except Exception as error:
        print("Error with PostgreSQL:", error)
        return []
    finally:
        cursor.close()
        connection.close()

def display_all_flights(routes):

    print("\nAll flights:")
    print("-" * 150)
    print(
        f"{'№':<4} | {'Airlines':<20} | {'Departure':<30} | {'Arrival':<30} | "
        f"{'Codes':<12} | {'Airplane'}")
    print("-" * 150)

    for route in routes:
        route_number = route[8]
        airline_name = route[0]
        departure = f"{route[2]} ({route[3]}, {route[4]})"
        arrival = f"{route[5]} ({route[6]}, {route[7]})"
        airport_codes = f"{route[9]} → {route[10]}"
        airplane = route[11] if route[11] else "N/A"

        print(
            f"{route_number:<4} | {airline_name:<20} | {departure:<30} | "
            f"{arrival:<30} | {airport_codes:<12} | {airplane}")

    print("-" * 150)
    print(f"Всего рейсов: {len(routes)}")


def search_by_departure_city(routes):
    city = input("\nPlease enter a city of departure: ").strip()

    results = []
    for route in routes:
        if city.lower() in route[3].lower():
            results.append(route)

    display_search_results(results)

def search_by_airline(routes):
    airline = input("\nPlease enter an airline: ").strip()

    results = []
    for route in routes:
        if airline.lower() in route[0].lower():
            results.append(route)

    display_search_results(results)

def display_search_results(results):
    if not results:
        print("\nFlights are not found.")
        return

    print("\nSearch results:")
    print("-" * 150)
    print(
        f"{'№':<4} | {'Airlines':<20} | {'Departure':<30} | {'Arrival':<30} | "
        f"{'Codes':<12} | {'Airplane'}")
    print("-" * 150)

    for route in results:
        route_number = route[8]
        airline_name = route[0]
        departure = f"{route[2]} ({route[3]}, {route[4]})"
        arrival = f"{route[5]} ({route[6]}, {route[7]})"
        airport_codes = f"{route[9]} → {route[10]}"
        airplane = route[11] if route[11] else "N/A"

        print(
            f"{route_number:<4} | {airline_name:<20} | {departure:<30} | "
            f"{arrival:<30} | {airport_codes:<12} | {airplane}")

    print("-" * 150)
    print(f"The number of flights: {len(results)}")


def show_menu():
    print("\n" + "=" * 50)
    print("MENU".center(50))
    print("=" * 50)
    print("1. Show all routes/flights")
    print("2. Search a city of departure")
    print("3. Search an airline")
    print("4. Exit")
    print("=" * 50)

def main():
    routes = print_routes_data()
    if not routes:
        print("Please check DB connection")
        return

    while True:
        show_menu()
        choice = input("Please choose (1-4): ").strip()

        if choice == "1":
            display_all_flights(routes)
        elif choice == "2":
            search_by_departure_city(routes)
        elif choice == "3":
            search_by_airline(routes)
        elif choice == "4":
            print("\nBye-bye!")
            break
        else:
            print("\nChoose the number from 1 to 4")

        input("\nPress 'Enter' to continue...")

if __name__ == "__main__":
    main()