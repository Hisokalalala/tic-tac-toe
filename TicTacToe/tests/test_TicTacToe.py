from unittest import TestCase
from TicTacToe.TicTacToe import turn


class Test(TestCase):
    def test_turn(self):
        self.assertEqual(turn([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 1), "1 0 0\n0 0 0\n0 0 0")
        self.assertEqual(turn([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 2, 1), "0 0 0\n1 0 0\n0 0 0")
