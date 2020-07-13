import numpy
import random

from Position import Position
from Validator import Validator


class Generator:
    SUDOKU_NUMBER = 9

    def __init__(self):
        self.grid = numpy.zeros((9, 9))
        self.backtracking = []
        self.validator = Validator(self.grid)

    def change_value(self, last_position):
        last_element = self.grid[last_position.row][last_position.column]

        if last_element not in last_position.no_candidates:
            last_position.no_candidates.append(last_element)
            self.grid[last_position.row][last_position.column] = random.randint(1, 9)

            if len(last_position.no_candidates) > 8:
                return

    def generate_sudoku(self):
        while len(self.backtracking) < 10:
            while self.validator.validation():
                position = Position(random.randrange(9), random.randrange(9))
                self.backtracking.append(position)
                self.grid[position.row][position.column] = random.randint(1, 9)

            self.change_value(self.backtracking[-1])

        return self.grid

    def pretty_print(self):
        for row in self.grid:
            print(row)


generator = Generator()
sudoku = generator.generate_sudoku()
print(sudoku)

validator = Validator(sudoku)
print(validator.validation())
