import random


class SudokuBoard:

    def __init__(self):
        self.grid = [[0] * 9 for _ in range(9)]

        attempts, row_num = 0, 0
        while row_num < 9:
            while not self._build_new_row(row_num):
                self.grid[row_num] = [0] * 9
                attempts += 1

                if attempts > 50:
                    self.grid = [[0 for _ in range(9)] for _ in range(9)]
                    attempts, row_num = 0, 0
                    continue

            row_num += 1

    def _build_new_row(self, row_num):
        for column_num in range(9):
            available_numbers = self._get_available_numbers(row_num, column_num)
            if not available_numbers:
                return False
            number = random.choice(list(available_numbers))
            self.grid[row_num][column_num] = number
        return True

    def _get_available_numbers(self, row_num, column_num):
        row_occupied_numbers = {self.grid[row_num][j] for j in range(9)}
        column_occupied_numbers = {self.grid[i][column_num] for i in range(9)}
        sub_grid_low_row = row_num - row_num % 3
        sub_grid_low_column = column_num - column_num % 3
        sub_grid_occupied_numbers = {self.grid[i][j] for i in range(sub_grid_low_row, sub_grid_low_row + 3)
                                     for j in range(sub_grid_low_column, sub_grid_low_column + 3)}
        occupied_numbers = row_occupied_numbers | column_occupied_numbers | sub_grid_occupied_numbers
        return {1, 2, 3, 4, 5, 6, 7, 8, 9} - occupied_numbers

    # Returns if each row fulfills the criterion of having only one element from 1 to 9
    def _check_rows(self):
        for row in self.grid:
            if len(set(row)) != 9:
                return False
        return True

    # Returns if each column fulfills the criterion of having only one element from 1 to 9
    def _check_columns(self):
        for icolumn in range(9):
            column = [row[icolumn] for row in self.grid]
            if len(set(column)) != 9:
                return False
        return True

    # Returns if each sub grid fulfills the criterion of having only one element from 1 to 9
    def _check_sub_grids(self):
        for irow in range(0, 9, 3):
            for icolumn in range(0, 9, 3):
                sub_grid = [self.grid[i][j] for i in range(irow, irow + 3) for j in range(icolumn, icolumn + 3)]
                if len(set(sub_grid)) != 9:
                    return False
        return True

    # Returns if the sudoku matrix is valid or not.
    @property
    def is_valid(self):
        return self._check_rows() and self._check_columns() and self._check_sub_grids()

    def print(self):
        print("** Sudoku Board **")
        for row in self.grid:
            print(row)


for i in range(0, 100):
    sb = SudokuBoard()
    #sb.print()
    print(sb.is_valid)