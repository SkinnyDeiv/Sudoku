import threading
import datetime

TIME_A = datetime.datetime.now()

GRID = [
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

SUDOKU_NUMBER = 9

total_flags = []
list_threads = []


# Check only the rows from later to do the analysis.
def check_rows(grid):
    for i in range(SUDOKU_NUMBER):
        thread_a = threading.Thread(target=get_flags, args=(grid[i],))
        list_threads.append(thread_a)
        thread_a.start()


# Check only the columns from later to do the analysis
def check_columns(grid):
    for i in range(SUDOKU_NUMBER):
        columns = []
        for j in range(SUDOKU_NUMBER):
            columns.append(grid[j][i])
        thread_b = threading.Thread(target=get_flags, args=(columns,))
        list_threads.append(thread_b)
        thread_b.start()


# Check each sub grid from later to do the analysis
def check_sub_grids(grid):
    col_b = 0
    col_e = 3
    row_b = 0
    row_e = 3
    count = 0
    sub_grid = []
    while count < 9:
        for i in range(col_b, col_e):
            for j in range(row_b, row_e):
                sub_grid.append(grid[i][j])
        if col_b <= 3 or col_e <= 6:
            col_b += 3
            col_e += 3
        count += 1
        if (count == 3 or count == 6) and (row_b <= 3 or row_e <= 6):
            row_b += 3
            row_e += 3
            col_b = 0
            col_e = 3
        thread_c = threading.Thread(target=get_flags, args=(sub_grid,))
        list_threads.append(thread_c)
        thread_c.start()
        sub_grid = []


# Support functions to calculate the values of getFlags and getArrFlag.
# Give an array with boolean values that will validate the data.
def get_flags(arr_values):
    arr_flag = [None] * SUDOKU_NUMBER

    for i in range(SUDOKU_NUMBER):
        if arr_flag[arr_values[i] - 1] is None:
            arr_flag[arr_values[i] - 1] = True
        else:
            arr_flag[arr_values[i] - 1] = False

    for i in range(SUDOKU_NUMBER):
        if arr_flag[i] is None: arr_flag[i] = False

    are_equal = arr_flag[0] and arr_flag[1]
    get_arr_flag(are_equal, arr_flag, 2)


# Recursive function that give like result an array of flags.
def get_arr_flag(entry_flag, arr_flag, index):
    if index < 9:
        entry_flag = entry_flag and arr_flag[index]
        index += 1
        get_arr_flag(entry_flag, arr_flag, index)
    else:
        total_flags.append(entry_flag)


check_rows(GRID)
check_columns(GRID)
check_sub_grids(GRID)

time_b = datetime.datetime.now()

flag = total_flags[0] and total_flags[1]


def result_sudoku(flag, arr_flag, index):
    if index < 27:
        flag = flag and arr_flag[index]
        index += 1
        result_sudoku(flag, arr_flag, index)
    else:
        print("The sudoku is", "correct." if flag else "incorrect.")


result_sudoku(flag, total_flags, 2)

print("Time", time_b - TIME_A)
print("Number of threads used:", len(list_threads))
