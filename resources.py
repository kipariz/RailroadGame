import pygame
import os
from settings import *

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path
city_path = os.path.join(image_path, 'city')

trainR = pygame.image.load(os.path.join(image_path, 'train.png'))
trainR = pygame.transform.scale(trainR, (TILESIZE-5, (TILESIZE-3)*2))
trainUp = pygame.transform.rotate(trainR, 90)
trainL = pygame.transform.rotate(trainR, 180)
trainD = pygame.transform.rotate(trainR, 270)

rail_vertical = pygame.image.load(os.path.join(image_path, 'rail.png'))
rail_vertical = pygame.transform.scale(rail_vertical, (TILESIZE, TILESIZE))

rail_horizontal = pygame.image.load(os.path.join(image_path, 'rail1.png'))
rail_horizontal = pygame.transform.scale(rail_horizontal, (TILESIZE, TILESIZE))

rail_cross = pygame.image.load(os.path.join(image_path, 'rail2.png'))
rail_cross = pygame.transform.scale(rail_cross, (TILESIZE, TILESIZE))

water = pygame.image.load(os.path.join(image_path, 'water.png'))
water = pygame.transform.scale(water, (TILESIZE, TILESIZE))

sand = pygame.image.load(os.path.join(image_path, 'sand.png'))
sand = pygame.transform.scale(sand, (TILESIZE, TILESIZE))

mountain = pygame.image.load(os.path.join(image_path, 'mountain.png'))
mountain = pygame.transform.scale(mountain, (TILESIZE, TILESIZE))

house1 = pygame.image.load(os.path.join(city_path, 'house1.png'))
house1 = pygame.transform.scale(house1, (TILESIZE, TILESIZE))

house2 = pygame.image.load(os.path.join(city_path, 'house2.png'))
house2 = pygame.transform.scale(house2, (TILESIZE, TILESIZE))

house3 = pygame.image.load(os.path.join(city_path, 'house3.png'))
house3 = pygame.transform.scale(house3, (TILESIZE, TILESIZE))

house4 = pygame.image.load(os.path.join(city_path, 'house4.png'))
house4 = pygame.transform.scale(house4, (TILESIZE, TILESIZE))

house5 = pygame.image.load(os.path.join(city_path, 'house5.png'))
house5 = pygame.transform.scale(house5, (TILESIZE, TILESIZE))

house6 = pygame.image.load(os.path.join(city_path, 'house6.png'))
house6 = pygame.transform.scale(house6, (TILESIZE, TILESIZE))

city_arr=[house1,house2,house3,house4,house5,house6]