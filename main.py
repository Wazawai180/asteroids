import pygame
import constants
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000
            
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()