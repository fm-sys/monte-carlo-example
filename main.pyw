import pygame, sys, random, math, pickle
pygame.init()
screen = pygame.display.set_mode([500,500])
screen.fill([255,255,255])
pygame.display.flip()

try:
    pickle_datei = open('pi.data', 'rb')
    entpickelte_liste = pickle.load(pickle_datei)
    pickle_datei.close()
    anweisung = "Daten wurden geladen..."
    anweisung_font = pygame.font.Font(None, 46)
    anweisung_surf = anweisung_font.render(anweisung, 1, (0, 0, 255))
    screen.blit(anweisung_surf, [50, 230])
    pygame.display.flip()

    pygame.time.delay(1500)
except:
    entpickelte_liste = [0,0]

In  = entpickelte_liste[0]
Out = entpickelte_liste[1]
zaeler = 0
farbe  = 255
plus   = -5
aktiv  = True

screen.fill([255,255,255])

while aktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            aktiv = False

            pickle_datei = open('pi.data', 'wb')
            pickle.dump([In,Out], pickle_datei)
            pickle_datei.close()

            screen.fill([255,255,255])
            anweisung = "Daten wurden gesichert..."
            anweisung_font = pygame.font.Font(None, 46)
            anweisung_surf = anweisung_font.render(anweisung, 1, (0, 0, 255))
            screen.blit(anweisung_surf, [50, 230])
            pygame.display.flip()

            pygame.time.delay(1500)

            pygame.quit()


    for i in range(5000):
        zaeler += 1
        if zaeler == 1000:
            zaeler = 0
            farbe += plus
            if farbe <= 100 or farbe >= 255:
                plus = -plus

        x = random.random() * 500
        y = random.random() * 500
        delta = math.sqrt(x ** 2 + (500 - y) ** 2)
        if delta <= 500:
            In += 1
            farb_liste = [0, 355-farbe, 0]
        else:
            Out += 1
            farb_liste = [farbe, 0, 0]
            
        if i % 100 == 0: screen.set_at([int(x), int(y)], farb_liste)
        
    pygame.draw.circle(screen, [0, 0, 0], [0, 500], 500, 3)

    Pi = (float(In) / (Out + In)) * 4
    pygame.draw.rect(screen, [0,0,0],[0,410,500,70],0)

    anweisung = "In: " + str(In)
    anweisung_font = pygame.font.Font(None, 36)
    anweisung_surf = anweisung_font.render(anweisung, 1, (0, 0, 255))
    screen.blit(anweisung_surf, [10, 420])

    anweisung = "Out: " + str(Out)
    anweisung_font = pygame.font.Font(None, 36)
    anweisung_surf = anweisung_font.render(anweisung, 1, (0, 0, 255))
    screen.blit(anweisung_surf, [250, 420])

    anweisung = "Pi: ~" + str(Pi) #str(round(Pi, 5))
    anweisung_font = pygame.font.Font(None, 36)
    anweisung_surf = anweisung_font.render(anweisung, 1, (0, 0, 255))
    screen.blit(anweisung_surf, [10, 450])
    pygame.display.flip()
