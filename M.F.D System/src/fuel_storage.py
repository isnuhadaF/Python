

class FuelStorage:
    def __init__(self):
        self.fuel_litres_available = {"Petrol": 500000,
                           "Diesel": 300000,
                           "Kerosene": 150000,
                            "Natural Gas": 200000,
                                      }
    def view_storage(self):
        return (f"====================\n"
                f"AVAILABLE FUEL TYPES\n"
                f"====================\n\n"
                f"Petrol : {self.fuel_litres_available["Petrol"]}\n"
                f"Diesel : {self.fuel_litres_available["Diesel"]}\n"
                f"kerosene  : {self.fuel_litres_available["Kerosene"]}\n"
                f"Natural Gas : {self.fuel_litres_available["Natural Gas"]}\n")

