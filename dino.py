# import modules here
import pygame
from random import randint

# Initializing imgs
Cloud_img = pygame.image.load("./img/cloud.png")

# Setup variables
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 256
START_X = 120
START_Y = 208
COLOR = (30, 230, 230)  # color is just a temporary replacement for the actual dino imgs

# hit boxes for the standing and ducking dino
STAND_W = 20
STAND_H = 50
DUCK_W = 50
DUCK_H = 20


# CAN's CODE
# Classes for the game startup menu, buttons, and helper functions for the opening screen


class Menu:
    def __init__(self) -> None:
        for i in range(3):
            Cloud(randint(0, 1024))
        # loop variables
        self.running = True
        self.startGame = False

        # setings menu
        Button(300, 64, 173, 32, "seting", soundChange, name="sound")
        self.soundOn = True
        Button(500, 64, 208, 32, "seting", self.main, name="back to menu")

        # main menu
        Button(384, 32, 76, 32, "main", StartGame, name="play")
        Button(480, 32, 76, 32, "main", StartGame, name="skin")
        Button(608, 32, 128, 32, "main", self.seting, name="setings")
        self.main()

    def seting(self):
        for button in buttons:
            button.show = False
            if button.window == "seting":
                button.show = True

    def main(self):
        for button in buttons:
            button.show = False
            if button.window == "main":
                button.show = True


def StartGame():
    menu.startGame = True


def soundChange():
    if menu.soundOn:
        menu.soundOn = False
    else:
        menu.soundOn = True


class Cloud:
    def __init__(self, x=1024):
        clouds.append(self)
        self.y = randint(0, 100)
        self.x = x
        self.nextCloudIn = randint(300 * len(clouds), 600 * len(clouds))
        scale = 1 + (randint(-50, 50) / 100)
        self.Cloud_img = pygame.transform.scale(Cloud_img, (159 * scale, 57 * scale))

    def render(self):
        screen.blit(self.Cloud_img, (self.x, self.y))

    def update(self):
        if self.x <= -150:
            clouds.remove(self)
        else:
            self.x -= 8 * (100 / (self.y + 50)) * dt
            self.nextCloudIn -= 1
            if len(clouds) < 10:
                if self.nextCloudIn == 0:
                    Cloud()
            elif self.nextCloudIn == 0:
                self.nextCloudIn = 1
            self.render()


class Button:
    def __init__(self, x, y, width, height, window, func, name="Button") -> None:
        buttons.append(self)
        self.react = pygame.Rect(x, y, width, height)
        self.coolDown = 0
        self.func = func
        self.window = window
        self.name = name
        self.mouseOn = False
        self.show = False

    def render(self):
        if self.show:
            textRect = pygame.Rect(
                self.react.x + 8,
                self.react.y + 8,
                self.react.width - 16,
                self.react.height - 16,
            )
            font = pygame.font.Font("./img/PressStart2P-Regular.ttf", 16)
            if self.name == "sound":
                if not menu.soundOn:
                    text = font.render("Sound: Off", True, "green")
                else:
                    text = font.render("Sound: On", True, "green")
            else:
                text = font.render(self.name, True, "green")
            if self.mouseOn:
                pygame.draw.rect(screen, (255, 255, 255), self.react, border_radius=10)
                screen.blit(text, textRect)
            else:
                pygame.draw.rect(screen, (0, 0, 0), self.react, border_radius=10)
                screen.blit(text, textRect)

    def update(self):
        if self.coolDown > 0:
            self.coolDown -= 1
        elif self.show:
            self.mouseOn = False
            if self.react.collidepoint(pygame.mouse.get_pos()):
                self.mouseOn = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.coolDown = 15
                    self.func()


# Dino class made by Sophie
class Dino:
    def __init__(self):
        #how fast dino moves in the x direction
        self.speed = 10
        # Attribute initalizers
        self.image = COLOR
        # switches between ducking and standing states
        self.is_standing = True
        # checks if the dino is jumping or not
        self.on_ground = True
        # controls the dino jump (essentially y velocity)
        self.velocityY = 0

        # sets up with defaults
        self.x = START_X
        self.y = START_Y
        self.w = STAND_W
        self.h = STAND_H
        self.make_box()

    # brings the dino up
    def jump(self):
        self.on_ground = False
        self.velocityY = -7  # adjust as necessary to change the power of the jump

    # drags the dino back down if it's in the air
    def gravity(self):
        if self.on_ground:
            self.velocityY = 0
            self.y = (
                START_Y + 1
            )  # the +1 is just to make sure the code registers that the two boxes are touching
        else:
            # adjust as necessary to change the falling speed
            self.velocityY += 16 * dt

            # if the dino ducks while jumping, speed increases
            if not dino.is_standing:
                self.velocityY += 32 * dt  # 10 is hardcoded arbitrary extra fall
        # speed limit
        if self.velocityY > 25:
            self.velocityY = 25

    def adjust(self):
        if not self.on_ground:
            self.y += self.velocityY + 1
            if self.y > START_Y:
                self.y = START_Y + 1

        # switches between states
        if dino.is_standing:
            dino.w = STAND_W
            dino.h = STAND_H
        else:
            dino.w = DUCK_W
            dino.h = DUCK_H

        self.make_box()

    # Makes the RECT for the dino
    # self.x is CENTERED
    # self.y is represents the BOTTOM
    # makes the rect represent the top left corner
    def make_box(self):
        self.box = pygame.Rect(self.x - self.w / 2, self.y - self.h, self.w, self.h)

    def draw(self):
        # simple for now but may adjust later when we add the images of the dino
        pygame.draw.rect(screen, self.image, self.box)


# this list will hold all of the objects it is named after.
# by going throug these list with a for loop you can run a condition on all instencesn of a class
# place to set up the leval
buttons = []
clouds = []

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino")
pygame.display.set_icon(pygame.image.load("./img/green cactus.png"))
clock = pygame.time.Clock()
# dino!
dino = Dino()
menu = Menu()

dt = 0


# sets up the ground rect spanning the entire width of the screen
GROUND_RECT = pygame.Rect(0, START_Y, SCREEN_WIDTH, 20)


while not menu.startGame:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu.running = False
            menu.startGame = True

    # updates the player (location)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((183, 201, 226))
    if len(clouds) == 0:
        Cloud()
    for cloud in clouds:
        cloud.update()

    # RENDER GAME HERE
    for button in buttons:
        button.update()
        button.render()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000



while menu.running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu.running = False

    # setup
    keys = pygame.key.get_pressed()

    # First check if dino is on the ground and standing
    dino.on_ground = dino.box.colliderect(GROUND_RECT)
    dino.is_standing = not keys[pygame.K_DOWN]

    # make adjustments to dino
    dino.gravity()
    if keys[pygame.K_SPACE] and dino.on_ground and dino.is_standing:
        dino.jump()

    # implement adjustments
    dino.adjust()

    # RENDER GAME HERE
    # fill the screen with a color to wipe away anything from last frame
    screen.fill((183, 201, 226))

    # RENDER GAME HERE

    if len(clouds) == 0:
        Cloud()
    for cloud in clouds:
        cloud.update()
    pygame.draw.rect(screen, 0, GROUND_RECT)
    dino.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
