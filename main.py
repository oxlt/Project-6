import os

# File name for the list of vehicles
VEHICLE_FILE = "AllowedVehiclesList.txt"

# Initialize file if it does not exist
def initialize_vehicle_file():
    if not os.path.exists(VEHICLE_FILE):
        default_vehicles = [
            "Ford F-150",
            "Chevrolet Silverado",
            "Tesla CyberTruck",
            "Toyota Tundra",
            "Rivian R1T",
            "Ram 1500"
        ]
        with open(VEHICLE_FILE, "w") as file:
            file.writelines(f"{vehicle}\n" for vehicle in default_vehicles)

# Load vehicles from the file into a list
def load_vehicles():
    with open(VEHICLE_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

# Save the list of vehicles back to the file
def save_vehicles(vehicles):
    with open(VEHICLE_FILE, "w") as file:
        file.writelines(f"{vehicle}\n" for vehicle in vehicles)

# Function to print all authorized vehicles
def print_vehicles():
    vehicles = load_vehicles()
    print("\nAuthorized Vehicles:")
    for vehicle in vehicles:
        print(f"- {vehicle}")
    print()

# Function to search for a specific vehicle
def search_vehicle():
    vehicles = load_vehicles()
    vehicle_name = input("Please enter the vehicle name to search for: ").strip()
    if vehicle_name in vehicles:
        print(f'"{vehicle_name}" is an authorized vehicle.\n')
    else:
        print(f'"{vehicle_name}" is NOT an authorized vehicle.\n')

# Function to add a new vehicle
def add_vehicle():
    vehicles = load_vehicles()
    new_vehicle = input("Please enter the vehicle name to add: ").strip()
    if new_vehicle in vehicles:
        print(f'"{new_vehicle}" is already in the list of authorized vehicles.\n')
    else:
        vehicles.append(new_vehicle)
        save_vehicles(vehicles)
        print(f'"{new_vehicle}" has been added to the list of authorized vehicles.\n')

# Function to delete an existing vehicle
def delete_vehicle():
    vehicles = load_vehicles()
    vehicle_name = input("Please enter the vehicle name to delete: ").strip()
    if vehicle_name not in vehicles:
        print(f'"{vehicle_name}" is not in the list of authorized vehicles.\n')
    else:
        confirmation = input(f'Are you sure you want to remove "{vehicle_name}" from the Authorized Vehicles List? (yes/no): ').strip().lower()
        if confirmation == "yes":
            vehicles.remove(vehicle_name)
            save_vehicles(vehicles)
            print(f'"{vehicle_name}" has been removed from the list of authorized vehicles.\n')
        else:
            print(f'"{vehicle_name}" was not removed from the list.\n')

# Main function to display the menu and handle user choices
def main():
    initialize_vehicle_file()
    while True:
        print("""
********************************
AutoCountry Vehicle Finder v0.5
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. DELETE Authorized Vehicle
5. Exit
********************************
        """)
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            print_vehicles()
        elif choice == "2":
            search_vehicle()
        elif choice == "3":
            add_vehicle()
        elif choice == "4":
            delete_vehicle()
        elif choice == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input. Please try again.\n")

# Entry point of the program
if __name__ == "__main__":
    main()
