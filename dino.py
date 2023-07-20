# import modules here
import pygame
import os
from random import randint

# Initializing imgs

# Get the current working directory
# img = os.path.dirname(
#    os.path.abspath("/Users/patetoman/Documents/Git/dino/img/cloud.png")
#)


img = "img"

# load Logo
logo_img = pygame.image.load(os.path.join(img, "Logo.png"))
# Load Dino
dino_img1 = pygame.image.load(os.path.join(img, "dino", "frame1.png")) # TODO like this on all similar lines
dino_img2 = pygame.image.load(os.path.join(img, "dino", "frame2.png"))
dino_img3 = pygame.image.load(os.path.join(img, "dino", "frame3.png"))
# Load ducking Dino
dino_ducking_img1 = pygame.image.load(os.path.join(img, "dino", "duck_frame1.png"))
dino_ducking_img2 = pygame.image.load(os.path.join(img, "dino", "duck_frame2.png"))
dino_ducking_img3 = pygame.image.load(os.path.join(img, "dino", "duck_frame3.png"))

# Load the image cloud
Cloud_img = pygame.image.load("./img/cloud.png")

# Load ground
ground_img = pygame.image.load("./img/ground.png")
# resize rhe ground
scaled_ground_img = pygame.transform.scale(ground_img, (2048, 69.5))

# Setup variables
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 256
START_X = 120
START_Y = 220
COLOR = (30, 230, 230)  # color is just a temporary replacement for the actual dino imgs

# hit boxes for the standing and ducking dino
STAND_W = 75
STAND_H = 75
DUCK_W = 100
DUCK_H = 50


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

        #standing animations
        self.run_img1 = pygame.transform.scale(dino_img2,(75, 75))
        self.run_img2 = pygame.transform.scale(dino_img3,(75, 75))

        #ducking animations
        self.duck_img1 = pygame.transform.scale(dino_ducking_img2,(100, 50))
        self.duck_img2 = pygame.transform.scale(dino_ducking_img3,(100, 50))

        #jumping animations
        self.jump_img1 = pygame.transform.scale(dino_img1,(75, 75))
        self.jump_img2 = pygame.transform.scale(dino_ducking_img1,(100, 50))


        # Loading all the buttons for

        # setings menu
        Button(300, 64, 173, 32, "setting", soundChange, name="sound")
        self.soundOn = True
        Button(500, 64, 208, 32, "setting", self.main, name="back to menu")

        # main menu
        self.logoShow = True
        Button(350, 50, 76, 32, "main", StartGame, name="play")
        # Button(480, 32, 76, 32, "main", StartGame, name="skin")
        Button(350, 95, 140, 32, "main", self.setting, name="settings")
        self.main()

    def setting(self) -> None:
        """
        shows only buttons in the settings window
        """
        self.logoShow = False
        for button in buttons:
            button.show = False
            if button.window == "setting":
                button.show = True

    def main(self) -> None:
        """
        shows only buttons in the main window
        """
        self.logoShow = True
        for button in buttons:
            button.show = False
            if button.window == "main":
                button.show = True


def StartGame():
    # function for the starting button that starts the game
    menu.startGame = True


def soundChange():
    # function for the sound button that changes the sound from off to on and viceversa
    if menu.soundOn:
        menu.soundOn = False
    else:
        menu.soundOn = True


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
            self.x -= (8 * (100 / (self.y + 50)) * dino.speed / 100) * dt
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
        self.x -= (10 + dino.speed / 100) * dt
        if self.x <= -1024:
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
            font = pygame.font.Font("./img/PressStart2P-Regular.ttf", 16)
            if self.name == "sound":
                if not menu.soundOn:
                    text = font.render("Sound: Off", True, "yellow")
                else:
                    text = font.render("Sound: On", True, "yellow")
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
class Dino:
    """
    propertes: 
    methods: 
    """
    def __init__(self):
        self.frameTime = 15
        self.usedFrame = menu.run_img1
        self.usedFrame_duck = menu.duck_img1
        # how fast dino moves in the x direction
        self.speed = 10
        # Attribute initalizers
        self.image = COLOR
        # switches between ducking and standing states
        self.is_standing = True
        self.was_standing = True
        # checks if the dino is jumping or not
        self.on_ground = True
        # controls the dino jump (essentially y velocity)
        self.velocityY = 0

        # sets up with defaults
        self.rect = pygame.Rect(START_X, START_Y - STAND_H, STAND_W, STAND_H)
    # brings the dino up
    def jump(self):
        self.velocityY = -7  # update as necessary to change the power of the jump

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
        if self.rect.colliderect(ground.rect):
            self.on_ground = True
            self.velocityY = 0
            self.rect.bottom = ground.rect.top
        elif not self.on_ground:
            # update as necessary to change the falling speed
            self.velocityY += 16 * dt
            # if the dino ducks while jumping, speed increases
            if not self.is_standing:
                self.velocityY += 32 * dt  # 10 is hardcoded arbitrary extra fall
            # speed limit
            if self.velocityY > 25:
                self.velocityY = 25

        

    def update(self):
        self.rect.y += self.velocityY

        # switches between states
        

    # Makes the RECT for the dino
    # self.x is CENTERED
    # self.y is represents the BOTTOM
    # makes the rect represent the top left corner

    def draw(self):
        # simple for now but may update later when we add the images of the dino
        #pygame.draw.rect(screen, self.image, self.rect)
        self.frameTime -= 1
        if self.frameTime <= 0:
            self.frameTime = 10
            if not self.on_ground:
                self.usedFrame = menu.jump_img1
            elif self.usedFrame == menu.run_img1 or self.usedFrame == menu.jump_img1:
                self.usedFrame = menu.run_img2
            elif self.usedFrame == menu.run_img2:
                self.usedFrame = menu.run_img1
            if not self.on_ground:
                self.usedFrame_duck = menu.jump_img2
            elif self.usedFrame_duck == menu.duck_img1 or self.usedFrame_duck == menu.jump_img2:
                self.usedFrame_duck = menu.duck_img2
            elif self.usedFrame_duck == menu.duck_img2:
                self.usedFrame_duck = menu.duck_img1
        
        if self.is_standing:
            screen.blit(self.usedFrame, (self.rect.x, self.rect.y ))
        else:
            screen.blit(self.usedFrame_duck, (self.rect.x, self.rect.y))



# this list will hold all of the objects it is named after.
# by going throug these list with a for loop you can run a condition on all instencesn of a class
# place to set up the leval
buttons = []
clouds = []

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("                                                                                                                                                                                                                                                                            Dino Dash")
pygame.display.set_icon(logo_img)
logo_img = pygame.transform.scale(logo_img, (153, 134))
clock = pygame.time.Clock()
ground = Ground()
# dino!
menu = Menu()
dino = Dino()



dt = 0


# sets up the ground rect spanning the entire width of the screen


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
    


    # make updatements to dino
    dino.is_standing = not keys[pygame.K_DOWN]

    if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and dino.on_ground and dino.is_standing:
        dino.jump()
    dino.gravity()
    dino.update()

    # implement updatements


    # RENDER GAME HERE
    # fill the screen with a color to wipe away anything from last frame
    screen.fill((183, 201, 226))

    # RENDER GAME HERE
    ground.render()

    if len(clouds) == 0:
        Cloud()
    for cloud in clouds:
        cloud.update()
    # pygame.draw.rect(screen, 0, GROUND_RECT)
    dino.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
