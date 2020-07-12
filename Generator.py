import random


class Generator:
    SUDOKU_NUMBER = 9

    def __init__(self):
        self.grid = [[0] * self.SUDOKU_NUMBER] * self.SUDOKU_NUMBER

    def fill_subgrid(self):
        random_list = random.sample(range(1, 10), 9)

        print(random_list)
        for irow in range(0, self.SUDOKU_NUMBER):
            # print(random_list.pop())
            self.grid[irow][0] = random_list.pop()
        print(random_list)

        return self.grid


generator = Generator()
print(generator.fill_subgrid())
