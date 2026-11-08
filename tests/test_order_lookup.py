import sqlite3
import unittest

from src.database import initialize
from src.order_api import lookup_order


class OrderLookupTest(unittest.TestCase):
    def test_existing_order(self):
        with sqlite3.connect(":memory:") as connection:
            initialize(connection)
            connection.execute(
                "INSERT INTO orders VALUES (?, ?, ?)", (1, "EX-100", "demo@example.invalid")
            )
            self.assertEqual(lookup_order(connection, "EX-100"), (200, {
                "id": 1, "reference": "EX-100",
            }))
