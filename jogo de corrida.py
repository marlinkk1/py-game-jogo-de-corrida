import pygame
import random

# Inicializa o Pygame
pygame.init()

# Constantes
LARGURA_TELA = 800
ALTURA_TELA = 600
COR_FUNDO = (255, 255, 255)
COR_CARRO = (255, 0, 0)
COR_OBSTACULO = (0, 255, 0)
VELOCIDADE_CARRO = 10
VELOCIDADE_OBSTACULO = 20
FPS = 55
BLACK=(0,0,0)

# Cria a tela do jogo
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Jogo de Carro')

# Carregar imagens
imagem_carro = pygame.Surface((50, 100))
imagem_carro.fill(COR_CARRO)

imagem_obstaculo = pygame.Surface((50, 100))
imagem_obstaculo.fill(COR_OBSTACULO)

# Função para desenhar o carro
def desenhar_carro(x, y):
    tela.blit(imagem_carro, (x, y))

# Função para desenhar os obstáculos
def desenhar_obstaculos(obstaculos):
    for obstaculo in obstaculos:
        tela.blit(imagem_obstaculo, (obstaculo[0], obstaculo[1]))

# Função para mover os obstáculos
def mover_obstaculos(obstaculos):
    for obstaculo in obstaculos:
        obstaculo[1] += VELOCIDADE_OBSTACULO
    return [o for o in obstaculos if o[1] < ALTURA_TELA]

# Função principal do jogo
def jogo():
    # Posições iniciais
    x_carro = LARGURA_TELA // 2 - 25
    y_carro = ALTURA_TELA - 120

    # Lista de obstáculos
    obstaculos = []

    # Clock para controlar a taxa de atualização
    clock = pygame.time.Clock()

    # Variáveis de controle
    rodando = True
    pontos = 0

    while rodando:
        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Movimentação do carro
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and x_carro > 0:
            x_carro -= VELOCIDADE_CARRO
        if teclas[pygame.K_RIGHT] and x_carro < LARGURA_TELA - 50:
            x_carro += VELOCIDADE_CARRO

        # Criar novos obstáculos
        if random.randint(1, 100) <= 5:
            x_obstaculo = random.randint(0, LARGURA_TELA - 50)
            obstaculos.append([x_obstaculo, -100])  # posição inicial acima da tela

        # Mover obstáculos
        obstaculos = mover_obstaculos(obstaculos)

        # Verificar colisão
        for obstaculo in obstaculos:
            if (x_carro < obstaculo[0] + 50 and x_carro + 50 > obstaculo[0] and
                    y_carro < obstaculo[1] + 100 and y_carro + 100 > obstaculo[1]):
                rodando = False

        # Atualizar pontos
        pontos += 1

        # Preencher o fundo
        tela.fill(COR_FUNDO)

        # Desenhar o carro
        desenhar_carro(x_carro, y_carro)

        # Desenhar obstáculos
        desenhar_obstaculos(obstaculos)

        # Exibir a pontuação
        fonte = pygame.font.SysFont(None, 36)
        texto_pontos = fonte.render(f'Pontos: {pontos}', True, (255, 255, 255))
        tela.blit(texto_pontos, (10, 10))

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de quadros
        clock.tick(FPS)

    # Exibir a pontuação final
    tela.fill(BLACK)
    texto_final = fonte.render(f'Game Over! Pontos: {pontos}', True, (255, 255, 255))
    tela.blit(texto_final, (LARGURA_TELA // 2 - 100, ALTURA_TELA // 2))
    pygame.display.flip()
    pygame.time.delay(3000)

# Iniciar o jogo
jogo()

# Finalizar o Pygame
pygame.quit()