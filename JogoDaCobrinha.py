import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# fundo
fundo = pygame.image.load('imagens/gameover.png')

pygame.mixer.music.set_volume(0.05)
musicadefundo = pygame.mixer.music.load('sons/som.mp3')
pygame.mixer.music.play(-1)

colisao = pygame.mixer.Sound('sons/queissomeufilho.wav')

largura = 640
altura = 480

xcobra = int(largura / 2)
ycobra = int(altura / 2)

velocidade = 10
xcontrole = velocidade
ycontrole = 0

xmaca = randint(40, 600)
ymaca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 20, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Joguinho da cobra')
relogio = pygame.time.Clock()
listaCobra = []
comprimentoInicio = 5
morreu = False


def aumentaC(listaCobra):
    for XeY in listaCobra:
        # XeY = [x, y]
        # XeY[0] = x
        # XeY[1] = y

        pygame.draw.rect(tela, (0, 0, 255), (XeY[0], XeY[1], 20, 20))


def reiniciar():
    global pontos, comprimentoInicio, xcobra, ycobra, listaCobra, listaCabeca, xmaca, ymaca, morreu
    pontos = 0
    comprimentoInicio = 5
    xcobra = int(largura / 2)
    ycobra = int(altura / 2)
    listaCobra = []
    listaCabeca = []
    xmaca = randint(40, 600)
    ymaca = randint(50, 430)
    morreu = False


while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))

    mensagem = f'Pontuação: {pontos}'
    textFormatado = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if xcontrole == velocidade:
                    pass
                else:
                    xcontrole = -velocidade
                    ycontrole = 0
            if event.key == K_d:
                if xcontrole == -velocidade:
                    pass
                else:
                    xcontrole = velocidade
                    ycontrole = 0
            if event.key == K_w:
                if ycontrole == velocidade:
                    pass
                else:
                    ycontrole = -velocidade
                    xcontrole = 0
            if event.key == K_s:
                if ycontrole == -velocidade:
                    pass
                else:
                    ycontrole = velocidade
                    xcontrole = 0

    xcobra = xcobra + xcontrole
    ycobra = ycobra + ycontrole

    cobra = pygame.draw.rect(tela, (0, 0, 255), (xcobra, ycobra, 20, 20))
    maca = pygame.draw.circle(tela, (255, 0, 0), (xmaca, ymaca), 10)

    if cobra.colliderect(maca):
        xmaca = randint(40, 600)
        ymaca = randint(50, 430)
        pontos += 1
        colisao.play()
        comprimentoInicio = comprimentoInicio + 1

    listaCabeca = []
    listaCabeca.append(xcobra)
    listaCabeca.append(ycobra)

    listaCobra.append(listaCabeca)

    if listaCobra.count(listaCabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla de espaço para jogar novamente'
        textFormatado2 = fonte2.render(mensagem, True, (255, 255, 255))
        returnTexto = textFormatado2.get_rect()

        morreu = True
        while morreu:
            tela.blit(fundo, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        reiniciar()

            returnTexto.center = (largura // 2, altura // 2)
            tela.blit(textFormatado2, returnTexto)
            pygame.display.update()

    if xcobra > largura:
        xcobra = 0
    if xcobra < 0:
        xcobra = largura
    if ycobra < 0:
        ycobra = altura
    if ycobra > altura:
        ycobra = 0

    if len(listaCobra) > comprimentoInicio:
        del listaCobra[0]

    aumentaC(listaCobra)

    tela.blit(textFormatado, (450, 40))

    pygame.display.update()