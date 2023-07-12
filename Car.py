import pygame
from random import randint
pygame.init()

x = 545
y = 360

pos_X = 320
pos_Y = 800 #para iniciar fora da tela...

pos_Ya = 800
pos_Yb = 1000

velocidade = 40
velocidadeAux = 5

timer = 0
tempo = 0

fundo = pygame.image.load('BackGround.png')
carro = pygame.image.load('carro.png')
carro2 = pygame.image.load('carro2.png')
policia = pygame.image.load('policia.png')
ambulancia = pygame.image.load('ambulance.png')

font = pygame.font.SysFont('Times New Roman', 30)
texto = font.render("Tempo: ", True,(255,255,255), (0,0,0))
posTexto = texto.get_rect()
posTexto.center = (65,50)

janela = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Criando um jogo com python")

janela_aberta = True

while (janela_aberta):
    pygame.time.delay(50) #o delay para executar o codigo...
    for event in pygame.event.get():  #permite saber que evento foi feito...
        if(event.type == pygame.QUIT): #se o tipo do evento fpr de fechar a janela entao a janelaaberta passa a false...
            janela_aberta = False
    comandos = pygame.key.get_pressed()#pega a tecla pressionada...
    #o eixo começa no canto superior direito da tela, então:
    if comandos[pygame.K_UP] and y >= 30:
        y -= velocidade #se eu quiser subir o ponto, tenho que diminuir o y, para ir em direção ao zero... 
    if comandos[pygame.K_DOWN] and y <= 440:
        y += velocidade #se eu quiser descer tenho que aumentar o y para ir mais para baixo...
    if comandos[pygame.K_RIGHT] and x <= 740:
        x += velocidade #se eu quiser ir a direita aumento o x...
    if comandos[pygame.K_LEFT] and x >= 310:
        x -= velocidade  #se eu quiser ir a esquerda diminuo o x, para ir a esquerda em direção ao zero... 

    #deteta colisao...
    if x + 120 > pos_X+470 and y+190 > pos_Ya: #lado direito...
        y = 500
        
    if x - 90 < pos_X and y - 40 > pos_Y-500: #lado esquerdo...
        y = 500
        
    # if((x + 120 > pos_X+230 and y+190 > pos_Yb) and (x - 90 < pos_X+230 and y - 40 > pos_Yb)): #colisao central...
        #   y = 500

    #para os carros cpu subirem sozinhos...
    pos_Y -= velocidadeAux 
    pos_Ya -= velocidadeAux
    pos_Yb -= velocidadeAux  
    
    if(pos_Y <= -400): #policia
        pos_Y = randint(1000, 1300)
    
    if(pos_Ya <= -400):
        pos_Ya = randint(1300, 1500)
    
    if pos_Yb <= -400: #ambulance
        pos_Yb = randint(1500, 2000)
    
    if (timer < 20): #executa o timer a cada 50 milissegundos...
        timer += 1  
    else:# a cada segundo incrementa...
        tempo +=1
        texto = font.render("Tempo: "+str(tempo),True, (255,255,255), (0,0,0))
        timer = 0  #para ser incrementado a cada 1 segundo...
        
    janela.blit(fundo,(0,0)) #copia a foto para a tela onde a foto irá iniciar no canto 0,0...
    janela.blit(carro,(x,y))
    
    if(tempo==10):
        velocidadeAux = 7
    elif tempo == 15:
        velocidadeAux = 10
    
    pos_Y -= velocidadeAux
    pos_Ya -= velocidadeAux
    pos_Yb -= velocidadeAux   
    
    #carro policia...
    janela.blit(policia, (pos_X,  pos_Y-500))
    #carro 2...
    janela.blit(carro2, (pos_X+440, pos_Ya))
    #carro ambulance...
    janela.blit(ambulancia, (pos_X+230, pos_Yb))
    
    janela.blit(texto, (posTexto))
    pygame.display.update()#deve atualizar apos fazer o desenho...
pygame.quit()