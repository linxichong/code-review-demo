import unittest

from src.notifications import receipt_message


class NotificationsTest(unittest.TestCase):
    def test_receipt_message(self):
        self.assertIn("受け付け", receipt_message())
