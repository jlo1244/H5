import pygame
from random import randint
Black = (0, 0, 0,)


class Ball(pygame.sprite.Sprite):
    # ball sprite

    def __init__(self, color, width, height):
        # call sprite constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(Black)
        self.image.set_colorkey(Black)

        # draw ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]
        if self.velocity[1] == 0:
            self.velocity[1] = randint(-8, 8)

        # fetch ball
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
        if self.velocity[1] == 0:
            self.velocity[1] = randint(-8, 8)


class Shot(Ball):
    # Shot
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
        self.velocity = [0, -4]
        self.image = pygame.Surface([width, height])
        self.image.fill(Black)
        self.image.set_colorkey(Black)

        # draw shot
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # fetch shot
        self.rect = self.image.get_rect()
