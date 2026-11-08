import sqlite3
import unittest

from src.database import initialize
from src.order_repository import find_by_email


class EmailLookupTest(unittest.TestCase):
    def test_untrusted_email_is_a_value(self):
        with sqlite3.connect(":memory:") as connection:
            initialize(connection)
            connection.execute(
                "INSERT INTO orders VALUES (?, ?, ?)", (1, "EX-100", "demo@example.invalid")
            )
            self.assertEqual(find_by_email(connection, "demo@example.invalid"), (1, "EX-100"))
            self.assertIsNone(find_by_email(connection, "' OR '1'='1"))
