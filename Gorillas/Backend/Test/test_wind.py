import unittest

from Backend.Data.Enumerators import WindDirection
from Backend.Data.Wind import Wind


class TestWind(unittest.TestCase):

    def test_init(self):
        w = Wind()
        self.assertEqual(w.direction, WindDirection.LEFT)
        self.assertEqual(w.velocity, 0)

        w = Wind(WindDirection.RIGHT)
        self.assertEqual(w.direction, WindDirection.RIGHT)
        self.assertEqual(w.velocity, 0)

        w = Wind(WindDirection.RIGHT, 15)
        self.assertEqual(w.direction, WindDirection.RIGHT)
        self.assertEqual(w.velocity, 15)

        self.assertRaises(Exception, lambda: Wind(RIGHT, -1))
        self.assertRaises(Exception, lambda: Wind(WindDirection.RIGHT, -1))
