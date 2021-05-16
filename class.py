"""This code is copyright free (CC0), but please credit useage."""

import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

class Sprite:
    def __init__(self, pos, img):
        """Made by https://github.com/CT7-labs, CC0 license."""
        self.rect = pygame.Rect(pos)
        self.img = img
        self.imgAngle = 0
        self.angle = 0
    def rotate(self, d):
        """Rotates the sprite clockwise - feel free to make it counterclockwise"""
        self.angle -= d
    def rotateImg(self, d):
        """Rotates the image clockwise - feel free to make it counterclockwise"""
        self.imgAngle -= d
    def changeImg(self, newImg):
        """Replaces the image with a new image"""
        self.img = newImg
    def move(self, x, y):
        """Moves the sprite along the X and Y axis"""
        self.rect = self.rect.move(x, y)
    def forward(self, speed, x=0):
        """Moves the sprite forward based on its rotation"""
        moveVector = pygame.math.Vector2(x, -speed).rotate(-self.angle)
        self.rect = self.rect.move(moveVector)
    def draw(self):
        """Draws the sprite"""
        newImg = pygame.transform.rotate(self.img, self.angle + self.imgAngle)
        newRect = newImg.get_rect()
        newRect.center = self.rect.center
        screen.blit(newImg, newRect) # change the name if you'd like
    def collide(self, sprite):
        """Detects collision with another Sprite"""
        return self.rect.colliderect(sprite.rect)
