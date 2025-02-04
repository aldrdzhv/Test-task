import unittest

from training import get_score

class TestGetScore(unittest.TestCase):
    def setUp(self):
        self.game_stamps = [
            {"offset": 0, "score": {"home": 0, "away": 0}},
            {"offset": 10, "score": {"home": 1, "away": 0}},
            {"offset": 20, "score": {"home": 1, "away": 1}},
            {"offset": 30, "score": {"home": 2, "away": 1}},
            {"offset": 40, "score": {"home": 2, "away": 2}},
        ]

    def test_offset_exact_match(self):
        home, away = get_score(self.game_stamps, 20)
        self.assertEqual((home, away), (1, 1))

    def test_offset_between_stamps(self):
        home, away = get_score(self.game_stamps, 25)
        self.assertEqual((home, away), (1, 1))

    def test_offset_less_than_first_stamp(self):
        home, away = get_score(self.game_stamps, -5)
        self.assertEqual((home, away), (0, 0))

    def test_offset_greater_than_last_stamp(self):
        home, away = get_score(self.game_stamps, 50)
        self.assertEqual((home, away), (2, 2))

    def test_empty_game_stamps(self):
        home, away = get_score([], 20)
        self.assertEqual((home, away), (0, 0))

if __name__ == "__main__":
    unittest.main()