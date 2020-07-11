import threading


class Validator:
    SUDOKU_NUMBER = 9

    def __init__(self, sudoku_matrix):
        self.matrix = sudoku_matrix
        self.matrix_checker = []

    # Returns if each row fulfills the criterion of having only one element from 1 to 9
    def _check_rows(self):
        for i in range(self.SUDOKU_NUMBER):
            thread_a = threading.Thread(target=self._get_flags, args=(self.matrix[i],))
            thread_a.start()

    # Returns if each column fulfills the criterion of having only one element from 1 to 9
    def _check_columns(self):
        for i in range(self.SUDOKU_NUMBER):
            columns = []
            for j in range(self.SUDOKU_NUMBER):
                columns.append(self.matrix[j][i])
            thread_b = threading.Thread(target=self._get_flags, args=(columns,))
            thread_b.start()

    # Returns if each sub grid fulfills the criterion of having only one element from 1 to 9
    def _check_sub_grids(self):
        col_start, row_start, count = 0, 0, 0
        col_end, row_end = 3, 3
        sub_grid = []

        while count < 9:
            for i in range(col_start, col_end):
                for j in range(row_start, row_end):
                    sub_grid.append(self.matrix[i][j])

            if col_start <= 3 or col_end <= 6:
                col_start += 3
                col_end += 3

            count += 1

            if (count == 3 or count == 6) and (row_start <= 3 or row_end <= 6):
                row_start += 3
                row_end += 3
                col_start = 0
                col_end = 3

            thread_c = threading.Thread(target=self._get_flags, args=(sub_grid,))
            thread_c.start()
            sub_grid = []

    # Checks if there is some element repeated.
    def _get_flags(self, arr_values):
        arr_flag = [None] * self.SUDOKU_NUMBER

        for i in range(self.SUDOKU_NUMBER):
            if arr_flag[arr_values[i] - 1] is None:
                arr_flag[arr_values[i] - 1] = True
            else:
                arr_flag[arr_values[i] - 1] = False

        for i in range(self.SUDOKU_NUMBER):
            if arr_flag[i] is None:
                arr_flag[i] = False

        initial_flag = arr_flag[0] and arr_flag[1]
        self._get_arr_flag(initial_flag, arr_flag, 2)

    # Recursive function that gives as result an array of flags.
    def _get_arr_flag(self, entry_flag, arr_flag, index):
        if index < 9:
            entry_flag = entry_flag and arr_flag[index]
            index += 1
            self._get_arr_flag(entry_flag, arr_flag, index)
        else:
            self.matrix_checker.append(entry_flag)

    # Returns if the sudoku matrix is correct or not.
    def validation(self):
        self._check_rows()
        self._check_columns()
        self._check_sub_grids()

        result = True

        for flag in self.matrix_checker:
            result = result and flag

        return result
