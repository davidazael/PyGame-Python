import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 700

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

spaceShip_width = 75
spaceShip_height = 132


gameDisplay = pygame.display.set_mode((display_width ,display_height))
pygame.display.set_caption('Evade Game')
clock = pygame.time.Clock()

backGround = pygame.image.load('galaxy.jpg')                    #call images
spaceImg = pygame.image.load('spaceShip1.png')
meteor2 = pygame.image.load('meteor2.png')

def meteor( x,y ):
    gameDisplay.blit(meteor2, (x,y))

def meteorSecond( x,y ):
    gameDisplay.blit( meteor2, (x,y))

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render( "Dodged: "+ str(count), True, white)
    gameDisplay.blit(text, (0,0))

def space( x,y ):
    gameDisplay.blit(spaceImg,(x,y))															#blits image == blit(displays imgage of choice, (location))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()												#so we can get the rect around our text

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 75)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2),(display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def crash():
    message_display('You Crashed!')
    time.sleep(2)
    game_loop()

def game_loop():
    x = (display_width * .45)
    y = (display_height * .8)
    x_change = 0
    y_change = 0

    xAxis = random.randrange(0, display_width)
    xAxis2 = random.randrange(0, display_width)
    xAxis3 = random.randrange(0, display_width)
    xAxis4 = random.randrange(0, display_width)

    yAxis = 0
    yAxis2 = 0
    yAxis3 = 0
    yAxis4 = 0

    meteor_speed = 10
    meteor2_speed = 7
    meteor3_speed = 12
    meteor4_speed = 15

    meteor_width = 25

    meteor_height = 75

    dodged = 0

    move_left = -5
    move_right = 5
    move_down = 5
    move_up = -5

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:													#if X is pressed then it makes it gameExit to quit so there for it closes the window
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:												#check if there is a key pressed
                if event.key == pygame.K_LEFT:												#if left key is being pressed
                    x_change = move_left
                elif event.key == pygame.K_RIGHT:
                    x_change = move_right

                if event.key == pygame.K_UP:
                    y_change =  move_up
                elif event.key == pygame.K_DOWN:
                    y_change = move_down


            if event.type == pygame.KEYUP:													#when key is relized
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change

    #	gameDisplay.fill('galaxy') 															#make screen fill(color)
        gameDisplay.blit(backGround,(0,0))

        #things(thingx, thingy, thingw, thingh, color)
        meteor( xAxis, yAxis )
        meteor( xAxis2, yAxis2 )

        yAxis  += meteor_speed + .25
        yAxis2  += meteor2_speed + .25
    #	things( thing_startx, thing_starty, thing_width, thing_height, block_color )        #the block its self
    #	thing_starty += thing_speed															#how fast the block will move down

        space(x,y)																			#to show spaceship/ calls SPACESHIP which was definded above
        things_dodged(dodged)

        if x > display_width - spaceShip_width or x < 0:									#if spaceship hits the edges of the window it is now considered a crash
            crash()

        if y > display_height - spaceShip_height or y < 25:
            crash()

        if yAxis > display_height:
            yAxis = 0 - display_height
            xAxis = random.randrange(0,display_width)
            dodged += 1

        if y < yAxis + meteor_height:
            print('meteor works ')

            if x > xAxis and x < xAxis + meteor_width or x + spaceShip_width > xAxis and x + spaceShip_width < xAxis + meteor_width:
                print('crash')
                crash()

        if yAxis2 > display_height:
            yAxis2 = 0 - display_height
            xAxis2 = random.randrange(0,display_width)
            dodged += 1

        if y < yAxis2 + meteor_height:
            print('meteor works2 ')

            if x > xAxis2 and x < xAxis2 + meteor_width or x + spaceShip_width > xAxis2 and x + spaceShip_width < xAxis2 + meteor_width:
                print('crash')
                crash()

        if dodged > 10:
            move_left = -8
            move_right = 8
            move_up = -8
            move_down = 8
            meteor( xAxis3, yAxis3 )
            yAxis3 += meteor3_speed + 1

            if yAxis3 > display_height:
                yAxis3 = 0 - display_height
                xAxis3 = random.randrange(0,display_width)
                dodged += 1

            if y < yAxis3 + meteor_height:
                print('meteor works3 ')

                if x > xAxis3 and x < xAxis3 + meteor_width or x + spaceShip_width > xAxis3 and x + spaceShip_width < xAxis3 + meteor_width:
                    print('crash')
                    crash()

        if dodged > 20:
            move_left = -10
            move_right = 10
            move_up = -10
            move_down = 10

            meteor( xAxis4, yAxis4 )
            yAxis4 += meteor4_speed + 2

            if yAxis4 > display_height:
                yAxis4 = 0 - display_height
                xAxis4 = random.randrange(0,display_width)
                dodged += 1

            if y < yAxis4 + meteor_height:
                print('meteor works3 ')

                if x > xAxis4 and x < xAxis4 + meteor_width or x + spaceShip_width > xAxis4 and x + spaceShip_width < xAxis4 + meteor_width:
                    print('crash')
                    crash()

        pygame.display.update()
        clock.tick( 120 )
game_loop()
