import transaction
import fuel_storage
from datetime import datetime


class FuelStation:
    def __init__(self):
        self.fuel_types = {"Petrol": 1400,
                           "Diesel": 1900,
                           "Kerosene": 2458,
                           "Natural Gas": 380
                           }
        self.transactions = transaction.Transaction()
        self.storage = fuel_storage.FuelStorage()

    def view_fuel_menu(self):
        fuel_menu = ("=================\n"
                     "FUEL STATION MENU\n"
                     "=================\n\n")
        fuel_numbering = 1
        for fuel_type, fuel_rate in self.fuel_types.items():
            fuel_menu += f"({fuel_numbering}) {fuel_type}: {fuel_rate}\n"
            fuel_numbering += 1
        return fuel_menu


    def convert_litres_to_price_paid(self, litres: float, fuel_type: str):
        return litres * self.fuel_types[f"{fuel_type}"]

    def buy_petrol(self, price_paid: float):
        if price_paid >= self.fuel_types["Petrol"]:
            litres_of_petrol = price_paid / self.fuel_types["Petrol"]

            if self.storage.fuel_litres_available["Petrol"] >= litres_of_petrol > 0 <= 50:
                self.storage.fuel_litres_available["Petrol"] -= litres_of_petrol
                self.transactions.set_transaction(price_paid, "Petrol", litres_of_petrol)

                return self.generate_receipt(price_paid, "Petrol", litres_of_petrol)
            else:
                return "We're out of petrol until further notice. We apologize for any inconvenience caused by this."
        else:
            return f"Amount must be above the price of {self.fuel_types['Petrol']}/litre for Petrol."

    def buy_diesel(self, price_paid: float):
        if price_paid >= self.fuel_types["Diesel"]:
            litres_of_diesel = price_paid / self.fuel_types["Diesel"]
            if self.storage.fuel_litres_available["Diesel"] >= litres_of_diesel > 0 <= 50:
                self.storage.fuel_litres_available["Diesel"] -= litres_of_diesel
                self.transactions.set_transaction(price_paid, "Diesel", litres_of_diesel)

                return self.generate_receipt(price_paid, "Diesel", litres_of_diesel)
            else:
                return "We're currently out of Diesel until further notice. We apologize for any inconvenience caused by this."
        else:
            return f"Amount must be above the price of {self.fuel_types['Diesel']}/litre for diesel."

    def buy_kerosene(self, price_paid: float):
        if price_paid >= self.fuel_types["Kerosene"]:
            litres_of_kerosene = price_paid / self.fuel_types["Kerosene"]
            if self.storage.fuel_litres_available["Kerosene"] >= litres_of_kerosene > 0 <= 50:
                self.storage.fuel_litres_available["Kerosene"] -= litres_of_kerosene
                self.transactions.set_transaction(price_paid, "Kerosene", litres_of_kerosene)

                return self.generate_receipt(price_paid, "Kerosene", litres_of_kerosene)
            else:
                return "We're currently out of Kerosene until further notice. We apologize for any inconvenience caused by this."
        else:
            return f"Amount must be above the price of {self.fuel_types['Kerosene']}/litre for kerosene."

    def buy_natural_gas(self, price_paid: float):
        if price_paid >= self.fuel_types["Natural Gas"]:
            litres_of_natural_gas = price_paid / self.fuel_types["Natural Gas"]

            if self.storage.fuel_litres_available["Natural Gas"] >= litres_of_natural_gas > 0 <= 50:
                self.storage.fuel_litres_available["Natural Gas"] -= litres_of_natural_gas
                self.transactions.set_transaction(price_paid, "Natural Gas", litres_of_natural_gas)

                return self.generate_receipt(price_paid, "Natural Gas", litres_of_natural_gas)
            else:
                return "We are currently out of Natural Gas until further notice. We apoologize for any inconvenience caused by this."
        else:
            return f"Amount must be above the price of {self.fuel_types['Natural Gas']}/litre for natural-gas."

    
    def generate_receipt(self, price_paid: float, fuel_type: str, litre_amount: float):
        return (f"  {datetime.today()}\n"
                f"==============================\n"
                f"  OKOKO-BIOKO FILLING STATION\n"
                f"==============================\n"
                f"\n"
                f"Fuel Type: {fuel_type}\n"
                f"Fuel Amount: {litre_amount}\n"
                f"Amount Paid: {price_paid}\n\n"
                f"Thank you for your patronage\n"
                f"==============================\n"
                f"Saving Transaction...\n")
station = FuelStation()
