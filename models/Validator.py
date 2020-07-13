def _purge_list(entry_list):
    purged_list = []
    for element in entry_list:
        if element != 0.0:
            purged_list.append(element)

    return len(purged_list) != len(set(purged_list))


class Validator:
    SUDOKU_NUMBER = 9

    def __init__(self, sudoku_matrix):
        self.matrix = sudoku_matrix

    # Returns if each row fulfills the criterion of having only one element from 1 to 9
    def _check_rows(self):
        for row in self.matrix:
            if len(set(row)) != self.SUDOKU_NUMBER and _purge_list(row):
                return False
        return True

    # Returns if each column fulfills the criterion of having only one element from 1 to 9
    def _check_columns(self):
        for icolumn in range(self.SUDOKU_NUMBER):
            column = [row[icolumn] for row in self.matrix]
            if len(set(column)) != self.SUDOKU_NUMBER and _purge_list(column):
                return False
        return True

    # Returns if each sub grid fulfills the criterion of having only one element from 1 to 9
    def _check_sub_grids(self):
        for irow in range(0, self.SUDOKU_NUMBER, 3):
            for icolumn in range(0, self.SUDOKU_NUMBER, 3):
                sub_grid = [self.matrix[i][j] for i in range(irow, irow + 3) for j in range(icolumn, icolumn + 3)]
                if len(set(sub_grid)) != self.SUDOKU_NUMBER and _purge_list(sub_grid):
                    return False
        return True

    # Returns if the sudoku matrix is correct or not.
    def validation(self):
        return self._check_rows() and self._check_columns() and self._check_sub_grids()


