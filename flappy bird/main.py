import pygame
from scripts.cenas import Partida
from scripts.cenas import Menu # importamos a cena 'Menu'

pygame.init()

tamanhoTela = [600, 400]
tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("FlappyBird Clone")
relogio = pygame.time.Clock()
corFundo = (255, 218, 185)

listaCenas = {
    'partida': Partida(tela),
    'menu' : Menu(tela) # adicionamos o menu na cena
}

cenaAtual = 'menu' # mudamos para menu

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
    tela.fill(corFundo)

    cenaAtual = listaCenas[cenaAtual].atualizar()

    relogio.tick(60)
    pygame.display.flip()