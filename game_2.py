import pygame
import os, random
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0
yellow = 255,255,0
green = 0,155,0

def homeScreen():
    bg_img = pygame.image.load("images/bg.jpg")
    font_1 = pygame.font.Font('fonts/font_1.ttf', 70)
    text_1 = font_1.render('Zombie Attack',True,white)
    font_2 = pygame.font.Font('fonts/font_1.ttf',40)
    text_2 = font_2.render('Press Any Key to Start Game',True,red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                main()

        screen.blit(bg_img, (0,0))
        screen.blit(text_1,(100,100))
        screen.blit(text_2,(50,250))

        pygame.display.update()

def health_bars(zombie_health):
    if zombie_health > 75:
        zombie_health_color = green
    elif zombie_health > 50:
        zombie_health_color = yellow
    elif zombie_health < 0:
        zombie_health_color = white
    else:
        zombie_health_color = red

    pygame.draw.rect(screen, zombie_health_color, (500, 100, zombie_health, 20))



def main():
    bg_img = pygame.image.load("background.png")
    zombie_health = 100
    gun_aimImage = pygame.image.load('images/aim_2.png')
    gun_aimImageWidth = gun_aimImage.get_width()
    gun_aimImageHeight = gun_aimImage.get_height()

    gunImage = pygame.image.load("0/gun_1.png")
    gunImageWidth = gunImage.get_width()
    gunImageHeight = gunImage.get_height()

    zombie_2_Images = os.listdir('images/zombie_2')
    zombie_2_Frames = []
    for i in range(len(zombie_2_Images)):
        img = pygame.image.load('images/zombie_2/' + zombie_2_Images[i])
        zombie_2_Frames.append(img)

    zombieImg = zombie_2_Frames[0]
    zombieImgWidth = zombieImg.get_width()
    zombieImgHeight = zombieImg.get_height()
    zombieY =  height/2 - 150
    zombieX =  width/2 - 200


    shotSound = pygame.mixer.Sound('sounds/shot_sound.wav')

    game = True
    pos = 0
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                shotSound.play()
                if zombieRect.colliderect(gunAimRect):
                    zombie_health -= 10
                    if zombie_health < 0:
                        gameOver()

        posx,posy = pygame.mouse.get_pos()                                              # DOUBT
        gunX,gunY = posx - gun_aimImageWidth / 2, posy - gun_aimImageHeight / 2

        screen.fill(white)
        health_bars(zombie_health)
        pos+=1
        frame = (pos // 40) % len(zombie_2_Frames)

        zombieImg = zombie_2_Frames[frame]

        # zombieImg = zombieFr[frame]
        zombieRect = pygame.Rect(zombieX, zombieY, zombieImgWidth, zombieImgHeight)
        gunAimRect = pygame.Rect(gunX, gunY, gun_aimImageWidth, gun_aimImageHeight)

        screen.blit(bg_img, (0, 0))
        screen.blit(gunImage, (posx, height - gunImageHeight))
        screen.blit(gun_aimImage,  (gunX, gunY))
        screen.blit(zombieImg,(zombieX,zombieY))

        pygame.display.update()

# main()
homeScreen()










