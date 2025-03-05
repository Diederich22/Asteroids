import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape





class Asteroid(CircleShape):

    def __init__(self,x,y,radius,velocity=None):
        super().__init__(x,y,radius)
        if velocity is None:
            self.velocity =  pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        else:
            self.velocity = velocity





    def draw(self, surface):
        # Draw a circle representing the asteroid
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        # Update the asteroid's position based on its velocity
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20, 50)
        min_speed = 2.0
        velocity1 = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
        velocity2 = pygame.math.Vector2.rotate(self.velocity, -angle) * 1.2
        A1 = Asteroid(self.position.x, self.position.y, new_radius, velocity2)
        A2 = Asteroid(self.position.x, self.position.y, new_radius, velocity1)

        for group in self.groups():
            group.add(A1)
            group.add(A2)
