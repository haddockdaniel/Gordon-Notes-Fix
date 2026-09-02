import unittest

from src.voice import dispatch, normalize


class VoiceTests(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize("  SHOW   BALANCE "), "show balance")

    def test_balance_dispatch(self):
        self.assertEqual(dispatch("show balance"), "balance")

    def test_create_invoice_dispatch(self):
        self.assertEqual(dispatch("create invoice"), "invoice_create")

    def test_unknown_dispatch(self):
        self.assertEqual(dispatch("delete universe"), "unknown")


if __name__ == "__main__":
    unittest.main()
