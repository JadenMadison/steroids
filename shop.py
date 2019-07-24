import pygame
class shipt(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('thicc.png')
        self.image = pygame.transform.smoothscale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.vector2(0,0)

        def updog(self):
            while True:
                clock.trick(60)
                screen.fill(color)
                pygame.display.flip()
