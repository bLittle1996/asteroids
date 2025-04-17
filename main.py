import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from event_emitter import EventEmitter
import os

def main():
    print("Starting Asteroids!")
    os.environ['SDL_AUDIODRIVER'] = 'pulseaudio' # ensure we are using an audio driver that #worksonmymachine 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_loop(screen)

def game_loop(surface: pygame.Surface):
    game_running = True

    def on_quit(_event):
        nonlocal game_running 
        game_running = False

    EventEmitter.default.on(pygame.QUIT, on_quit)

    while game_running:
        process_events()
        render_background(surface)
        draw()

def render_background(surface: pygame.Surface):
    surface.fill(pygame.Color([0,0,0,0]))
    

def draw():
    pygame.display.flip()

def process_events():
    for event in pygame.event.get():
        EventEmitter.default.emit(event.type, event)



if __name__ == "__main__":
    main()
