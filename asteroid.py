import pygame
import constants
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.position = (x, y)
        self.radius = radius
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface= screen,
                           color= "white",
                           center= self.position,
                           radius= self.radius,
                           width= 2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_vector_pos = self.velocity.rotate(random_angle)
        new_vector_neg = self.velocity.rotate(-random_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_vector_pos * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_vector_neg * 1.2

