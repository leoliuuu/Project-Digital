#authors: Siena and Felix
# Needed functions isLegalMove
#new variables: board = matrix

import numpy
import pygame
import random
import sys
from pynput.keyboard import Key, Controller
from winning import winning, scoring
keyboard = Controller()

pygame.init()

def isLegalMove(column, board):
    """
    Input: board (matrix), column (int)
    Check if there is a space left in the column
    output: boolean
    >>> isLegalMove((('0 1 0 1 0; 0 0 0 0 0; 0 0 0 0 0; 0 0 0 0 0')), board)
    True
    """
    # loop through every row of a column
    rows = board.shape[0]
    for row in reversed(range(rows)):
        if board[row, column] == 0:
            # as soon as we find the first empty spot return True
            return True
    # if we iterated through all rows
    return False


def makeMove(column, board, myTurn):
    """
    Input: column (int), whose turn (boolean), and the board (matrix)
    What: insert your coin in the column you chose
    How: find the first empty (0) spot in the column and replace with your number
    Output: the new board
    >>> makeMove(1, board, True)
    [[0, 2, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    """
    # adapt the number of rows to the game
    rows=board.shape[0]
    # check if it is my turn
    if myTurn == True: #bot = player 2
        coin = 2
    else: #human = player 1
        coin = 1
    board_temp = board.copy()
    for row in reversed(range(rows)):
        if board_temp[row, column] == 0:
            board_temp[row, column] = coin
            return board_temp

def search(depth, board, myTurn):
        """ Search the tree until depth 'depth'
            By default, the  is the board, and curr_player is whomever called this search
            Return score
            >>> search(0, board, True)

        """
        columns = board.shape[1]
        # enumerate all possible moves from this board
        legal_moves = []
        for column in range(columns):
            # if column i is a legal move
            if isLegalMove(column, board):
                # make the move in column i for curr_player
                temp = makeMove(column, board, myTurn)
                # print(temp)
                # create list of matrix
                legal_moves.append(temp)
        ### BASECASE (if depth == 0, game tied or someone wins)
        if depth == 0 or len(legal_moves) == 0 or winning(board)[0]:
            # return value(board, curr_player) from winning
            return scoring(board, myTurn) #*(depth+1)
        #### RECURSION
        elif myTurn:  #Maximizing Player
            score = -99999999
            for child in legal_moves:
                val = search(depth-1, child, False)
                score = max(score, val)
                # print(score)
            return score
        elif not myTurn:  #Minimizing Player
            score = 99999999
            for child in legal_moves:
                val = search(depth-1, child, True)
                score = min(score, val)
            return score

def best_option(possible_moves):
    """
    INPUT: options with score (dict)

    choose the the highest value
    return the key (branch) of the maximum value (score)
    if no option given, choose the middle column(3)

    OUTPUT: column (integer) were we should place our piece
    """
    best_score = -99999999
    best_move = None
    moves = possible_moves.items()
    random.shuffle(list(moves))
    for move, score in moves:
        if score >= best_score:
            best_score = score
            best_option = move
    # best_option = max(possible_moves, key=possible_moves.get)
    # return str(best_option+1)
    return str(best_option+1)



def choose_options(depth, board, myTurn=True):
    """
    INPUT: depth(integer), board(matrix), myTurn(boolean)

    creates a dict with score s

    OUTPUT: column (integer) were we should place our piece
    >>> choose_options(depth, board)

    """
    rows = board.shape[0]
    columns = board.shape[1]
    possible_moves = {} # possible moves (key) and their scores (value)
    for column in range(columns):
        # check if column i is a possible
        if isLegalMove(column, board):
            # make the move in column  for curr_player
            temp = makeMove(column, board, myTurn)
            # print(column)
            # print(temp)
            if winning(temp)[1] == 2:
                # print('winning')
                return str(column+1)
            if depth == 0:
                possible_moves[column] = scoring(temp, True)
            #### assign overall score (value, recurs function) to every column (key)
            possible_moves[column] = search(depth-1, temp, False)
    print(possible_moves)
    # return the key(column) for the best score
    return best_option(possible_moves)

def simulate_keypress(keypress):
    """simulates keypress"""
    keyboard.press(keypress)
    keyboard.release(keypress)

def bot_player(depth, board, myTurn=True):
    """
    concludes every necessary function for AI
    choose best option & simulate keypress for it
    >>> bot_player(depth, board, myTurn=True)

    """
    # print('thinking')
    # col = int(choose_options(depth, board))
    col = choose_options(depth, board)
    s = simulate_keypress(col)
    # print('done')
    # return col
    return s

a = numpy.matrix('0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 0 0 2 1; 0 0 0 0 0 1 1; 0 0 2 2 2 2 2')
# a = numpy.matrix('0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 1 0 0 0')
# print(choose_options(4, a))
# print(a)
# print(bot_player(2, a))
