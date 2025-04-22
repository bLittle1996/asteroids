import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        self.containers: list[pygame.sprite.Group] = []

        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(x, y)
        self.radius = radius
    
       
    def draw(self, screen: pygame.Surface):
        pass

    # delta_time is in seconds
    def update(self, delta_time: int):
        pass
