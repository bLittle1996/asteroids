import pygame
import os

from pygame.sprite import Group

from asteroid import Asteroid, AsteroidField
from bullet import Bullet
from constants import COLOUR_BLACK, SCREEN_WIDTH, SCREEN_HEIGHT
from eventemitter import EventEmitter
from player import Player

def main():
    print("Starting Asteroids!")
    os.environ['SDL_AUDIODRIVER'] = 'pulseaudio' # ensure we are using an audio driver that #worksonmymachine 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_running = True
    def on_quit(_event):
        nonlocal game_running 
        game_running = False
    EventEmitter.default.on(pygame.QUIT, on_quit)

    updatables, drawables, asteroids, bullets = setup_groups()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    ticker = pygame.time.Clock()
    delta_time = 0.0 # in seconds

    while game_running:
        process_events()
        # updates
        updatables.update(delta_time)
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print('skill issue')
                game_running = False
            for bullet in bullets:
                if asteroid.is_colliding(bullet):
                    asteroid.kill()
                    bullet.kill()

        # draws
        fill_background(screen)
        for drawable in drawables:
            drawable.draw(screen)
        update_screen()

        delta_time = ticker.tick(60) / 1000 # 60 frames per second

def fill_background(surface: pygame.Surface):
    surface.fill(COLOUR_BLACK)

def update_screen():
    pygame.display.flip()

def process_events():
    for event in pygame.event.get():
        EventEmitter.default.emit(event.type, event)

# returns updateable and drawable, in that order
def setup_groups() -> tuple[pygame.sprite.Group, pygame.sprite.Group, pygame.sprite.Group, pygame.sprite.Group]:
    updatable, drawable = pygame.sprite.Group(), pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    # add groups to relevant classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Bullet.containers = (bullets, updatable, drawable)

    return updatable, drawable, asteroids, bullets


if __name__ == "__main__":
    main()
