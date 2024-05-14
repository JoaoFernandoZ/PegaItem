import pygame
import random


class Item:

    def __init__(self, Imagem : str, Tamanho : tuple, Posicaox : int, Velocidade : int, __TamanhoJanela : tuple, Dano):
        self.Imagem = pygame.image.load(Imagem)
        self.Tamanho = [Tamanho[0], Tamanho[1]]
        self.Posicao = [Posicaox, __TamanhoJanela[1]]
        self.PosicaoInicial = self.Posicao
        self.VelocidadeBase = Velocidade
        self.Velocidade = Velocidade+random.randint(-3,3)
        self.Dano = Dano

        self.Imagem = pygame.transform.scale(self.Imagem, self.Tamanho)

        self.Mascara = pygame.mask.from_surface(self.Imagem)
    
    def Posicionar(self, Tela):
        Tela.blit(self.Imagem, self.Posicao)

    def Andar(self, __TamanhoJanela):
        self.Posicao[1] += self.Velocidade

        if self.Posicao[1] >= __TamanhoJanela[1]:
            self.Posicao[1] = 0-random.randint(0,25)
            self.Posicao[0] = random.randint(0,__TamanhoJanela[0]-self.Tamanho[0])
            self.Velocidade = self.VelocidadeBase+random.randint(-3,3)

# céu*