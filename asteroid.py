from circleshape import *
from constants import *
import pygame
import random
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        
        split_angle = random.uniform(20,50)

        split_1_vector = self.velocity.rotate(split_angle)
        split_2_vector = self.velocity.rotate(split_angle) * -1
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_1.velocity = (split_1_vector) * 1.2
        new_2.velocity = (split_2_vector) * 1.2




