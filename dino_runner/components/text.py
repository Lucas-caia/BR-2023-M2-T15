import pygame

FONT_STYLE = 'freesansbold.ttf'


class Text:
    def __init__(self):
        self.font = pygame.font.Font(FONT_STYLE, 22)

    def render_text(self, text, color, center_pos, screen):
        rendered_text = self.font.render(text, True, color)
        text_rect = rendered_text.get_rect()
        text_rect.center = center_pos
        screen.blit(rendered_text, text_rect)
