import unittest

from Backend.Data.ScoreKeeper import ScoreKeeper


class TestSoreKeeper(unittest.TestCase):
    def test_init(self):
        sk = ScoreKeeper()
        self.assertEqual(sk.score_dict[0], 0)
        self.assertEqual(sk.score_dict[1], 0)

        sk = ScoreKeeper(2, 9)
        self.assertEqual(sk.score_dict[0], 2)
        self.assertEqual(sk.score_dict[1], 9)

        sk = ScoreKeeper(2)
        self.assertEqual(sk.score_dict[0], 2)
        self.assertEqual(sk.score_dict[1], 0)

    def test_record_win(self):
        sk = ScoreKeeper()
        self.assertEqual(sk.score_dict[0], 0)
        sk.record_win(0)
        self.assertEqual(sk.score_dict[0], 1)
        sk.record_win(1)
        sk.record_win(1)
        self.assertEqual(sk.score_dict[1], 2)

    def test_get_score(self):
        sk = ScoreKeeper()
        self.assertEqual(sk.get_score(0), 0)
        self.assertEqual(sk.get_score(1), 0)
        sk.record_win(0)
        self.assertEqual(sk.get_score(0), 1)
