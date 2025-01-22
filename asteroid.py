import pygame
import random
from circleshape import *
from constants import *
from logic import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        angle = random.uniform(20, 50)
        new_velocity_1= self.velocity.rotate(angle) * 1.2
        new_velocity_2= self.velocity.rotate(-angle) * 1.2
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS

        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            
            return
        
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = new_velocity_1
        new_asteroid_2.velocity = new_velocity_2
        