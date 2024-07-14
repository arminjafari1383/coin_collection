import pygame
import random


pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("بازی سکه ومانع")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
dark_gray = (40,40,40)
Light_gray = (120,120,120)

player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 10

obstacle_width = 100
obstacle_height = 20
obstacle_x = random.randint(0,screen_width)
obstacle_y = screen_height - player_height - 10
obstacle_speed = 10