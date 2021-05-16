"""This code is copyright free (CC0), but please credit useage."""

import pygame
pygame.init()
screen = pygame.display.set_mode((750, 500))

img = pygame.image.load('')

class Sprite:
    def __init__(self, pos, img):
        """Made by https://github.com/CT7-labs, CC0 license."""
        self.rect = pygame.Rect(pos)
        self.img = img
        self.imgAngle = 0
        self.angle = 0
    def rotate(self, d):
        self.angle -= d
    def rotateImg(self, d):
        self.imgAngle -= d
    def changeImg(self, newImg):
        self.img = newImg
    def move(self, x, y):
        self.rect = self.rect.move(x, y)
    def forward(self, speed, x=0):
        moveVector = pygame.math.Vector2(x, -speed).rotate(-self.angle)
        self.rect = self.rect.move(moveVector)
    def draw(self):
        newImg = pygame.transform.rotate(self.img, self.angle + self.imgAngle)
        newRect = newImg.get_rect()
        newRect.center = self.rect.center
        screen.blit(newImg, newRect)
    def collide(self, sprite):
        return self.rect.colliderect(sprite.rect)
