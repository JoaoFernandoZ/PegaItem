import pygame
from personagem import *
from item       import *
pygame.init()

__TamanhoJanela = (800,500)
__TamanhoPlayer = (40,40)
__PosicaoInicial    = ((__TamanhoJanela[0]/2)-__TamanhoPlayer[0]/2  , __TamanhoJanela[1]-__TamanhoPlayer[1])

__TamanhoCarro  = (50,50)
__Controles     = (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, 0)

Jogadores       = []

Tela            = pygame.display.set_mode(__TamanhoJanela)
pygame.display.set_caption("Pega Item")

__Fundo     = pygame.image.load("Imagens/Fundo.jpg")
__Fundo     = pygame.transform.scale(__Fundo, __TamanhoJanela)

EstaRodando = True

Clock       = pygame.time.Clock()

while EstaRodando:
    Eventos = pygame.event.get()

    for evento in Eventos:
        if evento.type == pygame.QUIT: EstaRodando = False
    
    Tela.fill((25,25,25))
    Tela.blit(__Fundo, (0,0))

    pygame.display.update()
    Clock.tick(60)