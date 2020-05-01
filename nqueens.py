import numpy as np

def main():
    global n
    n = input("Enter N")
    n = int(n)
    global board
    board = np.zeros((n,n), dtype=int)
    solve_board(0)


def solve_board(row):

    if(row == n):
        print('-'*n)
        for row in board:
            for col in row:
                if col == 1:
                    print ("Q", end = " ")
                else:
                    print (".", end = " ")
            print("")


    else:
        for col in range(n):
            if (is_valid (board,row,col,n)):
                board[row][col]=1
                solve_board(row+1)
                board[row][col]=0
        return False

def is_valid(board,i,j,n):
    if board[i][j] == 1: #Queen placed
        return False

    for row in range(0,i): #check column
        if (board[row][j]==1):
            return False
    x,y = i,j

    while (x>=0 and y>=0): #left diagonal
         if (board[x][y]==1):
             return False
         x-=1
         y-=1

    x,y = i,j
    while (x>=0 and y<n): #right diagonal
         if (board[x][y]==1):
             return False
         x-=1
         y+=1
    return True

if __name__ == "__main__":
    main()
