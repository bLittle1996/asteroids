import pygame
from pygame.constants import K_a, K_d, K_s, K_w
from pygame.math import Vector2
from circleshape import CircleShape
from constants import COLOUR_WHITE, PLAYER_RADIUS, PLAYER_ROTATION_SPEED, PLAYER_SPEED

class Player(CircleShape):
    TRIANGLE_LINE_WIDTH = 2
    TRIANGLE_COLOUR = COLOUR_WHITE

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: float = 0
    
    def triangle(self) -> list[Vector2]:
        forward: Vector2 = Vector2(0, 1).rotate(self.rotation) * self.radius 
        right: Vector2 = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        # create 3 points for the player triangle
        a = self.position + forward # center shifted forward
        b = self.position - forward - right # center shifted back and left
        c = self.position - forward + right # center shifted back and right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, self.TRIANGLE_COLOUR, self.triangle(), self.TRIANGLE_LINE_WIDTH)

    def move(self, delta_time: float):
        self.velocity = Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * delta_time
        self.position += self.velocity

    def update(self, delta_time: float):
        keys = pygame.key.get_pressed()

        if keys[K_a]:
            self.rotation += -PLAYER_ROTATION_SPEED * delta_time
        if keys[K_d]:
            self.rotation += PLAYER_ROTATION_SPEED * delta_time
        if keys[K_w]:
           self.move(delta_time)
        if keys[K_s]:
           self.move(delta_time)


    def get_forwards_unit_vector(self) -> Vector2:
        return Vector2(0, 1).rotate(self.rotation)
