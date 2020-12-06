#Author: John, Leo, & Viktoria
#Project: Connect 4
#Date: 12/12/2017

import numpy
import pygame

def createboard(rows,columns):
    """ Creates a string given rows and columns desired
        that can be converted into a matrix through numpy

    >>> createboard(5,4)
    '0,0,0,0,0; 0,0,0,0,0; 0,0,0,0,0; 0,0,0,0,0'
    >>> createboard(3,7)
    '0,0,0; 0,0,0; 0,0,0; 0,0,0; 0,0,0; 0,0,0; 0,0,0'
    """
    row_size = ''
    for rows in range(rows):
        if rows == 0:
            row_size = row_size + '0'
        else:
            row_size = row_size + ',0'
    fullmatrix = ''
    for cols in range(columns):
        if cols == 0:
            fullmatrix = fullmatrix + row_size
        else:
            fullmatrix = fullmatrix + '; ' + row_size
    return fullmatrix


def look_through_rows(board, column, player):
    """ Given a matrix, a column of the matrix, and a key,
    This function will look through the column bottom to top,
    and find the first empty slot indicated by a 0 and place
    a piece there (1 or 2)
    >>> look_through_rows(numpy.matrix('0,0,0,0,0; 0,0,0,0,0; 0,0,0,0,0; 0,0,0,0,0'), 2, 1)
    matrix([[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0]])
    >>> look_through_rows(numpy.matrix('0,0,0; 0,0,0; 0,0,0; 0,0,0; 0,0,0; 0,0,0; 0,0,0'), 1, 2)
    matrix([[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 2, 0]])
    """
    if board.shape[1] > column:
        count = board.shape[0] - 1
        count2 = 1
        while count >= 0 and count2 == 1:
            if board[count,column] == 0:
                board[count,column] = player
                count2 = count2 - 1
            else:
                count = count - 1
        return board
    else:
        print('Improper Column Given')

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
