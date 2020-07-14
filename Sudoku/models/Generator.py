import numpy
import random

from Validator import Validator


class Generator:
    SUDOKU_NUMBER = 9
    GRID_SIZE = 81

    def __init__(self):
        self.grid = numpy.zeros((9, 9))
        self.route = []
        self.validator = Validator(self.grid)

    def fill_places(self):
        for i in range(10):
            while self.validator.validation():
                position = (random.randrange(9), random.randrange(9))
                if position not in self.route:
                    self.route.append(position)
                    self.grid[position[0]][position[1]] = random.randint(1, 9)

            invalid_value = self.route.pop()
            self.grid[invalid_value[0]][invalid_value[1]] = 0.0

            last_position = self.route.pop()
            for possible_value in range(9):
                self.grid[last_position[0]][last_position[1]] = possible_value
                if self.validator.validation():
                    break
                else:
                    continue


generator = Generator()
generator.fill_places()

for row in generator.grid:
    print(row)

validator = Validator(generator.grid)
print(validator.validation(), len(generator.route))
