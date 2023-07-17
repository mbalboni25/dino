import pygame





# this list will hold all of the objects it is named after.
# by going throug these list with a for loop you can run a condition on all instencesn of a class

# place to set up the leval
pygame.init()
screen = pygame.display.set_mode((1024, 256))
clock = pygame.time.Clock()
dt = 0

# place to set up the leval


# Example file showing a basic pygame "game loop"
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT] and not player.onLaddder:
        friction = False
        player.setVelocityX("a")

    # updates the player (location)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((183, 201, 226))

    # RENDER GAME HERE


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
