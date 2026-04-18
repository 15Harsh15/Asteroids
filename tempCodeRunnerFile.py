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
    game_over = False
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
    font = pygame.font.Font(None, 36)
    score = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main() # This re-runs the game from the start
                    return # This closes the current "dead" instance
        if not game_over:
            updatable.update(dt)
            for asteroid in asteroids:
                for shot in shots :
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")
                        asteroid.split()
                        shot.kill()
                        score += 10
                if asteroid.collides_with(player):
                    log_event("player_hit")
                    print("Game over!")
                    game_over = True
        screen.fill("black")
        # Render the text: (text, antialias, color)
        score_surface = font.render(f"Score: {score}", True, "white")

        # Draw it at coordinates (x, y)
        screen.blit(score_surface, (10, 10))
        for draw in drawable:
            draw.draw(screen)
        if game_over:
        # Create a larger font for the "Game Over" text
            big_font = pygame.font.Font(None, 72)
            msg_surface = big_font.render("GAME OVER", True, "red")
            # Update instruction to say ENTER
            retry_surface = font.render("Press ENTER to Restart", True, "white")
            screen.blit(msg_surface, (SCREEN_WIDTH / 2 - 140, SCREEN_HEIGHT / 2 - 50))
            screen.blit(retry_surface, (SCREEN_WIDTH / 2 - 120, SCREEN_HEIGHT / 2 + 20))
        pygame.display.flip()
        dt = clock.tick(60)/1000
        # player.draw(screen)
        # player.update(dt)
        
main()
 