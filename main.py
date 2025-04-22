import pygame
import os

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

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ticker = pygame.time.Clock()
    delta_time = 0

    while game_running:
        process_events()
        fill_background(screen)
        player.draw(screen)
        update_screen()
        delta_time = ticker.tick(60) / 1000 # 60 frames per second

def fill_background(surface: pygame.Surface):
    surface.fill(COLOUR_BLACK)
    

def update_screen():
    pygame.display.flip()

def process_events():
    for event in pygame.event.get():
        EventEmitter.default.emit(event.type, event)



if __name__ == "__main__":
    main()
