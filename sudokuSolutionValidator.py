import threading
import datetime

timeA = datetime.datetime.now()

grid = [
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

sudoku_number = 9
totalFlags = []
listThreads = []


# Check only the rows from later to do the analysis.
def checkRows(grid):
    for i in range(sudoku_number):
        thread_a = threading.Thread(target=getFlags, args=(grid[i],))
        listThreads.append(thread_a)
        thread_a.start()


# Check only the columns from later to do the analysis
def checkColumns(grid):
    for i in range(sudoku_number):
        columns = []
        for j in range(sudoku_number):
            columns.append(grid[j][i])
        thread_b = threading.Thread(target=getFlags, args=(columns,))
        listThreads.append(thread_b)
        thread_b.start()

# Check each sub grid from later to do the analysis
def checkSubGrids(grid):
    beginRow = 0
    beginColumn = 0
    endRow = 3
    endColumn = 3
    for x in range(sudoku_number):
        sub_grid = []
        for i in range(beginRow, endRow):
            for j in range(beginColumn, endColumn):
                sub_grid.append(grid[i][j])
        thread_c = threading.Thread(target=getFlags, args=(sub_grid,))
        listThreads.append(thread_c)
        thread_c.start()


# Support functions to calculate the values of getFlags and getArrFlag.
# Give an array with boolean values that will validate the data.
def getFlags(arr_values):
    arr_flag = [None] * sudoku_number
    for i in range(sudoku_number):
        if arr_flag[arr_values[i] - 1] is None:
            arr_flag[arr_values[i] - 1] = True
        else:
            arr_flag[arr_values[i] - 1] = False
    for i in range(sudoku_number):
        if arr_flag[i] is None: arr_flag[i] = False;
    flag = arr_flag[0] and arr_flag[1]
    getArrFlag(flag, arr_flag, 2)


# Recursive function that give like result an array of flags.
def getArrFlag(flag, arr_flag, index):
    if index < 9:
        flag = flag and arr_flag[index]
        index += 1
        getArrFlag(flag, arr_flag, index)
    else:
        totalFlags.append(flag)


checkRows(grid)
checkColumns(grid)
checkSubGrids(grid)

timeB = datetime.datetime.now()
print(totalFlags, timeB - timeA)
print(listThreads)
