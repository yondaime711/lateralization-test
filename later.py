import pygame
from datetime import datetime
import time
import pygame.mixer

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
screen = pygame.display.set_mode((640, 480))



#----

for x in range(1):

    screen.fill(white)

    pygame.display.flip()

    time.sleep(3)

    pygame.draw.circle(screen, black,(320, 240), 20)

    pygame.display.flip()

    reaction_start = datetime.now()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                 reaction_end = datetime.now()
                 running = False
    txt=open('wyniki.txt','a')
    print('czas reakcji: ', file=txt)
    print(reaction_end - reaction_start, file=txt)
    txt.close()

#--------------------------------------------------------------------------

for x in range(1):

    screen.fill(white)

    pygame.display.flip()

    time.sleep(3)

    pygame.draw.circle(screen, red,(320, 240), 20)

    pygame.display.flip()

    reaction_start = datetime.now()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                 reaction_end = datetime.now()
                 running = False

    txt=open('wyniki.txt','a')
    print('czas reakcji: ', file=txt)
    print(reaction_end - reaction_start, file=txt)
    txt.close()

#--------------------------------------------------------------------------

for x in range(1):
    screen.fill(white)

    pygame.display.flip()

    time.sleep(3)

    pygame.draw.circle(screen, blue,(320, 240), 20)

    pygame.display.flip()

    reaction_start = datetime.now()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                 reaction_end = datetime.now()
                 running = False

    txt=open('wyniki.txt','a')
    print('czas reakcji: ', file=txt)
    print(reaction_end - reaction_start, file=txt)
    txt.close()


#--------------------------------------------------------------------------

for x in range(1):

    screen.fill(white)

    pygame.display.flip()

    time.sleep(3)

    pygame.draw.circle(screen, green,(320, 240), 20)

    pygame.display.flip()

    reaction_start = datetime.now()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                 reaction_end = datetime.now()
                 running = False

    txt=open('wyniki.txt','a')
    print('czas reakcji: ', file=txt)
    print(reaction_end - reaction_start, file=txt)
    txt.close()


#--------------------------------------------------------------------------

for x in range(1):

    screen.fill(black)

    pygame.display.flip()

    time.sleep(2)

    pygame.draw.circle(screen, white,(320, 240), 20)

    pygame.display.flip()

    reaction_start = datetime.now()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                 reaction_end = datetime.now()
                 running = False

    txt=open('wyniki.txt','a')

    print('czas reakcji: ', file=txt)
    print(reaction_end - reaction_start, file=txt)
    txt.close()

#----
for x in range(1):

    screen.fill(white)

    pygame.display.flip()

    time.sleep(3)

    pygame.draw.circle(screen, black,(320, 240), 20)

    pygame.display.flip()

    reaction_start = datetime.now()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                 reaction_end = datetime.now()
                 running = False
    txt=open('wyniki.txt','a')
    print('czas reakcji: ', file=txt)
    print(reaction_end - reaction_start, file=txt)
    txt.close()

#--------------------------------------------------------------------------

for x in range(1):

    screen.fill(white)

    pygame.display.flip()

    time.sleep(3)

    pygame.draw.circle(screen, red,(320, 240), 20)

    pygame.display.flip()

    reaction_start = datetime.now()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                 reaction_end = datetime.now()
                 running = False

    txt=open('wyniki.txt','a')
    print('czas reakcji: ', file=txt)
    print(reaction_end - reaction_start, file=txt)
    txt.close()

#--------------------------------------------------------------------------

for x in range(1):
    screen.fill(white)

    pygame.display.flip()

    time.sleep(3)

    pygame.draw.circle(screen, blue,(320, 240), 20)

    pygame.display.flip()

    reaction_start = datetime.now()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                 reaction_end = datetime.now()
                 running = False

    txt=open('wyniki.txt','a')
    print('czas reakcji: ', file=txt)
    print(reaction_end - reaction_start, file=txt)
    txt.close()


#--------------------------------------------------------------------------

for x in range(1):

    screen.fill(white)

    pygame.display.flip()

    time.sleep(3)

    pygame.draw.circle(screen, green,(320, 240), 20)

    pygame.display.flip()

    reaction_start = datetime.now()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                 reaction_end = datetime.now()
                 running = False

    txt=open('wyniki.txt','a')
    print('czas reakcji: ', file=txt)
    print(reaction_end - reaction_start, file=txt)
    txt.close()


#--------------------------------------------------------------------------

for x in range(1):

    screen.fill(black)

    pygame.display.flip()

    time.sleep(2)

    pygame.draw.circle(screen, white,(320, 240), 20)

    pygame.display.flip()

    reaction_start = datetime.now()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                 reaction_end = datetime.now()
                 running = False

    txt=open('wyniki.txt','a')

    print('czas reakcji: ', file=txt)
    print(reaction_end - reaction_start, file=txt)
    txt.close()

#----

screen.fill((255, 255, 255))

font = pygame.font.SysFont(None, 30)

text = font.render("NACISNIJ DOWOLNY PRZYCISK ABY WYJSC", 0, (0,255,0))

text_rect = text.get_rect(center=screen.get_rect().center)

screen.blit(text, text_rect)

pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            pygame.quit()