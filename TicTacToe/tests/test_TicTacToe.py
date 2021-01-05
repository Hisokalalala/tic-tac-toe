from unittest import TestCase
from TicTacToe.TicTacToe import turn
from TicTacToe.TicTacToe import whowin


class Test(TestCase):
    def test_turn(self):
        self.assertEqual(turn([["?", "?", "?"], ["?", "?", "?"], ["?", "?", "?"]], "M", 1, 1), "○ ? ?\n? ? ?\n? ? ?\n")
        self.assertEqual(turn([["?", "?", "?"], ["?", "?", "?"], ["?", "?", "?"]], "B", 2, 1), "? ? ?\n× ? ?\n? ? ?\n")

class Test(TestCase):
    def test_whowin(self):
        self.assertEqual(whowin([["○", "○", "○"], ["×", "×", "?"], ["?", "?", ""]]), "result: ○ WIN!!")
        self.assertEqual(whowin([["○", "?", "×"], ["○", "×", "?"], ["○", "?", "?"]]), "result: ○ WIN!!")
        self.assertEqual(whowin([["○", "○", "×"], ["○", "×", "?"], ["×", "○", "?"]]), "result: × WIN!!")