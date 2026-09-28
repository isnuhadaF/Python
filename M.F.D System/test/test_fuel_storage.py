import unittest
from fuel_storage import FuelStorage
from fuel_station import FuelStation


class TestFuelStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FuelStorage()

    def test_get_storage_does_not_raise_and_returns_a_string(self):
        result = self.storage.get_storage()
        self.assertIsInstance(result, str)

    def test_get_storage_output_includes_all_four_fuel_type_names(self):
        # TODO: assert "Petrol", "Diesel", "Kerosene", and
        # "Natural Gas" each appear somewhere in the returned string.
        pass

    def test_get_storage_output_separates_each_line_with_a_newline_character(self):
        # TODO: assert the returned string contains at least 4 "\n"
        # characters -- catches the missing-newline formatting bug.
        pass

    def test_fuel_litres_available_keys_exactly_match_fuel_station_fuel_types_keys(self):
        # TODO: station = FuelStation()
        # assert set(self.storage.fuel_litres_available.keys()) \
        #     == set(station.fuel_types.keys())
        # This is the test that would have caught the missing
        # "Natural Gas" key before buy_natural_gas ever ran against it.
        pass


if __name__ == "__main__":
    unittest.main()