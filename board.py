import pygame
import numpy
import functions
import sys
import winning
import fake_bot
import bot

class Board:
    def __init__(self, rows, columns, piecesize=100):

        self.rows = rows
        self.columns = columns
        self.matrix = numpy.matrix(functions.createboard(self.rows,self.columns))

    def draw(self, screen):
        # Drawing the grid
        for x in range(0, self.rows * 100, 100):
            for y in range(0, self.columns * 100, 100):
                rectangle =(x,y, 100, 100)
                pygame.draw.rect(screen, (0,0,255), rectangle, 5)

        #drawing the chips
        for x in range(self.rows):
            for y in range(self.columns):
                pos = (x *100 + 50 , y *100 + 50)

                if self.matrix[y, x] == 1:
                    color = (255, 255, 0)   # player 1 is yellow
                elif self.matrix[y, x] == 2:
                    color = (255, 0, 0)     # player 2 is red
                else:
                    continue
                pygame.draw.circle(screen, color , pos, 40)


### Initializing and printing board
gameboard = Board(7,6)
print (gameboard.matrix)


### Set colors and dimensions of board
background_color = (255,255,255)    #white
width, height = 1000 , 600           #screen dimensions for connect 4
#width, height = 500, 400            #screen dimensions for connect 3
black = (0,0,0)
player = 1                          #Player 1 ges to start first
Time = 0                            #Timer Variable for delay
win = winning.winning(gameboard.matrix)   #winning function to check if game has been won


### Initializing game environment
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Connect 4')
#screen.fill(background_color)


intro = True
running = False
endscreen = False

while intro:
    screen.fill(black)
    font = pygame.font.SysFont("Lucida Sans Typewriter", 13)
    text1 = font.render("Welcome to Connect 4, Press S to start the game. Use 1,2,3,4,5,6,7 keys to place pieces", True, (background_color))
    textrect = text1.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.blit(text1, textrect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            if event.key == pygame.K_s:
                intro = False
                running = True

while running:
    screen.fill(background_color) #set up background
    gameboard.draw(screen)
    basicfont = pygame.font.SysFont(None, 45)
    text = basicfont.render('Player %.2d'%(player) + "'s turn", True, (0, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = 850
    textrect.centery = screen.get_rect().centery
    screen.blit(text, textrect)
    pygame.display.update()



    if player == 2:
        # temp_board = gameboard.matrix.copy()
        # print(temp_board)
        # fake_bot.fake_player(4, temp_board)
        bot.bot_player(4, gameboard.matrix.copy())
        win = winning.winning(gameboard.matrix)
        if win[0] == True:
            running = False
            endscreen = True


    for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                # c = pygame.key.get_pressed()
                # functions.look_through_rows(gameboard.matrix, functions.pygame_key_reader(c) ,player)
                if event.key == pygame.K_1:
                    functions.look_through_rows(gameboard.matrix, 0, player)
                    print('keypress')
                if event.key == pygame.K_2:
                    functions.look_through_rows(gameboard.matrix, 1, player)
                    print('keypress')
                if event.key == pygame.K_3:
                    functions.look_through_rows(gameboard.matrix, 2, player)
                    print('keypress')
                if event.key == pygame.K_4:
                    functions.look_through_rows(gameboard.matrix, 3, player)
                    print('keypress')
                if event.key == pygame.K_5:
                    functions.look_through_rows(gameboard.matrix, 4, player)
                    print('keypress')
                if event.key == pygame.K_6:
                    functions.look_through_rows(gameboard.matrix, 5, player)
                    print('keypress')
                if event.key == pygame.K_7:
                    functions.look_through_rows(gameboard.matrix, 6, player)
                    print('keypress')
                print(gameboard.matrix)

                if player == 1:
                    player = 2
                elif player == 2:
                    player = 1

                gameboard.draw(screen)
                pygame.display.update()

            win = winning.winning(gameboard.matrix)
            if win[0] == True:
                running = False
                endscreen = True


    if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            pygame.quit()
            quit()

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
        text = basicfont.render('Congrats!', True, (0, 0, 255), (255, 255, 255))
        textrect.centerx = 875
        textrect.centery = 250
        screen.blit(text, textrect)
        text = basicfont.render('Player %.2d'%(win[1]) + ' Has Won', True, (0, 0, 255), (255, 255, 255))
        textrect.centerx = 875
        textrect.centery = 250
        screen.blit(text, textrect)

    pygame.display.update()

pygame.quit()
