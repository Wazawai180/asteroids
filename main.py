import pygame
import constants
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from circleshape import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000
            
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                sys.exit("Game Over!")
            for bullet in shots:
                if asteroid.collision_check(bullet) == True:
                    asteroid.split()
                    bullet.kill()

        for objects in drawable:
            objects.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()