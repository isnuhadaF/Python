import unittest
from transaction import Transaction


class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.txn = Transaction()

    def test_set_transaction_adds_one_entry_to_self_transactions_dictionary(self):
        self.txn.set_transaction(1400, "Petrol", 1.0)
        self.assertEqual(len(self.txn.transactions), 1)

    def test_get_transactions_returns_a_string_type_not_none(self):
        # TODO: record one transaction, call get_transactions(),
        # assert isinstance(result, str) -- a version of this method
        # that used print() instead of return would fail this.
        pass

    def test_get_transactions_returns_empty_string_when_self_transactions_dictionary_is_empty(self):
        # TODO: no set_transaction calls at all -- get_transactions()
        # on a brand new Transaction() should return "" cleanly.
        pass

    def test_set_transaction_called_twice_does_not_overwrite_the_first_entry_in_self_transactions_dictionary(self):
        # TODO: call set_transaction twice with different fuel_type
        # and fuel_amount values. Assert len(self.txn.transactions) == 2.
        # This is the datetime.now()-as-key bug made concrete.
        pass

    def test_get_transactions_output_includes_both_fuel_type_and_fuel_cost_values(self):
        # TODO: record one transaction, assert the fuel_type string
        # and the fuel_cost value both appear in the returned text.
        pass


if __name__ == "__main__":
    unittest.main()