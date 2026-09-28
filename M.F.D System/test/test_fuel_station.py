import unittest
from fuel_station import FuelStation


class TestFuelStationSingleFuel(unittest.TestCase):
    """Focused tests against Petrol only, to work out the pattern
    before applying it across all four fuel types below."""

    def setUp(self):
        # fresh station before every test — stock and transaction
        # history must never leak between test cases
        self.station = FuelStation()

    # --- WORKED EXAMPLE ---------------------------------------------
    def test_buy_petrol_rejects_price_below_fuel_price(self):
        result = self.station.buy_petrol(100)  # petrol is 1400/litre
        self.assertIn("must be above the price", result)
        # a rejected purchase must not touch stock at all
        self.assertEqual(
            self.station.storage.fuel_litres_available["Petrol"], 500000
        )
    # ------------------------------------------------------------------

    def test_buy_petrol_accepts_price_exactly_equal_to_fuel_price(self):
        # TODO: price_paid == 1400 should SUCCEED (boundary is >=, not >)
        # — this is the boundary bug that showed up as an inconsistency
        # between buy_petrol and the other three methods earlier.
        pass

    def test_buy_petrol_rejects_negative_price(self):
        # TODO: buy_petrol(-500) — should land in the same "too low"
        # rejection branch as any other value below the price, not crash.
        pass

    def test_buy_petrol_succeeds_and_decrements_stock_correctly(self):
        # TODO: buy_petrol(2800) → 2 litres exactly.
        # Assert: stock dropped by exactly 2, a transaction got recorded
        # (check len(self.station.transactions.transactions) == 1),
        # and the return value is a string containing "Petrol".
        pass

    def test_buy_petrol_rejects_when_stock_is_insufficient(self):
        # TODO: manually shrink stock first —
        # self.station.storage.fuel_litres_available["Petrol"] = 1
        # then buy more litres than that. Assert the "out of petrol"
        # message comes back, and stock is unchanged.
        pass

    def test_buy_petrol_boundary_exact_remaining_stock(self):
        # TODO: set stock to exactly the litres this purchase needs,
        # confirm the purchase still SUCCEEDS (>=, not >) — this is
        # the same boundary idea as the price check, but on the stock
        # side instead.
        pass


class TestFuelStationAllFuelTypes(unittest.TestCase):
    """Same core behaviours as above, run once per fuel type via
    subTest instead of being copy-pasted four times — the tests
    shouldn't repeat the duplication problem the buy_x methods have."""

    def setUp(self):
        self.station = FuelStation()
        self.buy_methods = {
            "Petrol": self.station.buy_petrol,
            "Diesel": self.station.buy_diesel,
            "Kerosene": self.station.buy_kerosene,
            "Natural Gas": self.station.buy_natural_gas,
        }

    def test_all_fuels_reject_price_below_their_own_rate(self):
        # TODO: loop fuel_type, buy over self.buy_methods.items(),
        # use self.station.fuel_types[fuel_type] to get the real price,
        # call buy(price - 1), wrap each iteration in
        # `with self.subTest(fuel=fuel_type):` and assert the
        # rejection message.
        pass

    def test_all_fuels_produce_a_receipt_string_on_success(self):
        # TODO: buy a valid amount of each fuel, assert the fuel's own
        # name shows up in the returned receipt string (catches a
        # copy-paste mistake like the wrong fuel_type being passed
        # into generate_receipt for one of the four methods).
        pass


if __name__ == "__main__":
    unittest.main()