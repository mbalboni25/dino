# import modules here
import pygame
import os
from random import randint

import pygame.draw_py

# Initializing imgs


img = "img"

# load Logo
logo_img = pygame.image.load(os.path.join(img, "Logo.png"))
# Load Dino
dino_img1 = pygame.image.load(os.path.join(img, "dino", "frame1.png"))
dino_img2 = pygame.image.load(os.path.join(img, "dino", "frame2.png"))
dino_img3 = pygame.image.load(os.path.join(img, "dino", "frame3.png"))
# Load ducking Dino
dino_ducking_img1 = pygame.image.load(os.path.join(img, "dino", "duck_frame1.png"))
dino_ducking_img2 = pygame.image.load(os.path.join(img, "dino", "duck_frame2.png"))
dino_ducking_img3 = pygame.image.load(os.path.join(img, "dino", "duck_frame3.png"))

# Load ditto
ditto_img1 = pygame.image.load(os.path.join(img, "ditto", "frame1.png"))
ditto_img2 = pygame.image.load(os.path.join(img, "ditto", "frame2.png"))
ditto_img3 = pygame.image.load(os.path.join(img, "ditto", "frame3.png"))
ditto_ducking_img = pygame.image.load(os.path.join(img, "ditto", "duck_frame.png"))

obs_green = pygame.image.load(os.path.join(img, "green cactus.png"))
obs_yellow = pygame.image.load(os.path.join(img, "yellow cactus.png"))
obs_meteor = pygame.image.load(os.path.join(img, "Supreme_Meteor.png"))
green_img = pygame.transform.scale(obs_green, (30, 60))
yellow_img = pygame.transform.scale(obs_yellow, (30, 60))
meteor_img = pygame.transform.scale(obs_meteor, (55, 30))

# Load the image cloud
Cloud_img = pygame.image.load(os.path.join(img, "cloud.png"))

# Load ground
ground_img = pygame.image.load(os.path.join(img, "ground.png"))
# resize rhe ground
scaled_ground_img = pygame.transform.scale(ground_img, (2048, 69.5))

# music setup (testing mode)
pygame.mixer.init()
step = pygame.mixer.Sound(os.path.join(img, "running.mp3"))
music = pygame.mixer.music.load(os.path.join(img, "game music.mp3"))
ping = pygame.mixer.Sound(os.path.join(img, "trimmed ping.mp3"))

# Setup variables
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 256
START_X = 120
START_Y = 220
COLOR = (30, 230, 230)  # color is just a temporary replacement for the actual dino imgs

# hit boxes for the standing and ducking dino
STAND_W = 35
STAND_H = 75
DUCK_W = 60
DUCK_H = 50
prev_x = 1000
dt = 0

# CAN's CODE
# Classes for the game startup menu, buttons, and helper functions for the opening screen


class Menu:
    """
    propertes:
    running: make false to close the game
    startGame: starts the game
    soundOn: shows if the sound is on

    metods:
    seting(self) -> None: hides all butons and then shows only seting menu buttons
    main(self) -> None: hides all butons and then shows only main menu buttons
    """

    def __init__(self) -> None:
        for i in range(3):
            Cloud(randint(0, 1024))
        # loop variables
        self.running = True
        self.startGame = False
        self.score = 1
        self.lastScore = self.score

        self.setDino()

        # Loading all the buttons for

        # game over menu
        Button(408, 192, 208, 32, "game over", self.main, name="back to menu")

        # setings menu
        Button(300, 64, 190, 32, "setting", skinChange, name="skinChange")
        Button(500, 64, 208, 32, "setting", self.main, name="back to menu")

        # main menu
        self.logoShow = True
        Button(350, 50, 76, 32, "main", StartGame, name="play")
        # Button(480, 32, 76, 32, "main", StartGame, name="skin")
        Button(350, 95, 140, 32, "main", self.setting, name="settings")
        self.main()

    def setDino(self):
        # standing animations
        self.run_img1 = pygame.transform.scale(dino_img2, (75, 75))
        self.run_img2 = pygame.transform.scale(dino_img3, (75, 75))

        # ducking animations
        self.duck_img1 = pygame.transform.scale(dino_ducking_img2, (100, 50))
        self.duck_img2 = pygame.transform.scale(dino_ducking_img3, (100, 50))

        # jumping animations
        self.jump_img1 = pygame.transform.scale(dino_img1, (75, 75))
        self.jump_img2 = pygame.transform.scale(dino_ducking_img1, (100, 50))
        self.skin = "dino"

    def setDitto(self):
        # standing animations
        self.run_img1 = pygame.transform.scale(ditto_img2, (75, 81.25))
        self.run_img2 = pygame.transform.scale(ditto_img3, (75, 81.25))

        # ducking animations
        self.duck_img1 = pygame.transform.scale(ditto_ducking_img, (100, 50))
        self.duck_img2 = pygame.transform.scale(ditto_ducking_img, (100, 50))

        # jumping animations
        self.jump_img1 = pygame.transform.scale(ditto_img1, (75, 81.25))
        self.jump_img2 = pygame.transform.scale(ditto_ducking_img, (100, 50))

        self.skin = "ditto"

    def gameOver(self):
        self.window = "game over"
        self.logoShow = False
        for button in buttons:
            button.show = False
            if button.window == "game over":
                button.show = True

    def setting(self) -> None:
        """
        shows only buttons in the settings window
        """
        self.window = "setting"
        self.logoShow = False
        for button in buttons:
            button.show = False
            if button.window == "setting":
                button.show = True

    def main(self) -> None:
        """
        shows only buttons in the main window
        """
        self.window = "main"
        self.logoShow = True
        for button in buttons:
            button.show = False
            if button.window == "main":
                button.show = True


def StartGame():
    # function for the starting button that starts the game
    menu.startGame = True


def skinChange():
    # function for the skin button that changes the skin from off to on and viceversa
    if menu.skin == "dino":
        menu.skin = "ditto"
        menu.setDitto()
    else:
        menu.skin = "dino"
        menu.setDino()


class Cloud:
    """
    propertes:
    clouds: a list of all clouds
    x: the x cordinat of the cloud
    y: the y cordinat of the cloud
    nextCloudIn: the time it will take for this cloud to genaret a new one
    Cloud_img: a randomly scaled cloud img
    methods:
    render(self) -> None: renders the cloud
    update(self) -> None: moves the cloud on the x directon, if the cloud is out of the window it despawns it, also calls render() and creats new clouds if nextCloudIn is = to 0
    """

    def __init__(self, x=1024):
        clouds.append(self)
        self.x = x
        self.y = randint(0, 100)
        self.nextCloudIn = randint(300 * len(clouds), 600 * len(clouds))
        scale = 1 + (randint(-50, 50) / 100)
        self.Cloud_img = pygame.transform.scale(Cloud_img, (159 * scale, 57 * scale))

    def render(self) -> None:
        screen.blit(self.Cloud_img, (self.x, self.y))

    def update(self) -> None:
        if self.x <= -150:
            clouds.remove(self)
        else:
            self.x -= (8 * (100 / (self.y + 50)) + dino.moveBy) * dt
            self.nextCloudIn -= 1
            if len(clouds) < 10:
                if self.nextCloudIn == 0:
                    Cloud()
            elif self.nextCloudIn == 0:
                self.nextCloudIn = 1
            self.render()


class Ground:
    """
    propertes:
    x: the x cordinet of the ground

    methods:
    render(self) -> None: moves the ground and then puts it onto the screen
    """

    def __init__(self) -> None:
        self.rect = pygame.Rect(0, START_Y, SCREEN_WIDTH, 20)
        self.x = 0

    def render(self) -> None:
        self.x -= dino.moveBy * dt
        if self.x <= -1025:
            self.x = 0
        screen.blit(scaled_ground_img, (self.x, 187))


class Button:
    """
    propertes:
    buttons: a List of all buttons
    react: the button hitbox (a pygame.rect)
    coolDown: button coldown to stop instantanus clicking
    func: function given to the button to exacute
    window: which menu window the button is in
    name: the text that is displayed on the button
    mouseOn: boolen that shows if the mous is on the button
    show: shows the button

    methods:
    render(self) -> None: Renders the button whith text placed on the button
    update(self) -> None: checks if the button is clicked
    """

    def __init__(self, x, y, width, height, window, func, name="Button") -> None:
        buttons.append(self)
        self.react = pygame.Rect(x, y, width, height)
        self.coolDown = 0
        self.func = func
        self.window = window
        self.name = name
        self.mouseOn = False
        self.show = False

    def render(self) -> None:
        if self.show:
            textRect = pygame.Rect(
                self.react.x + 8,
                self.react.y + 8,
                self.react.width - 16,
                self.react.height - 16,
            )
            font = pygame.font.Font(os.path.join(img, "PressStart2P-Regular.ttf"), 16)
            if self.name == "skinChange":
                if menu.skin == "dino":
                    text = font.render("Skin: dino", True, "yellow")
                else:
                    text = font.render("Skin: ditto", True, "yellow")
            else:
                text = font.render(self.name, True, "yellow")
            if self.mouseOn:
                pygame.draw.rect(screen, (252, 157, 3), self.react, border_radius=10)
                screen.blit(text, textRect)
            else:
                pygame.draw.rect(screen, (0, 0, 0), self.react, border_radius=10)
                screen.blit(text, textRect)

    def update(self) -> None:
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
class Obstacle:
    def __init__(self, x):
        # obstacles.append(self)

        # randomly determines if the cactus is yellow or green
        # will change a bit once we add birds

        self.type = randint(0, 2)
        if menu.score <= 1000:
            self.type = randint(0, 1)
        if self.type == 0:
            self.image = green_img
            self.box = pygame.Rect(
                x, START_Y - 60, 30, 60
            )  # placeholder box for the moment
        elif self.type == 1:
            self.image = yellow_img
            self.box = pygame.Rect(
                x, START_Y - 60, 30, 60
            )  # placeholder box for the moment
        else:
            new_y = START_Y - 30
            tier = randint(0, 2)
            if tier == 1:
                new_y -= 55
                # print('mid')
            else:
                new_y -= tier * 40
            self.image = meteor_img
            self.box = pygame.Rect(x, new_y, 55, 30)  #'''

        # this is to test the metors
        # self.image = meteor_img
        # self.box = pygame.Rect(x, START_Y-30-55, 55, 30)
        # img stuff here:

        # self.box = pygame.Rect(x, START_Y -65 -randint(-5, 3), 35, 70) #placeholder box for the moment

    def render(self):
        # pygame.draw.rect(screen, (0, 0, 0), self.box)
        screen.blit(self.image, (self.box.x, self.box.y))

    def move(self):
        self.box.x -= dino.moveBy * dt

    def remove(self):
        if self.box.x < -100:
            obstacles.remove(self)
            add_obs()


def check_losing():
    for obs in obstacles:
        if dino.rect.colliderect(obs.box):
            # print("hit a box")
            # step.stop()
            menu.startGame = False
            # pygame.quit()


# adds a new obstacle within a randomized distance of the last one
def add_obs():
    global prev_x
    if len(obstacles) > 0:
        prev_x = obstacles[-1].box.x
    new_x = prev_x + randint(250, 600) + dino.speed / 5
    obstacles.append(Obstacle(new_x))
    # return new_x

    prev_x = new_x


class Dino:
    """
    propertes:
    methods:
    """

    def __init__(self):
        self.moveBy = 50
        self.frameTime = 0
        self.usedFrame = menu.run_img1
        self.usedFrame_duck = menu.duck_img1
        # how fast dino moves in the x direction

        # Attribute initalizers
        self.image = COLOR
        # switches between ducking and standing states
        self.is_standing = True
        self.was_standing = True
        # checks if the dino is jumping or not
        self.on_ground = True
        # controls the dino jump (essentially y velocity)
        self.velocityY = 0

        self.speed = 300

        # sets up with defaults
        self.rect = pygame.Rect(START_X, START_Y - STAND_H, STAND_W, STAND_H)

    # brings the dino up
    def jump(self):
        self.rect.y -= 2
        self.velocityY = -9  # update as necessary to change the power of the jump

    # drags the dino back down if it's in the air
    def gravity(self):
        if dino.is_standing:
            self.rect.width = STAND_W
            self.rect.height = STAND_H
            if not self.was_standing:
                self.rect.y -= 25
            self.was_standing = True

        else:
            self.rect.width = DUCK_W
            self.rect.height = DUCK_H
            if self.was_standing:
                self.rect.y += 25
            self.was_standing = False
        self.on_ground = False
        if self.on_ground:
            pass
        elif self.rect.colliderect(ground.rect):
            self.on_ground = True
            self.velocityY = 0
            self.rect.bottom = ground.rect.top + 1
        else:
            self.on_ground = False
        if not self.on_ground:
            # update as necessary to change the falling speed
            self.velocityY += 21 * dt
            # if the dino ducks while jumping, speed increases
            if not self.is_standing:
                self.velocityY += 64 * dt  # 10 is hardcoded arbitrary extra fall
            # speed limit
            if self.velocityY > 25:
                self.velocityY = 25

    def update(self):
        if self.speed <= 500:
            self.speed += 5 * dt
        menu.score += self.speed / 1000
        self.rect.y += self.velocityY

        if round(menu.score) % 400 == 0:
            ping.play()
        # switches between states

    # Makes the RECT for the dino
    # self.x is CENTERED
    # self.y is represents the BOTTOM
    # makes the rect represent the top left corner

    def draw(self):
        # simple for now but may update later when we add the images of the dino
        # pygame.draw.rect(screen, self.image, self.rect)
        self.frameTime -= 1
        # if self.frameTime == 5:
        # step.stop()
        if self.frameTime <= 0:
            self.frameTime = 10
            if not self.on_ground:
                step.stop()
                self.usedFrame = menu.jump_img1
            elif self.usedFrame == menu.run_img1:
                step.play(maxtime=100)
                self.usedFrame = menu.run_img2
            elif self.usedFrame == menu.run_img2 or self.usedFrame == menu.jump_img1:
                step.play(maxtime=100)
                self.usedFrame = menu.run_img1
            if not self.on_ground:
                step.stop()
                self.usedFrame_duck = menu.jump_img2
            elif (
                self.usedFrame_duck == menu.duck_img1
                or self.usedFrame_duck == menu.jump_img2
            ):
                step.play(maxtime=100)
                self.usedFrame_duck = menu.duck_img2
            elif self.usedFrame_duck == menu.duck_img2:
                step.play(maxtime=100)
                self.usedFrame_duck = menu.duck_img1

        if self.is_standing:
            screen.blit(self.usedFrame, (self.rect.x - 20, self.rect.y))
        else:
            screen.blit(self.usedFrame_duck, (self.rect.x - 20, self.rect.y))

    def reset(self):
        self.moveBy = 50
        self.frameTime = 0
        self.usedFrame = menu.run_img1
        self.usedFrame_duck = menu.duck_img1
        # how fast dino moves in the x direction

        # Attribute initalizers
        self.image = COLOR
        # switches between ducking and standing states
        self.is_standing = True
        self.was_standing = True
        # checks if the dino is jumping or not
        self.on_ground = True
        # controls the dino jump (essentially y velocity)
        self.velocityY = 0

        self.speed = 300
        menu.lastScore = menu.score
        menu.score = 1

        self.rect.x = START_X
        self.rect.y = START_Y - STAND_H


def reset():
    dino.reset()
    global obstacles
    global prev_x
    obstacles = []
    prev_x = 1000
    for i in range(6):
        add_obs()
    menu.gameOver()


def main():
    while menu.startGame:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu.running = False
                menu.startGame = False

        # setup
        keys = pygame.key.get_pressed()

        # First check if dino is on the ground and standing

        # make updatements to dino
        dino.is_standing = not (keys[pygame.K_DOWN] or keys[pygame.K_s])

        if (
            (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w])
            and dino.on_ground
            and dino.is_standing
        ):
            dino.jump()
        dino.gravity()
        dino.update()

        # implement updatements

        # RENDER GAME HERE
        # fill the screen with a color to wipe away anything from last frame
        screen.fill((183, 201, 226))

        # RENDER GAME HERE
        dino.moveBy = dino.speed
        ground.render()
        if len(clouds) == 0:
            Cloud()
        for cloud in clouds:
            cloud.update()

        for obs in obstacles:
            obs.move()
            obs.render()

        obstacles[0].remove()

        # checks score for ping

        check_losing()

        # pygame.draw.rect(screen, 0, GROUND_RECT)
        dino.draw()

        font = pygame.font.Font(os.path.join(img, "PressStart2P-Regular.ttf"), 16)
        text = font.render("Score:" + str(round(menu.score)), True, "black")
        screen.blit(text, (5, 5))

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
    reset()


# this list will hold all of the objects it is named after.
# by going throug these list with a for loop you can run a condition on all instencesn of a class
# place to set up the leval
buttons = []
clouds = []


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(
    "                                                                                                                                                                                                                                                                            Dino Dash"
)
pygame.display.set_icon(logo_img)
logo_img = pygame.transform.scale(logo_img, (153, 134))
clock = pygame.time.Clock()
ground = Ground()

menu = Menu()
# dino!
dino = Dino()


obstacles = []

for i in range(6):
    add_obs()


# sets up the ground rect spanning the entire width of the screen

# pygame.mixer.music.play(loops=-1)
step.set_volume(1)
pygame.mixer.music.set_volume(0.5)
while menu.running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu.running = False

    # updates the player (location)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((183, 201, 226))

    ground.render()

    if len(clouds) == 0:
        Cloud()
    for cloud in clouds:
        cloud.update()

    # RENDER GAME HERE
    if menu.logoShow:
        screen.blit(logo_img, (150, 45))

    for button in buttons:
        button.update()
        button.render()

    if menu.window == "game over":
        font = pygame.font.Font(os.path.join(img, "PressStart2P-Regular.ttf"), 32)
        text = font.render("Game Over", True, "black")
        screen.blit(text, (380, 50))
        font = pygame.font.Font(os.path.join(img, "PressStart2P-Regular.ttf"), 16)
        text = font.render(f"score: {round(menu.lastScore)}", True, "black")
        screen.blit(text, (420, 98))

    # flip() the display to put your work on screen
    pygame.display.flip()
    if menu.startGame:
        main()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
