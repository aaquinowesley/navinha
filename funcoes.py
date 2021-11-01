import pygame
from init import janela, imagemNave

corTexto = 255,255,255
teclas = {'esquerda':False,'direita':False,'cima':False,'baixo':False}


def Moverjogador(teclas,dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]


def ColocarTexto(texto, fonte,janela,x,y):
    objTexto = fonte.render(texto,True,corTexto)
    rectTexto = objTexto.get_rect()
    rectTexto.topleft = (x,y)
    janela.blit(objTexto)


