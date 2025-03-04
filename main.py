import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Shot.containers = (drawable, updatable,shots)
Player.containers = (drawable,updatable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)


def main():

    clock = pygame.time.Clock()

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    print("Starting Asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")

    print(f"Screen height: {SCREEN_HEIGHT}")


    while True:

        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                import sys
                sys.exit()

        for sprite in drawable:
            sprite.draw(screen)


        for shot in shots:
            for asteroid in asteroids:
                if shot.is_colliding(asteroid):
                    print(f"Collision detected! Shot: {shot}, Asteroid: {asteroid}")
                    shot.kill()
                    asteroid.kill()



        pygame.display.flip()


if __name__ == "__main__":
    main()
