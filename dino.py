# import moduls here
import pygame
from random import randint

Cloud_img = pygame.image.load("./img/cloud.png")


class Menu:
    def __init__(self) -> None:
        for i in range(3):
            Cloud(randint(0,1024))
        # loop variabls
        self.running = True
        self.startGame = False

        # seting menu
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
        scale = 1+(randint(-50, 50)/100) 
        print(f"{scale}x")
        self.Cloud_img = pygame.transform.scale(Cloud_img, (159 * scale, 57 * scale))

    def render(self):
        screen.blit(self.Cloud_img, (self.x, self.y))

    def update(self):
        if self.x <= -150:
            clouds.remove(self)
        else:
            self.x -= 8 * (100/(self.y + 50)) * dt
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


# this list will hold all of the objects it is named after.
# by going throug these list with a for loop you can run a condition on all instencesn of a class

# place to set up the leval
buttons = []
clouds = []

pygame.init()
screen = pygame.display.set_mode((1024, 256))
pygame.display.set_caption("Dino")
pygame.display.set_icon(pygame.image.load("./img/green cactus.png"))
clock = pygame.time.Clock()
menu = Menu()
dt = 0


# Example file showing a basic pygame "game loop"


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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT] and not player.onLaddder:
        friction = False
        player.setVelocityX("a")

    # updates the player (location)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((183, 201, 226))
    if len(clouds) == 0:
        Cloud()
    for cloud in clouds:
        cloud.update()
    
    # RENDER GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
