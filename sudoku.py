from tabulate import tabulate


sudoku_board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


def display_board(sudoku_board):
    print(tabulate(sudoku_board, tablefmt='fancy_grid'))



def empty_cells_exist():
    for i in range(9):
        for j in range(9):
            if sudoku_board[i][j] == 0:
                return [i, j]
    return False


def valid_number_check(num, i, j):
    
    for row in range(9):
        if sudoku_board[row][j] == num:
            return False

    
    for col in range(9):
        if sudoku_board[i][col] == num:
            return False

    
    grid_row = (i // 3) * 3
    grid_col = (j // 3) * 3

    for i in range(3):
        for j in range(3):
            if sudoku_board[grid_row + i][grid_col + j] == num:
                return False

    
    return True


def solver():
    cells_exist = empty_cells_exist()

    if not cells_exist:
        return True

    i, j = cells_exist[0], cells_exist[1]
    for num in range(1,10):
        if valid_number_check(num, i, j):
            sudoku_board[i][j] = num
            
            
            if solver():
                return True
            else:
                sudoku_board[i][j] = 0
                

    return False

display_board(sudoku_board)

if solver():
    display_board(sudoku_board)
else:
    print("no solution available")