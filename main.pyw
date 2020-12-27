import pygame, sys, random, math, pickle
pygame.init()
screen = pygame.display.set_mode([500,500])
screen.fill([255,255,255])
pygame.display.flip()

try:
    pickle_file = open('pi.data', 'rb')
    data_list = pickle.load(pickle_file)
    pickle_file.close()
    string = "Prior data loaded..."
    string_font = pygame.font.Font(None, 46)
    string_surf = string_font.render(string, 1, (0, 0, 255))
    screen.blit(string_surf, [100, 230])
    pygame.display.flip()

    pygame.time.delay(1500)
except:
    data_list = [0,0]

In  = data_list[0]
Out = data_list[1]
counter = 0
color  = 255
color_change_per_step   = -5
active  = True

screen.fill([255,255,255])

while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

            pickle_file = open('pi.data', 'wb')
            pickle.dump([In,Out], pickle_file)
            pickle_file.close()

            screen.fill([255,255,255])
            string = "Data saved..."
            string_font = pygame.font.Font(None, 46)
            string_surf = string_font.render(string, 1, (0, 0, 255))
            screen.blit(string_surf, [150, 230])
            pygame.display.flip()

            pygame.time.delay(1500)

            pygame.quit()


    for i in range(20000):
        
        x = random.random() * 500
        y = random.random() * 500
        delta = math.sqrt(x ** 2 + (500 - y) ** 2)
        if delta <= 500:
            In += 1
            farb_liste = [0, 355 - color, 0]
        else:
            Out += 1
            farb_liste = [color, 0, 0]
            
        if i % 100 == 0:
            screen.set_at([int(x), int(y)], farb_liste)

            counter += 1
            if counter == 1000:
                counter = 0
                color += color_change_per_step
                if color <= 100 or color >= 255:
                    color_change_per_step = -color_change_per_step
        
    pygame.draw.circle(screen, [0, 0, 0], [0, 500], 500, 4)

    Pi = (float(In) / (Out + In)) * 4
    pygame.draw.rect(screen, [0,0,0],[0,410,500,70],0)

    string = "In: " + str(In)
    string_font = pygame.font.Font(None, 36)
    string_surf = string_font.render(string, 1, (0, 0, 255))
    screen.blit(string_surf, [10, 420])

    string = "Out: " + str(Out)
    string_font = pygame.font.Font(None, 36)
    string_surf = string_font.render(string, 1, (0, 0, 255))
    screen.blit(string_surf, [250, 420])

    string = "Pi: ~" + str(Pi) #str(round(Pi, 5))
    string_font = pygame.font.Font(None, 36)
    string_surf = string_font.render(string, 1, (0, 0, 255))
    screen.blit(string_surf, [10, 450])
    pygame.display.flip()
