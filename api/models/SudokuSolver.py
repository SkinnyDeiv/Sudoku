import random

from models.SudokuBoard import SudokuBoard


class SudokuSolver:

    def __init__(self, sudoku_board):
        self.sudoku_board = sudoku_board

    def solve(self):
        solutions = []
        self.solve_traversal(self.sudoku_board, solutions)
        if len(solutions) > 1:
            raise Exception("Sudoku has more than one solution")
        return solutions[0]

    @staticmethod
    def solve_traversal(sudoku_board, solutions):

        cells_to_solve = sudoku_board.get_empty_cells()
        if not cells_to_solve:
            if not sudoku_board in solutions:
                solutions.append(sudoku_board)
                return
        cells_to_solve.sort(key=lambda coords: len(sudoku_board.get_available_numbers(coords[0], coords[1])))

        row_num, column_num = cells_to_solve.pop(0)
        available_numbers = sudoku_board.get_available_numbers(row_num, column_num)

        for number in available_numbers:
            sudoku_copy = sudoku_board.clone()
            sudoku_copy.assign(row_num, column_num, number)
            SudokuSolver.solve_traversal(sudoku_copy, solutions)


sudoku = SudokuBoard()
sudoku.build()
sudoku_orig = sudoku.clone()
for i in range(40):
    sudoku.clear_cell(random.randrange(9), random.randrange(9))
solver = SudokuSolver(sudoku)
solution = solver.solve()
print(solution == sudoku_orig)
