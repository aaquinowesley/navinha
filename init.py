import pygame
import os 
from pygame.constants import K_a, K_d, K_w, K_x
from config import *


pygame.init()

janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))


diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'img')
diretorio_sons = os.path.join(diretorio_principal, 'sons')

print(diretorio_principal)

# Título e ícone
pygame.display.set_caption("NAVW1")

icone = pygame.image.load("img/icone.png")
pygame.display.set_icon(icone)

# Background

fundo = pygame.image.load('img/bg.jpg')

# Nave

imagemNave = pygame.image.load('img/nave_azul.png')

imagemBala = pygame.image.load('img/bala.png')

# Ocultar a visibilidade do mouse
pygame.mouse.set_visible(False)

 
pygame.mixer.music.load('sons/theme.mp3')
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.1)


#funções 
def player(x,y):
    janela.blit(imagemNave, (x, y))


def camera():
    janela.blit()

def tiro():
    janela.blit(imagemBala, ())


deve_continuar = True

while deve_continuar:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
            os.sys.exit()


        if playerX <= 0:
            playerX = 0
        elif playerX >= 436:
            playerX = 400

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            playerX -= 20
        if event.key == pygame.K_d:
            playerX += 20
        if event.key == pygame.K_w:
            playerY -= 20
        if event.key == pygame.K_s:
            playerY += 20
        if event.key == pygame.K_SPACE:
            tiro(playerX, tiroY)
        if event.key == pygame.K_m:
            if somAtivado:
                pygame.mixer.music.stop()
                somAtivado = False
            else:
                pygame.mixer.music.play(-1, 0.0)
                somAtivado = True 

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            playerX -= 5
        if event.key == pygame.K_d:
            playerX += 5
        if event.key == pygame.K_w:
            playerY -= 5
        if event.key == pygame.K_s:
            playerY += 5

    janela.blit(fundo, (0,0))
    player(playerX,playerY)
    relogio.tick(FPS)
    pygame.display.update()