from pgzero.builtins import animate
from static import bee
from random import uniform, randint

class BeeAnimation:
    def __init__(self, screen):
        self.screen = screen
        self.first_animation = True
        self.screen_width = self.screen.surface.get_size()[0]
        self.overflow = int(100*(self.screen_width/500))
        self.last_animation_x = None

    @staticmethod
    def get_speed():
        return uniform(3, 6)

    def set_screen(self, screen):
        self.screen = screen
        self.screen_width = self.screen.surface.get_size()[0]

    def animate_bee(self):
        bee.y = randint(100, self.screen.surface.get_size()[1] - 100)
        if self.first_animation:
            animate(bee, duration=3, on_finished=self.animate_bee, pos=(-2*self.overflow, bee.y))
            self.last_animation_x = -2*self.overflow
            self.first_animation = False
        speed = self.get_speed()
        if bee.x < -self.overflow:
            animate(bee, duration=speed, on_finished=self.animate_bee, pos=(self.screen_width+2*self.overflow, bee.y))
            self.last_animation_x = self.screen_width+2*self.overflow
            bee.flip(True, False)
        if bee.x > self.screen_width+self.overflow:
            animate(bee, duration=speed, on_finished=self.animate_bee, pos=(-2*self.overflow, bee.y))
            self.last_animation_x = -2*self.overflow
            bee.flip(True, False)

    def reset_animation(self):
        speed = self.get_speed()
        left = self.last_animation_x < 0
        if left:
            animate(bee, duration=speed, on_finished=self.animate_bee, pos=(-2*self.overflow, bee.y))
        else:
            animate(bee, duration=speed, on_finished=self.animate_bee, pos=(self.screen_width+2*self.overflow, bee.y))