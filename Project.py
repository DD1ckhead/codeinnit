class FlightBookingSystem:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight_number, current_airport, aircraft_num, airline_name, aircraft_code, distance, speed, arrival_time):
        self.flights[flight_number] = {
            'current_airport': current_airport,
            'aircraft_num': aircraft_num,
            'airline_name': airline_name,
            'aircraft_code': aircraft_code,
            'distance': int(distance),
            'speed': int(speed),
            'arrival_time': arrival_time,
            }

        def search_flights(self, choice, value):
            matching_flights = []
            for flight_number, flight_info in self.flights.items():
                if str(flight_info.get(choice)) == value:
                    matching_flights.append((flight_number, flight_info))
                    return matching_flights

                
def display_flight_info(flight_number, flight_info):
    print(f"Flight Number: {flight_number}")
    for key, value in flight_info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print()

def main():
    flight_system = FlightBookingSystem()

    
    flight_system.add_flight('F1001', 'JFK', 'A101', 'Delta', 'B777', '5000', '800', '18:00')
    flight_system.add_flight('F1002', 'LAX', 'A102', 'American Airlines', 'A380', '6000', '800', '20:00')
    flight_system.add_flight('F1003', 'ORD', 'A103', 'United Airlines', 'B787', '7000', '850', '22:00')

    while True:
        print("1. Search Flights by Flight Number")
        print("2. Search Flights by Current Airport")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            flight_number = input("Enter the flight number: ")
            matching_flights = flight_system.search_flights('flight_number', flight_number)
            if matching_flights:
                for flight_number, flight_info in matching_flights:
                    display_flight_info(flight_number, flight_info)
            else:
                print("No matching flights found.")
        elif choice == '2':
            current_airport = input("Enter the current airport: ")
            matching_flights = flight_system.search_flights('current_airport', current_airport)
            if matching_flights:
                for flight_number, flight_info in matching_flights:
                    display_flight_info(flight_number, flight_info)
            else:
                print("No matching flights found.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
