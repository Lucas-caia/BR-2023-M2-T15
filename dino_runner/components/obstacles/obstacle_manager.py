import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.obstacle_types = [Cactus, Bird, LargeCactus]

    def update(self, game):
        if len(self.obstacles) == 0:
            self.add_obstacle()

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(200)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def add_obstacle(self):
        obstacle_type = random.choice(self.obstacle_types)
        if obstacle_type == Cactus:
            obstacle = Cactus(SMALL_CACTUS)
        elif obstacle_type == Bird:
            obstacle = Bird(BIRD)
        elif obstacle_type == LargeCactus:
            obstacle = LargeCactus(LARGE_CACTUS)

        self.obstacles.append(obstacle)