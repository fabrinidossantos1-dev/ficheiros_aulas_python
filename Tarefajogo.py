import pygame
import random

pygame.init()

# Dimensões da tela
LARGURA, ALTURA = 600, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha Simples")

relogio = pygame.time.Clock()
tamanho_bloco = 20
velocidade = 10

# Posição inicial da cobra
cobra_x = LARGURA / 2
cobra_y = ALTURA / 2
vel_x = 0
vel_y = 0

comida_x = round(random.randrange(0, LARGURA - tamanho_bloco) / 20) * 20
comida_y = round(random.randrange(0, ALTURA - tamanho_bloco) / 20) * 20

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
                    rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                vel_x = -tamanho_bloco
                vel_y = 0
            elif evento.key == pygame.K_RIGHT:
                vel_x = tamanho_bloco
                vel_y = 0
            elif evento.key == pygame.K_UP:
                vel_y = -tamanho_bloco
                vel_x = 0
            elif evento.key == pygame.K_DOWN:
                vel_y = tamanho_bloco
                vel_x = 0

    cobra_x += vel_x
    cobra_y += vel_y

    tela.fill((0, 0, 0)) # Fundo preto
    # Desenha comida (vermelho)
    pygame.draw.rect(tela, (255, 0, 0), [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
    # Desenha cobra (verde)
    pygame.draw.rect(tela, (0, 255, 0), [cobra_x, cobra_y, tamanho_bloco, tamanho_bloco])

    pygame.display.update()
    relogio.tick(velocidade)

pygame.quit()


