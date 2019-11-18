# создать добавление карты по количеству клеток
# add events to build rails
# add information about the game (money, etc)
import random
import pygame
import sys
from settings import *
from resources import *
from sprites import *
import os
from math import sqrt


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        # pygame.display.set_mode((600, 400), pygame.FULLSCREEN|pygame.HWSURFACE)

    def load_data(self):
        pass

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pygame.sprite.Group()

        #Textures(self, 0, 0, city)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        
        while self.playing:
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            # self.runTrain(n)
            self.draw_texture(trainR, 4, 4)
            pygame.display.update()    

    def runTrain(self, x):

        self.draw_texture(trainUp, x, 4)

    def quit(self):
        pygame.display.quit()
        pygame.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw_texture(self, name, x, y):
        self.screen.blit(name, (x*TILESIZE, y*TILESIZE))

    def draw(self):
        self.screen.fill(FOREST_GREEN)

        for i in range(len(city_place[1])):
            self.draw_texture(city_arr[int(sqrt(i))],
                              city_place[0][i], city_place[1][i])

        for i in range(len(mountain_place[1])):
            self.draw_texture(
                mountain, mountain_place[0][i], mountain_place[1][i])

        for i in range(len(water_place[1])):
            self.draw_texture(water, water_place[0][i], water_place[1][i])

        for i in range(len(sand_place[1])):
            self.draw_texture(sand, sand_place[0][i], sand_place[1][i])

        for i in range(len(railV_place[1])):
            self.draw_texture(
                rail_vertical, railV_place[0][i], railV_place[1][i])
        for i in range(len(railH_place[1])):
            self.draw_texture(
                rail_horizontal, railH_place[0][i], railH_place[1][i])
        for i in range(len(railC_place[1])):
            self.draw_texture(rail_cross, railC_place[0][i], railC_place[1][i])

        self.draw_grid()

        pygame.display.flip()

    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()


if __name__ == "__main__":
    g = Game()

    while True:
        g.new()
        g.run()
