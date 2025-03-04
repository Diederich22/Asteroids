import pygame
from player import Player
from constants import *


def main():

    clock = pygame.time.Clock()

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")

    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:

        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        screen.fill("black")

        player.update(dt)

        player.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
