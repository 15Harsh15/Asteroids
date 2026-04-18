import pygame
from shot import Shot
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH,PLAYER_SHOOT_SPEED
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots,drawable,updatable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()
    player = Player(x, y)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots :
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        # player.draw(screen)
        # player.update(dt)
        
main()
 