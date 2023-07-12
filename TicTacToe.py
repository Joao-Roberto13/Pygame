import pygame
import numpy as np
from random import randint
pygame.init()

screen = pygame.display.set_mode((900,600))
screen.fill((28,170,156))
pygame.display.set_caption('TIC TAC TOE')


board = np.zeros((3,3))#numer de linhas e colunas

def draw_lines():
    # linha horizontal  1
    pygame.draw.line(screen,(23,145,135), (50, 200), (550, 200), 7)
    #linha horizontal 2    
    pygame.draw.line(screen,(23,145,135), (50, 400), (550, 400), 7)

    #linha vertical 1
    pygame.draw.line(screen,(23,145,135), (200, 50), (200, 550), 7)
    #linha vertical 2
    pygame.draw.line(screen,(23,145,135), (400, 50), (400, 550), 7)

def mark_square(row, col, player): #serve para marcar a linha selecionada... 
    board[row][col] = player

def isAvailable(row, col):
    return board [row][col] == 0 #se tiver zero no nosso arraybidimensional significa que não foi ocupado, retorna true...

def isFull():
    for row in range(3):
        for col in range(3):
            if isAvailable(row, col):
                return False
    return True

def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1: #signica que player 1 marcou o quadrado...
                pygame.draw.circle(screen, (239,231,200), (int(col*200+200/2), int(row*200+200/2)),60,15)#a col selecionada * o tamanho do quadrado + o tamanho do quadrado a dividir por 2 nos da o centro...
            elif board[row][col] == 2:
                pygame.draw.line(screen, (66, 66, 66), (col * 200 + 55, row * 200 + 200 - 55), (col * 200 + 200 - 55, row * 200 + 55), 25)
                pygame.draw.line(screen, (66, 66, 66), (col * 200 + 55, row * 200 + 55), (col * 200 + 200 - 55, row * 200 + 200 - 55), 25)

def check_win(player):
    #vertical win cehck...
    for col in range(3):
        if board [0][col] == player and board [1][col] == player and board [2][col] == player:
            draw_vertical_line(col, player)
            return True

    #horizontal win check...
    for row in range(3):
        if board[row][0] == player and  board[row][1] == player and board[row][2] == player:
            draw_horizontal_line(row, player)
            return True

    #asc diagonal win check...
    if board[2][0] == player and board [1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_dsc_diagonal(player)
        return True

    return False

def draw_vertical_line(col, player):
    posX = col * 200 + 200/2 # uma ver que é linha vertica significa que na tal coluna o eixo x não muda...
    if player == 1:
        color = (239,231,200)
    elif player == 2:
        color = (66, 66, 66)
    pygame.draw.line(screen,color,(posX,15), (posX, 600-15),15)

def draw_horizontal_line(row, player):
    posY = row * 200 + 200/2 # uma ver que é linha vertica significa que na tal coluna o eixo x não muda...
    if player == 1:
        color = (239,231,200)
    elif player == 2:
        color = (66, 66, 66)
    pygame.draw.line(screen,color,(15,posY), (600-15, posY),15) 

def draw_asc_diagonal(player):#crescrente...
    if player == 1:
        color = (239,231,200)
    elif player == 2:
        color = (66, 66, 66)

    pygame.draw.line(screen,color,(15,600-15), (600-15, 15),15) 

def draw_dsc_diagonal(player):#decrescente...
    if player == 1:
        color = (239,231,200)
    elif player == 2:
        color = (66, 66, 66)

    pygame.draw.line(screen,color,(15,15), (600-15,600 - 15), 15) 

def restart():
    screen.fill((28,170,156))
    draw_lines()
    player = randint(1, 2)

    for row in range(3):
        for col in range(3):
            board[row][col] = 0
draw_lines()

player = 1 
gameOver = False
font = pygame.font.SysFont('Times New Roman', 30)
contX = 0
contO = 0
contE = 0

#main loop...
open = True #mantem janela aberta...
while(open):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False #janela ira fechar
        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:#mouseclicker...
            mouseX = event.pos[0] #faz get das coordenadas do x...
            mouseY = event.pos[1] #get y...
            
            clicked_row = int(mouseY // 200)#200 é o tamanho de cada quadradro...
            clicked_col = int(mouseX // 200)# a // piso
        
            if clicked_col < 3:
                if(isAvailable(clicked_row, clicked_col)):
                    if player == 1:
                        mark_square(clicked_row, clicked_col, 1)
                        if check_win(player):
                            gameOver = True
                            contX += 1
                        player = 2
                        
                    elif player == 2:
                        mark_square(clicked_row, clicked_col, 2)
                        if check_win(player):
                            gameOver = True
                            contO += 1
                        player = 1
                    draw_figures()
            if(isFull() and gameOver == False):
                    contE += 1
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(600,30,280,550),400)
    
        texto = font.render("Highlight: ", False,(0,0,0), (255,252,255))
        screen.blit(texto, (670,50))
        
        textoX = font.render("X: "+str(contX), False,(28,170,156), (255,255,255))
        screen.blit(textoX, (620, 120))
        
        textoO = font.render("O: "+str(contO), False,(28,170,156), (255,255,255))
        screen.blit(textoO, (620, 170))
        
        textoE = font.render("X&O: "+str(contE), False,(28,170,156), (255,255,255))
        screen.blit(textoE, (620, 220))
        
        textoR = font.render("R to restart", False,(28,170,156), (255,255,255))
        screen.blit(textoR, (620, 300))
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                gameOver = False

    pygame.display.update()