#this is the file for our game

import pygame
import sys
import numpy
pygame.init()


background_color = (255,255,255)
WINDOW_DIMENSIONS = (640, 480)
width, height = 640, 480

"""Bunch of variables"""
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)
pygame.display.set_caption('Connect 4')


class Board:
    def __init__(self, matrix, piecesize=100):

        width, height = 5, 4

        # self.PIECESIZE = piecesize
        # self.BOARDWIDTH = width*piecesize
        # self.BOARDHEIGHT = height*piecesize
        # self.width = width
        # self.height = height
        # self.COLOR = (0, 0, 255)
        # self.XMARG = (WINDOW_DIMENSIONS[0] - self.BOARDWIDTH) // 2
        # self.YMARG = WINDOW_DIMENSIONS[1] // 4
        # self.RECT = pygame.Rect(self.XMARG, self.YMARG,
        #                         self.BOARDWIDTH, self.BOARDHEIGHT)
        # self.TURN = 0
        #
        # self.COUNT1 = 0  # player 1 moves
        # self.COUNT2 = 0  # player 2 moves

#the thigs used for the workign code

        self.width = width
        self.height = height
        self.matrix = matrix

        #self.PLAYERS = (p1, p2)2

    def draw(self, screen):
        # Drawing the grid
        for x in range(0, self.width * 100, 100):
            for y in range(0, self.height * 100, 100):
                rectangle =(x,y, 100, 100)
                #print("Drawing x, y : ", x, y)
                pygame.draw.rect(screen, (0,0,255), rectangle, 5)

        #drawing the chips
        for x in range(self.width):
            for y in range(self.height):
                pos = (x *100 + 50 , y *100 + 50)

                if self.matrix[y,x] == 1:
                    color = (255, 255, 0)   # yellow
                elif self.matrix[y, x] == 2:
                    color = (255, 0, 0)     # red
                else:
                    continue
                pygame.draw.circle(screen, color , pos, 40)

def createboard(rows,columns):
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

def winning(matrix, connect):
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    #horizontal
    for x in range(rows):
        for y in range(columns-connect+1):
            if matrix[x,y] == matrix[x,y+1] == matrix[x,y+2] and matrix[x,y] != 0:     #add another == for Connect 4
                return True, matrix[x,y]
    #vertical
    for y in range(columns):
        for x in range(rows-connect+1):
            if matrix[x,y] == matrix[x+1,y] == matrix[x+2,y] and matrix[x,y] != 0:     #add another == for Connect 4
                return True, matrix[x,y]
    #determines which side is longer for diagonal search
    if rows>columns:
        longer = rows
    else:
        longer = columns
    #diagonal
    arrayM = numpy.asarray(matrix)
    for x in range(longer-1):
        a = numpy.diagonal(arrayM,x-(rows-connect+1))
        for i in range(len(a)-connect+1):
            if a[i] == a[i++1] == a[i+2] and a[i] !=0:
                return True, a[i]
    #reverse diagonal
    arrayM = numpy.asarray(numpy.fliplr(matrix))
    for x in range(longer-1):
        a = numpy.diagonal(arrayM,x-(rows-connect+1))
        for i in range(len(a)-connect+1):
            if a[i] == a[i++1] == a[i+2] and a[i] !=0:
                return True, a[i]
    if numpy.count_nonzero(arrayM) == rows*columns:
        return True, 0
        #if not won
    return False, 0

pygame.init()

board = numpy.matrix('0,0,0,0,0; 0,0,0,0,0; 0,0,0,0,0; 0,0,0,0,0')
print(board)

# Initialise images (save images to folder)
#background = pygame.image.load('connect4Board.png').convert_alpha()
#redPiece = pygame.image.load('redPiece.png').convert_alpha()
#yellowPiece = pygame.image.load('yellowPiece.png').convert_alpha()



player = 0
Time = 0
endscreen = False
win = winning(board,3)

def look_through_rows(board, column, player):
    count = 3
    count2 = 1
    while count >= 0 and count2 == 1:
        if board[count,column] == 0:
            board[count,column] = player
            count2 = count2 - 1
        else:
            count = count - 1
    return board


#Keyboard input for player
running = True
while running:
    screen.fill((255, 255, 255)) #set up background
    boardC = Board(matrix = board)
    boardC.draw(screen)
    pygame.display.update()
    if pygame.time.get_ticks() > (Time + 10):
        Time = pygame.time.get_ticks()
        win = winning(board,3)
        if win[0] == True:
            running = False
            endscreen = True
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if player == 0:
                    player = 1
                elif player == 1:
                    player = 2
                elif player == 2:
                    player = 1
                if event.key == pygame.K_1:
                    look_through_rows(board, 0, player)
                    print(board)
                if event.key == pygame.K_2:
                    look_through_rows(board, 1, player)
                    print(board)
                if event.key == pygame.K_3:
                    look_through_rows(board, 2, player)
                    print(board)
                if event.key == pygame.K_4:
                    look_through_rows(board, 3, player)
                    print(board)
                if event.key == pygame.K_5:
                    look_through_rows(board, 4, player)
                    print(board)
                boardC.draw(screen)
                pygame.display.update()

while endscreen:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()

        basicfont = pygame.font.SysFont(None, 20)
        text = basicfont.render('Congrats! Player %.2d'%(win[1]) + ' Has Won', True, (0, 0, 0), (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery
        screen.blit(text, textrect)

    pygame.display.update()

pygame.quit()
