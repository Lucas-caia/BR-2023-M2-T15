import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.animation_counter = 0
        self.rect.y = 250

    def update(self, game_speed, obstacles):
        super().update(game_speed, obstacles)
        self.animate()

    def animate(self):
        frames_per_animation = 10
        self.animation_counter += 1

        if self.animation_counter >= frames_per_animation:
            if self.type == 0:
                self.type = 1
            else:
                self.type = 0

            self.animation_counter = 0