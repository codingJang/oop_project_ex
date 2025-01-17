import pygame

__all__ = ['Button', 'make_button']


class Button(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height, text='', num=0):
        super().__init__()
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.num = num

    def draw(self, screen, outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.Font('Teko-Medium.ttf', 40)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def mouse(self, pos):
        if (pos[0] > self.x) and (pos[0] < self.x + self.width):
            if (pos[1] > self.y) and (pos[1] < self.y + self.height):
                return True

        return False


def make_button(screen, sprites, pic=None):
    run = True
    while run:
        events = pygame.event.get()

        if pic is not None:
            ss = pygame.image.load(pic)
            screen.blit(ss, (0, 0))

        for i in sprites:
            i.draw(screen, (0, 0, 0))

        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in sprites:
                    if i.mouse(pos):
                        return i.num
            if event.type == pygame.MOUSEMOTION:
                for i in sprites:
                    if i.mouse(pos):
                        i.color = (255, 0, 0)
                    else:
                        i.color = (0, 255, 0)

        pygame.display.update()
