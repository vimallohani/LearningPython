    #! Python 3
'''
Making games with python chapter 2 program 5
'''
import pygame, sys, time
from pygame.locals import*

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Sound!!")

soundObj = pygame.mixer.Sound('badswap.wav')
soundObj.play()
time.sleep(1) #wait and let the sound play for X second
soundObj.stop()

while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()