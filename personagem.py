import pygame

class Personagem:
    def __init__(self, Imagem : str, Tamanho : tuple, Posicao : tuple, Controles : tuple) -> None:
        self.Imagem = pygame.image.load(Imagem)
        self.Tamanho = [Tamanho[0], Tamanho[1]]
        self.Posicao = [Posicao[0], Posicao[1]]
        self.PosicaoInicial = self.Posicao
        self.Controles = Controles # A = 0 | S = 1

        self.Imagem = pygame.transform.scale(self.Imagem, self.Tamanho)

        self.Mascara = pygame.mask.from_surface(self.Imagem)
    
    def Posicionar(self, Tela):
        Tela.blit(self.Imagem, self.Posicao)

    def Movimentar(self, __TamanhoJanela):
        __TeclasApertadas = pygame.key.get_pressed()

        if __TeclasApertadas[self.Controles[0]] and self.Posicao[0] > 0:
            self.Posicao[0] -= 5
        if __TeclasApertadas[self.Controles[1]] and self.Posicao[0] < __TamanhoJanela[0]-self.Tamanho[0]:
            self.Posicao[0] += 5