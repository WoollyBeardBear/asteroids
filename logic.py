import pygame

class Logic():
    def __init__(self, score, lives):
        self.score = 0
        self.lives = 3

    def add_score(self, s):
        self.score += s

    def die(self):
        self.lives -= 1
    
