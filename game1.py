import pygame,sys
pygame.init()
screen=pygame.display.set_mode((1200,800))
pygame.display.set_caption("clf is sb")
bg_color=(230,0,0)
while 1:
    screen.fill(bg_color)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    pygame.display.flip()