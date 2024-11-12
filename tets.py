import pygame
import random

# Inicializa o Pygame
pygame.init()

# Constantes
LARGURA_TELA = 600
ALTURA_TELA = 800
VELOCIDADE_CARRO = 10
VELOCIDADE_OBSTACULO = 10
FPS = 55
BLACK = (0, 0, 0)
COR_FUNDO = (255, 255, 255)  # Fundo branco para a tela inicial

# Cria a tela do jogo
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Jogo de Carro')

# Carregar imagens
imagem_carro = pygame.image.load('c:/Users/SENAI/Downloads/carro.png.png')  # Substitua pelo caminho da sua imagem
imagem_carro = pygame.transform.scale(imagem_carro, (50, 100))  # Ajusta o tamanho da imagem

imagem_obstaculo = pygame.image.load('c:/Users/SENAI/Downloads/obistaculo.png.png')  # Substitua pelo caminho da sua imagem
imagem_obstaculo = pygame.transform.scale(imagem_obstaculo, (50, 100))  # Ajusta o tamanho da imagem

# Carregar o sprite de fundo
imagem_fundo = pygame.image.load('c:/Users/SENAI/Desktop/rua.png.jpg')  # Substitua pelo caminho do seu fundo
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA_TELA, ALTURA_TELA))  # Ajusta o tamanho do fundo para cobrir a tela

# Função para desenhar o fundo
def desenhar_fundo():
    tela.blit(imagem_fundo, (0, 0))

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

        # Preencher o fundo com o sprite de fundo
        desenhar_fundo()

        # Desenhar o carro
        desenhar_carro(x_carro, y_carro)

        # Desenhar obstáculos
        desenhar_obstaculos(obstaculos)

        # Exibir a pontuação
        fonte = pygame.font.SysFont(None, 36)
        texto_pontos = fonte.render(f'Pontos: {pontos}', True, (0, 0, 0))
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

# Função para desenhar o botão "Jogar"
def desenhar_botao_jogar():
    fonte = pygame.font.SysFont(None, 48)
    texto = fonte.render("Jogar", True, (255, 255, 255))
    largura_botao = texto.get_width() + 20
    altura_botao = texto.get_height() + 20
    pos_x = LARGURA_TELA // 2 - largura_botao // 2
    pos_y = ALTURA_TELA // 2 - altura_botao // 2

    # Desenha o botão
    pygame.draw.rect(tela, (0, 128, 0), (pos_x, pos_y, largura_botao, altura_botao))
    tela.blit(texto, (pos_x + 10, pos_y + 10))

    return pygame.Rect(pos_x, pos_y, largura_botao, altura_botao)

# Função para a tela inicial
def tela_inicial():
    rodando = True
    while rodando:
        # Tela inicial com fundo branco
        tela.fill(COR_FUNDO)

        # Título
        fonte_titulo = pygame.font.SysFont(None, 64)
        texto_titulo = fonte_titulo.render("Jogo de Carro", True, (0, 0, 0))
        tela.blit(texto_titulo, (LARGURA_TELA // 2 - texto_titulo.get_width() // 2, ALTURA_TELA // 4))

        # Botão Jogar
        botao_jogar = desenhar_botao_jogar()

        # Atualizar a tela
        pygame.display.flip()

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi dentro da área do botão
                if botao_jogar.collidepoint(evento.pos):
                    jogo()  # Inicia o jogo quando clicar no botão
                    rodando = False

# Iniciar a tela inicial
tela_inicial()

# Finalizar o Pygame
pygame.quit()
