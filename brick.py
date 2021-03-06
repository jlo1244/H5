import pygame

Black = (0, 0, 0)
# brick block


class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(Black)
        self.image.set_colorkey(Black)

        # draw brick
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
