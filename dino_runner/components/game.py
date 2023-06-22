import pygame

from dino_runner.utils.constants import *
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.text import Text
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.death_count = 0
        self.highscore = 0

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.text_renderer = Text()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.reset_game()
        self.power_up_manager.reset_power_ups()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 3
        if self.score > self.highscore:
                self.highscore = self.score
    
    def reset_game(self):
        self.score = 0
        self.game_speed = 20

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) 
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))

        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0

        self.x_pos_bg -= self.game_speed

        if self.score >= 400:
            self.screen.fill((255, 153, 51))
            
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))

        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0

        if self.score >= 700:
            self.screen.fill((25, 25, 112))
            
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))

        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0

    def draw_score(self):
        score_text = f"Score: {self.score}"
        self.text_renderer.render_text(score_text, (0, 0, 0), (1000, 50), self.screen)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.text_renderer.render_text(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                    (0, 0, 0),
                    (500, 50),
                    self.screen,
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE


    def handle_events_on_meunu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.text_renderer.render_text("Press any key to start", (0, 0, 0), 
            (half_screen_width, half_screen_height), self.screen)
            self.screen.blit(ICON, (half_screen_width - 50, 180))
        else:
            self.text_renderer.render_text("Press any key to restart", 
            (0, 0, 0), (half_screen_width, half_screen_height), self.screen)
            score_text = f"Score: {self.score}"
            self.text_renderer.render_text(score_text, (0, 0, 0), (1000, 50), self.screen)
            death_count_text = f"Death Count: {self.death_count}"
            self.text_renderer.render_text(death_count_text, (0, 0, 0), (1000, 90), self.screen)
            highscore_text = f"Highscore: {self.highscore}"
            self.text_renderer.render_text(highscore_text, (0, 0, 0), (1000, 70), self.screen)
            self.screen.blit(RESTART, (half_screen_width - 40, 180))
            
        
        pygame.display.update()

        self.handle_events_on_meunu()