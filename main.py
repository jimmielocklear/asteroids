import sys
import pygame
from constants import *
import player
import asteroid
import asteroidfield
import shot
from circleshape import CircleShape
from logger import log_state, log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable, )
    shot.Shot.containers = (updatable, drawable, shots)


    game_asteroids = asteroidfield.AsteroidField()
    my_player = player.Player(x, y)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")




    while True:
        
        log_state()

        screen.fill("black")



        dt = game_clock.tick(60) / 1000



        updatable.update(dt)

        for a in asteroids:
            if a.collides_with(my_player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()


        for d in drawable:
            d.draw(screen)

        pygame.display.flip()


        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return






if __name__ == "__main__":
    main()
