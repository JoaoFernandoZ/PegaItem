import pygame
from personagem import *
from item       import *
pygame.init()

__TamanhoJanela = (800,500)
__TamanhoPlayer = (55,55)
__PosicaoInicial    = ((__TamanhoJanela[0]/2)-__TamanhoPlayer[0]/2  , __TamanhoJanela[1]-__TamanhoPlayer[1])

__TamanhoCarro  = (50,50)
__Controles     = (pygame.K_a, pygame.K_d)

Jogadores       = []

Tela            = pygame.display.set_mode(__TamanhoJanela)
pygame.display.set_caption("Pega Item")

__Fundo     = pygame.image.load("Imagens/Fundo.jpg")
__Fundo     = pygame.transform.scale(__Fundo, __TamanhoJanela)

EstaRodando = True

Clock       = pygame.time.Clock()

Jogadores.append(Personagem("imagens/Personagem.gif", __TamanhoPlayer, __PosicaoInicial, __Controles))

while EstaRodando:
    Eventos = pygame.event.get()

    for evento in Eventos:
        if evento.type == pygame.QUIT: EstaRodando = False
    
    Tela.fill((25,25,25))
    Tela.blit(__Fundo, (0,0))

    for Jogador in Jogadores:
        Jogador.Movimentar(__TamanhoJanela)
        Jogador.Posicionar(Tela)

        JogadorPosY = Jogador.Posicao[1]
        JogadorPosX = Jogador.Posicao[0]

    pygame.display.update()
    Clock.tick(60)