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
    colB = 0
    colE = 3
    rowB = 0
    rowE = 3
    count = 0
    sub_grid = []
    while (count < 9):
        for i in range(colB, colE):
            for j in range(rowB, rowE):
                sub_grid.append(grid[i][j])
        if (colB <= 3 or colE <= 6):
            colB += 3
            colE += 3
        count += 1
        if ((count == 3 or count == 6) and (rowB <= 3 or rowE <= 6)):
            rowB += 3
            rowE += 3
            colB = 0
            colE = 3
        thread_c = threading.Thread(target=getFlags, args=(sub_grid,))
        listThreads.append(thread_c)
        thread_c.start()
        sub_grid = []


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

flag = totalFlags[0] and totalFlags[1]

def resultSudoku(flag, arr_flag, index):
    if index < 27:
        flag = flag and arr_flag[index]
        index += 1
        resultSudoku(flag, arr_flag, index)
    else:
        print("The sudoku is", "correct." if flag else "incorrect.")

resultSudoku(flag, totalFlags, 2)

print ("Time", timeB - timeA)
print("Number of threads used:", len(listThreads))
