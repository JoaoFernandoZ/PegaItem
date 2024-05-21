import pygame
import random
from personagem import *
from item       import *
pygame.init()

########### [ CONFIGURAÇÕES ] ###########

__TamanhoJanela = (1920,1080) #800,500
__Scala = (__TamanhoJanela[0]/800, __TamanhoJanela[1]/500)
__TamanhoPlayer = (65 *__Scala[0] ,65 *__Scala[0]) #65,65
__TamanhoItem  = (45 *__Scala[0] ,45 *__Scala[0]) #45,45
__Controles     = (pygame.K_a, pygame.K_d)
__QuantidadeFrutas = 14 * __Scala[0] #15
__QuantidadeBombas = 3 * __Scala[0] #8
__VelocidadePlayer = 5 * __Scala[0]
__VelocidadeFruta = 6 * __Scala[0]

#########################################

__PosicaoInicial    = ((__TamanhoJanela[0]/2)-__TamanhoPlayer[0]/2  , __TamanhoJanela[1]-__TamanhoPlayer[1])

Jogadores       = []
Items           = []

Tela            = pygame.display.set_mode(__TamanhoJanela)
pygame.display.set_caption("Pega Item")

__Fundo     = pygame.image.load("Imagens/Fundo.jpg")
__Fundo     = pygame.transform.scale(__Fundo, __TamanhoJanela)

EstaRodando = True

Clock       = pygame.time.Clock()

Jogadores.append(Personagem("Imagens/Personagem.png", __TamanhoPlayer, __PosicaoInicial, __Controles, __VelocidadePlayer, __Scala))

for Frutas in range(0,int(__QuantidadeFrutas),1):
    X = random.randint(0,__TamanhoJanela[0]-__TamanhoItem[0])
    Items.append(Item(f"Imagens/comida_{random.randint(1,6)}.png", __TamanhoItem, X, __VelocidadeFruta, __TamanhoJanela, False, __Scala))

for Bombas in range(0,int(__QuantidadeBombas),1):
    X = random.randint(0,__TamanhoJanela[0]-__TamanhoItem[0])
    Items.append(Item("Imagens/bomba.png", __TamanhoItem, X, __VelocidadeFruta+1, __TamanhoJanela, True, __Scala))

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

        for Item in Items:
            ItemPosY = Item.Posicao[1]
            ItemPosX = Item.Posicao[0]

            Hb = (ItemPosX-JogadorPosX, ItemPosY-JogadorPosY)

            if Jogador.Mascara.overlap(Item.Mascara, Hb):
                if Item.Dano == True:
                    Jogador.Posicao = [__PosicaoInicial[0], __PosicaoInicial[1]]
                    Item.Posicao[1] = 0-random.randint(0,25)
                    Item.Posicao[0] = random.randint(0,__TamanhoJanela[0]-Item.Tamanho[0])
                else:
                    Item.Posicao[1] = 0-random.randint(0,25)
                    Item.Posicao[0] = random.randint(0,__TamanhoJanela[0]-Item.Tamanho[0])

    for Item in Items:
        Item.Andar(__TamanhoJanela)
        Item.Posicionar(Tela)

    pygame.display.update()
    Clock.tick(60)