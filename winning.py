#Author: Siena and Felix
#Date: 11/7/2017
#Determines if game is won and by who when given a matrix
#Scoring scores matrix, checking for wins and streaks
import numpy

#TODO check about range of functions

def winning(matrix, connect=4):
    """Check if player 1 or 2 wins with the board
    return tuple with (winning true/false, player who won)
    """
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    #horizontal
    for x in range(rows):
        for y in range(columns-connect+1):
            if matrix[x,y] == matrix[x,y+1] == matrix[x,y+2] == matrix[x,y+3] and matrix[x,y] != 0:
                # print('horiz')
                return True, matrix[x,y]
    #vertical
    for y in range(columns):
        for x in range(rows-connect+1):
            if matrix[x,y] == matrix[x+1,y] == matrix[x+2,y] == matrix[x+3,y] and matrix[x,y] != 0:
                # print('vertical')
                return True, matrix[x,y]
    #diagonal
    arrayM = numpy.asarray(matrix)
    for x in range(columns):
        a = numpy.diagonal(arrayM,x-(rows-connect))
        for i in range(len(a)-connect+1):
            if a[i] == a[i+1] == a[i+2] == a[i+3] and a[i] !=0:
                return True, a[i]
    #reverse diagonal
    arrayM = numpy.asarray(numpy.fliplr(matrix))
    for x in range(columns):
        a = numpy.diagonal(arrayM,x-(rows-connect))
        for i in range(len(a)-connect+1):
            if a[i] == a[i+1] == a[i+2] == a[i+3] and a[i] !=0:
                # print('diag')
                return True, a[i]
    #tie
    if numpy.count_nonzero(arrayM) == rows*columns:
        return True, 0
    #if not won
    return False, 0


def scoring(matrix, myTurn, connect=4):
    """Scores matrix position"""
    #TODO: add myTurn
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    a = winning(matrix, connect)[0]
    b = winning(matrix, connect)[1]
    score1 = 0
    score2 = 0
    # check if player 1 or 2 wins
    if b == 1:
        score1 = -100000
        return score1
    elif b == 2:
        score2 = 100000
        return score2
    else:
        #horizontal
        for x in range(rows):
            for y in range(columns-connect+2): #3 in a row
                if matrix[x,y] == matrix[x,y+1] == matrix[x,y+2] == 1:
                    score1 += 2500
                    # print(score1)
                elif matrix[x,y] == matrix[x,y+1] == matrix[x,y+2] == 2:
                    score2 += 2500
                    # print(score2)
            for y in range(columns-connect+3): #2 in a row
                if matrix[x,y] == matrix[x,y+1] == 1:
                    score1 += 50
                    # print(score1)
                elif matrix[x,y] == matrix[x,y+1] == 2:
                    score2 += 50
                    # print(score2)

        #vertical -- Doesn't look at the last row
        for y in range(columns):
            for x in range(rows-connect+2):
                if matrix[x,y] == matrix[x+1,y] == matrix[x+2,y] == 1:     #add another == for Connect 4
                    score1 += 2500
                    # print(score1)
                elif matrix[x,y] == matrix[x+1,y] == matrix[x+2,y] == 2:     #add another == for Connect 4
                    score2 += 2500
                    # print(score2)
            for x in range(rows-connect+3):
                if matrix[x,y] == matrix[x+1,y] == 1:     #add another == for Connect 4
                    score1 += 50
                    # print(score1)
                elif matrix[x,y] == matrix[x+1,y] == 2:     #add another == for Connect 4
                    score2 += 50
                    # print(score2)
        #diagonal
        arrayM = numpy.asarray(matrix)
        # for x in range(columns-1):
        for x in range(columns):
            a = numpy.diagonal(arrayM,x-(rows-connect))
            for i in range(len(a)-connect+2):
                if a[i] == a[i+1] == a[i+2] == 1:
                    score1 += 2500
                elif a[i] == a[i+1] == a[i+2] == 2:
                    score2 += 2500
            for i in range(len(a)-connect+3):
                if a[i] == a[i+1] == 1:
                    score1 += 50
                elif a[i] == a[i+1] == 2:
                    score2 += 50
        #reverse diagonal
        arrayM = numpy.asarray(numpy.fliplr(matrix))
        for x in range(columns-1):
            a = numpy.diagonal(arrayM,x-(rows-connect))
            for i in range(len(a)-connect+2):
                if a[i] == a[i+1] == a[i+2]  == 1:
                    score1 += 2500
                elif a[i] == a[i+1] == a[i+2] == 2:
                    score2 += 2500
            for i in range(len(a)-connect+3):
                if a[i] == a[i+1] == 1:
                    score1 += 50
                elif a[i] == a[i+1] == 2:
                    score2 += 50

    return score2-score1

# a = numpy.matrix('0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 1 0 0 2; 0 0 2 0 1 0 2; 0 2 0 0 0 1 2; 2 0 1 2 1 2 1')
# a = numpy.matrix('1 1 2 1 2 1 2; 1 2 1 1 2 2 1; 3 3 3 3 3 3 3; 2 1 2 1 2 1 2; 1 2 1 2 1 2 1; 1 2 1 2 1 2 1')
# print(a)
# print(scoring(a, True))
# print(winning(a))
