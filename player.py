import pygame
import circleshape
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """Move the player forward based on rotation."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Get direction
        self.position += forward * PLAYER_SPEED * dt  # Move in that direction

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  # Rotate left (counterclockwise)
            self.rotation -= PLAYER_TURN_SPEED * dt  # Subtract to rotate left

        if keys[pygame.K_d]:  # Rotate right (clockwise)
            self.rotation += PLAYER_TURN_SPEED * dt  # Add to rotate right

        if keys[pygame.K_w]:  # Move forward
            self.move(dt)  # No extra argument needed

        if keys[pygame.K_s]:  # Move backward
            self.move(-dt)  # Negative dt for backward movement
