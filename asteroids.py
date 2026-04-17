from circleshape import Circleshape
class Asteroid (Circleshape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self,surface,color,position,radius,width):
        self.surface = screen
        self.color = "white"
        self.position = (0,0)
        self.radius = radius
        self.width = LINE_WIDTH
    def update(self,velocity)
        velocity = self.velocity
        self.position+= self.velocity*dt 