import pygame
from shot import Shot
from circleshape import CircleShape
from constants import PLAYER_RADIUS,LINE_WIDTH,PLAYER_TURN_SPEED,PLAYER_SPEED,PLAYER_SHOOT_SPEED,PLAYER_SHOOT_COOLDOWN_SECONDS
class Player(CircleShape) :
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cool_down = 0
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),LINE_WIDTH)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def move(self,dt,current_speed):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * current_speed * dt
        self.position += rotated_with_speed_vector
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cool_down -= dt
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
           current_speed = 400
        else:
            current_speed = PLAYER_SPEED
        if keys[pygame.K_s] or  keys[pygame.K_DOWN]:
            self.move(-dt, current_speed) 
        if keys[pygame.K_w] or  keys[pygame.K_UP]:
            self.move(dt, current_speed)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_SPACE] or keys[pygame.K_0] or keys[pygame.K_KP0]:
            self.shoot()
    def shoot(self):
        if self.shot_cool_down <= 0:
            new_shot = Shot(self.position.x, self.position.y)
            new_shot.velocity = pygame.math.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
            self.shot_cool_down = PLAYER_SHOOT_COOLDOWN_SECONDS
    