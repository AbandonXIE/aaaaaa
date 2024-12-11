import pygame

pygame.init() # initialize hardware

window = pygame.display.set_mode((1024, 800)) # create a window
pygame.display.set_caption('DEMO of My First Pygame') # name

image_title = pygame.image.load('assets/title.png') # prepare title
window.blit(image_title, (0,0)) # display title
pygame.display.flip() # 1st refresh

image_lab = pygame.image.load('assets/lab.png')
image_castle = pygame.image.load('assets/castle.png')
image_forest = pygame.image.load('assets/forest.png')

image_wall_lab = pygame.image.load('assets/wall_lab.png')

image_castle_battle = pygame.image.load('assets/castle_battle.png')
image_forest_battle = pygame.image.load('assets/forest_battle.png')

image_chicken = pygame.image.load('assets/chicken.png') # prepare chicken
w_chicken, h_chicken = image_chicken.get_size()
image_chicken = pygame.transform.scale(image_chicken,(w_chicken//2, h_chicken//2))
window.blit(image_chicken, (100, 287)) # display chicken

image_pig = pygame.image.load('assets/pig.png') # prepare pig
w_pig, h_pig = image_pig.get_size()
image_pig = pygame.transform.scale(image_pig,(w_pig//2, h_pig//2))
window.blit(image_pig, (250, 363)) # display pig

image_green = pygame.image.load('assets/green.png')
image_green = pygame.transform.scale(image_green,(250, 333))
window.blit(image_green, (560, 403))

image_purple = pygame.image.load('assets/purple.png')

image_red = pygame.image.load('assets/red.png')
image_red = pygame.transform.scale(image_red,(250, 333))
window.blit(image_red, (720, 403))

image_banana = pygame.image.load('assets/banana.png')

font_title = pygame.font.Font('assets/VINERITC.TTF', 80) # set a font
text_title = font_title.render('DEMO of My First Pygame', True, (255, 0, 0)) # create a text
window.blit(text_title, (30, 10)) # display title text

font_title = pygame.font.Font('assets/VINERITC.TTF', 30)
text_title = font_title.render('Press Z to Begin', True, (255, 0, 0))
window.blit(text_title, (410, 140))

text_title = font_title.render('When you play:', True, (255, 0, 0))
window.blit(text_title, (405, 200))
text_title = font_title.render('Press arrow keys to move', True, (255, 0, 0))
window.blit(text_title, (350, 260))
text_title = font_title.render('Press Z to interact', True, (255, 0, 0))
window.blit(text_title, (390, 320))

pygame.mixer.music.load('assets/title_theme.mp3') # load music
pygame.mixer.music.play(-1, 0.0) # play music

world = 0
coins = 0
move = 0
attack = 5
hp = 20
defend = 10

pygame.display.update() # refresh again

while True: # gameloop
    for event in pygame.event.get(): # check event
        if event.type == pygame.QUIT: # check quit
            exit()
        
        background_color = (0, 0, 0) # background black

        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_z]: # check press z
            print("Z key pressed. Starting...")

            world = 2
            window.blit(image_lab, (0,0))
            window.blit(image_wall_lab, (0,0))

            pygame.mixer.music.load('assets/spacelab.mp3')
            pygame.mixer.music.play(-1, 0.0)

            move = 1

            pygame.display.update() # 1st refresh

        #image_red = pygame.transform.scale(30,40)
        #window.blit(image_red, (725, 125))
        #keys = pygame.key.get_pressed()

        #if keys[pygame.K_UP]:
            #red_ingame.y -= game_object.velocity
        #if keys[pygame.K_DOWN]:
            #red_ingame.y += game_object.velocity
        #if keys[pygame.K_LEFT]:
            #red_ingame.x -= game_object.velocity
        #if keys[pygame.K_RIGHT]:
            #red_ingame.x += game_object.velocity