import unittest

from src.voice import dispatch, normalize


class VoiceTests(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize("  SHOW   BALANCE "), "show balance")

    def test_known_dispatch(self):
        self.assertEqual(dispatch("show balance"), "balance")

    def test_unknown_dispatch(self):
        self.assertEqual(dispatch("create invoice"), "unknown")


if __name__ == "__main__":
    unittest.main()
