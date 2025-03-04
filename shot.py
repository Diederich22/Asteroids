import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS




class Shot(CircleShape):

    def __init__(self,x,y,velocity):
        super().__init__(x,y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, surface):
        # Draw a circle representing the asteroid
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius)

    def update(self, dt):
        # Update the asteroid's position based on its velocity
        self.position += self.velocity * dt











