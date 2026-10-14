def print_board(board):
    for i, row in enumerate(board):
        row_str=" "
        for j, value in enumerate(row):
            row_str+=value
            if j!= len(row)-1:
                row_str+="|"
        print(row_str)
        if i!= len(board)-1:
            print("--------")

def get_move(turn, board):
    while True:
        row= int(input("Row: "))
        col= int(input("Col: "))

        if row<1 or row>len(board):
            print("Invalid row, pl try again")
        elif col<1 or col>len(board[row-1]):
            print("Invalid col, pl try again")
        elif board[row-1][col-1]!=" ":
            print("Already taken, pl try again!")
        else:
            break
    board[row-1][col-1]=turn


board= [
    ["X"," "," "],
    [" ","0"," "],
    [" "," ","X"]
]
print_board(board)
get_move("X", board)
print_board(board)
get_move("0", board)
print_board(board)