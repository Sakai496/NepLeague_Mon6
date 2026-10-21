# main.py
from pathlib import Path
import sys
import pygame

# 画面初期化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame-ce Team Project")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()