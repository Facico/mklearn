import pygame
a=1;
pygame.init()
screen=pygame.display.set_mode((1200,800))
while 1:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
    pygame.display.flip()

