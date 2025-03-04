import pygame
from circleshape import CircleShape





class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, surface):
        # Draw a circle representing the asteroid
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        # Update the asteroid's position based on its velocity
        self.position += self.velocity * dt
