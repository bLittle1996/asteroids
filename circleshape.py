from pygame import Surface
from pygame.math import Vector2
from pygame.sprite import Group, Sprite

class CircleShape(Sprite):
    containers: tuple[Group, ...]

    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: Vector2 = Vector2(x, y)
        self.velocity: Vector2 = Vector2(0, 0)
        self.radius: float = radius
    
       
    def draw(self, screen: Surface) -> None:
        pass

    # delta_time is in seconds
    def update(self, delta_time: float) -> None:
        pass
