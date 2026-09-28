from datetime import datetime

class Transaction:
    def __init__(self):
        self.transactions = {}


    def set_transaction(self, fuel_cost: float, fuel_type: str, fuel_amount: float):
        self.transactions[f"{datetime.now()}"] = {f"N{fuel_type}": {"litre": fuel_amount,
                                                                  "Cost": fuel_cost}}

    def get_transactions(self):
        output = ""
        for key, value in self.transactions.items():
            output += f"{key}: {value}\n"
        return output

