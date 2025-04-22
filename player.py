import pygame
from pygame.math import Vector2
from circleshape import CircleShape
from constants import COLOUR_WHITE, PLAYER_RADIUS

class Player(CircleShape):
    TRIANGLE_LINE_WIDTH = 2
    TRIANGLE_COLOUR = COLOUR_WHITE

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self) -> list[Vector2]:
        forward: Vector2 = pygame.Vector2(0, 1).rotate(self.rotation) * self.radius # pyright: ignore (not detecting __mul__ overload)
        right: Vector2 = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 # pyright: ignore 
        # create 3 points for the player triangle
        a = self.position + forward # center shifted forward
        b = self.position - forward - right # center shifted back and left
        c = self.position - forward + right # center shifted back and right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, self.TRIANGLE_COLOUR, self.triangle(), self.TRIANGLE_LINE_WIDTH)

