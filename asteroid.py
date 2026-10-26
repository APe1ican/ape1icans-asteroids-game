import pygame
from constants import *
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "White", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        ran_angle = random.uniform(20, 50)
        left_split_rotation = self.velocity.rotate(ran_angle)
        right_split_rotation = self.velocity.rotate(-ran_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid_1.velocity = left_split_rotation * 1.2
        asteroid_2.velocity = right_split_rotation * 1.2
