# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:25:11 2020

@author: akush
"""
import numpy as np

def main():
    global board
    board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
             [5, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 7, 0, 0, 0, 0, 3, 1],
             [0, 0, 3, 0, 1, 0, 0, 8, 0],
             [9, 0, 0, 8, 6, 3, 0, 0, 5],
             [0, 5, 0, 0, 9, 0, 6, 0, 0],
             [1, 3, 0, 0, 0, 0, 2, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 7, 4],
             [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    sudoku(board)

def sudoku(board):

        for rowno in range(9):
            for colno in range(9):
                if board[rowno][colno] == 0:
                    for i in range(1,10):
                        if (is_valid(board,rowno,colno,i)):
                            board[rowno][colno]=i
                            sudoku(board)
                            board[rowno][colno]=0
                    return False

        print(np.matrix(board))

def is_valid(b,r,c,n): #check if number insertion is valid
    if n in b[r]: #if in row
        return False
    for x in range(0,9):
        if n == b[x][c]: #check for column
            return False
    sr = r - r%3
    sc = c - c%3
    for x in range(sr,sr+3):
        for y in range(sc,sc+3):
            if b[x][y]==n:
                return False
    return True

if __name__ == "__main__":
    main()
