import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()  # Create a Clock object to control FPS
    dt = 0  # Delta time variable

    # Create groups for updating and drawing
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Create player object and add to both groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill screen with black

        # Update all objects in the updatable group
        updatable.update(dt)

        # Draw all objects in the drawable group
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # Refresh the screen
        dt = clock.tick(60) / 1000  # Get delta time in seconds

    pygame.quit()


if __name__ == "__main__":
    main()
