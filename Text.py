import Settings
from pygame import font, time
from pygame.sprite import Sprite

class Text(Sprite):
    def __init__(self, textFont, size, message, color, xpos, ypos, steady = False):
        Sprite.__init__(self)
        self.font = font.Font(textFont, size)
        self.surface = self.font.render(message, True, color)
        self.rect = self.surface.get_rect(topleft=(xpos, ypos))
        self.timer = time.get_ticks()
        self.steady = steady

    def draw(self, surface):
        surface.blit(self.surface, self.rect)

    def update(self, current_time, *args):
        if not self.steady:
            passed = current_time - self.timer
            if passed <= 200 or 400 < passed <= 600:
                self.draw(Settings.SCREEN)
            elif 600 < passed:
                self.kill()
        else:
            passed = current_time - self.timer
            self.draw(Settings.SCREEN)
            if 5000 < passed:
                self.kill()

class steadyText(Sprite):
    def __init__(self, textFont, size, message, color, xpos, ypos):
        Sprite.__init__(self)
        self.font = font.Font(textFont, size)
        self.surface = self.font.render(message, True, color)
        self.rect = self.surface.get_rect(topleft=(xpos, ypos))
        self.timer = time.get_ticks()

    def update(self):
        Settings.SCREEN.blit(self.surface, self.rect)
