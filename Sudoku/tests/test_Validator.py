from unittest import TestCase
from models.Validator import Validator


class TestValidator(TestCase):
    SUDOKU_EX_A = [
        [6, 2, 4, 5, 3, 9, 1, 8, 7],
        [5, 1, 9, 7, 2, 8, 6, 3, 4],
        [8, 3, 7, 6, 1, 4, 2, 9, 5],
        [1, 4, 3, 8, 6, 5, 7, 2, 9],
        [9, 5, 8, 2, 4, 7, 3, 6, 1],
        [7, 6, 2, 3, 9, 1, 4, 5, 8],
        [3, 7, 1, 9, 5, 6, 8, 4, 2],
        [4, 9, 6, 1, 8, 2, 5, 7, 3],
        [2, 8, 5, 4, 7, 3, 9, 1, 6],
    ]

    SUDOKU_EX_B = [
        [6, 2, 4, 5, 6, 9, 1, 8, 7],
        [5, 1, 9, 7, 2, 8, 6, 3, 4],
        [8, 3, 7, 6, 1, 4, 2, 9, 5],
        [1, 4, 3, 8, 6, 5, 7, 2, 9],
        [9, 5, 8, 2, 9, 7, 3, 6, 1],
        [7, 6, 2, 3, 9, 1, 4, 5, 8],
        [3, 7, 1, 9, 5, 6, 8, 4, 2],
        [4, 9, 6, 1, 4, 2, 5, 7, 3],
        [2, 8, 5, 4, 7, 3, 9, 1, 6],
    ]

    SUDOKU_EX_C = [
        [9, 5, 8, 2, 4, 7, 3, 6, 1],
        [7, 6, 2, 3, 9, 1, 4, 5, 8],
        [3, 7, 1, 9, 5, 6, 8, 4, 2],
        [4, 9, 6, 1, 8, 2, 5, 7, 3],
        [2, 8, 5, 4, 7, 3, 9, 1, 6],
        [6, 2, 4, 5, 3, 9, 1, 8, 7],
        [5, 1, 9, 7, 2, 8, 6, 3, 4],
        [8, 3, 7, 6, 1, 4, 2, 9, 5],
        [1, 4, 3, 8, 6, 5, 7, 2, 9],
    ]

    def test_validator(self):
        self.assertTrue(Validator(self.SUDOKU_EX_A).validation(), "Should be True")
        self.assertFalse(Validator(self.SUDOKU_EX_B).validation(), "Should be False")
        self.assertFalse(Validator(self.SUDOKU_EX_C).validation(), "Should be False")
