import pygame
from pygame.math import Vector2

from circleshape import CircleShape
from constants import COLOUR_WHITE

class Bullet(CircleShape):
    BULLET_CALIBER = 5 # its just radius, but cool sounding
    BULLET_SPEED = 500 # very fast bullet (pew pew)
    def __init__(self, x, y):
        super().__init__(x, y, self.BULLET_CALIBER)
        self.image = pygame.Surface([self.BULLET_CALIBER * 2, self.BULLET_CALIBER * 2])
        self.image.fill(COLOUR_WHITE)
        self.velocity = Vector2(0, 1) * self.BULLET_SPEED

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, COLOUR_WHITE, self.position, self.radius)

    def update(self, delta_time: float) -> None:
        self.position += self.velocity * delta_time
        
