import pygame
import random
from pygame.math import Vector2
from pygame.sprite import Group, Sprite
from typing import Callable

from circleshape import CircleShape
from constants import COLOUR_WHITE, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE, SCREEN_HEIGHT, SCREEN_WIDTH

class Asteroid(CircleShape):
    LINE_WIDTH = 2
    MIN_SIZE = 1

    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, COLOUR_WHITE, self.position, self.radius, self.LINE_WIDTH)

    def update(self, delta_time: float) -> None:
        self.position += self.velocity * delta_time

    def get_size(self) -> int:
        return max(self.MIN_SIZE, int(self.radius // ASTEROID_MIN_RADIUS))

    def split(self) -> None:
        self.kill()
        if self.get_size() == self.MIN_SIZE:
            return
        # spawn two asteroids shooting off in random angles of one size tier lower
        new_size = (self.get_size() - 1) * ASTEROID_MIN_RADIUS
        new_angle = random.uniform(15, 45)
        speed_mod = 1.2 # smaller ones go faster of course!
        left_a = Asteroid(self.position.x, self.position.y, new_size)
        right_a = Asteroid(self.position.x, self.position.y, new_size)
        left_a.velocity = self.velocity.rotate(-new_angle) * speed_mod
        right_a.velocity = self.velocity.rotate(new_angle) * speed_mod
        
            
        



class AsteroidField(Sprite):
    containers: tuple[Group, ...]
    # list of spawn locations (left, right, top, bottom)
    # has a velocity vector and a position lambda that puts it somewhere on that line
    spawn_locations = [
        # left edge |->
        (Vector2(1, 0), lambda variance: Vector2(-ASTEROID_MAX_RADIUS, variance * SCREEN_HEIGHT)),
        # right edge <-|
        (Vector2(-1, 0), lambda variance: Vector2(SCREEN_WIDTH + ASTEROID_MAX_RADIUS, variance * SCREEN_HEIGHT)),
        # top edge _v_
        (Vector2(0, -1), lambda variance: Vector2(variance * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS)),
        # bottom edge _^_
        (Vector2(0, 1), lambda variance: Vector2(variance * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS)),
    ]

    def __init__(self) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
        self.spawn_timer = 0.0

    def spawn(self, radius: int, position: Vector2, velocity: Vector2) -> Asteroid:
         asteroid = Asteroid(position.x, position.y, radius) 
         asteroid.velocity = velocity
         return asteroid

    def update(self, delta_time: int) -> None:
        # do nothing if not enough time has passed  
        self.spawn_timer += delta_time
        if self.spawn_timer < ASTEROID_SPAWN_RATE:
            return

        
        velocity_vector, get_pos = random.choice(self.spawn_locations)
        asteroid_v = velocity_vector * random.randint(30, 100)
        asteroid_v = asteroid_v.rotate(random.randint(-35, 35))
        asteroid_pos = get_pos(random.random())
        asteroid_radius = ASTEROID_MIN_RADIUS * random.randint(1, ASTEROID_KINDS)
        self.spawn(asteroid_radius, asteroid_pos, asteroid_v)
        self.spawn_timer = 0.0
