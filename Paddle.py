import pygame

Black = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):

    # Paddle sprite

    def __init__(self, color, width, height):
        # Call constructor from parent class
        super().__init__()

        # Color, position and location
        self.image = pygame.Surface([width, height])
        self.image.fill(Black)
        self.image.set_colorkey(Black)

        # paddle draw
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        # paddle fetch
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # check left boundary
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # check right boundary
        if self.rect.x > 700:
            self.rect.x = 700
