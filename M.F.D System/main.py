from fuel_station import FuelStation
from fuel_storage import FuelStorage
from transaction import Transaction

def main():
    input("Press any key to begin...")

    station = FuelStation()
    in_station = True
    while in_station:
        print(station.view_fuel_menu())
        break


if __name__ == "__main__":
    main()