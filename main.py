# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()  # Create a Clock object to control FPS
    dt = 0  # Delta time variable

    # Create a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle window close event
                running = False

        screen.fill((0, 0, 0))  # Fill screen with black
        player.update(dt)  # handle movement
        player.draw(screen)
        pygame.display.flip()  # Refresh the screen

        dt = clock.tick(60) / 1000  # Get delta time in seconds


if __name__ == "__main__":

    main()
