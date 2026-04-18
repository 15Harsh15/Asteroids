from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
import random
from logger import log_event
class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self,dt):
        self.position+= self.velocity*dt 
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
                    return
        log_event("asteroid_split")
        
        first_asteroid_velocity=self.velocity.rotate(random.uniform(20,50))
        second_asteroid_velocity = self.velocity.rotate((random.uniform(-20,-50)))
        new_asteroid_radius = self.radius-ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid1.velocity=first_asteroid_velocity*1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid2.velocity=second_asteroid_velocity*1.2 