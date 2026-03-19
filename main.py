import pygame
from constants import *
import player
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    my_player = player.Player(x, y)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        
        log_state()

        screen.fill("black")



        dt = game_clock.tick(60) / 1000



        my_player.update(dt)
        my_player.draw(screen)

        pygame.display.flip()


        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return






if __name__ == "__main__":
    main()
