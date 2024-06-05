import pygame
import pygame.freetype
import time
import sys
from camera.camera import Camera

from utils.utils import Utils, Colors
from ui.menu.menu import Menu

class Pythos:

    def __init__(self, title, data_path, colorkey=(0, 0, 0), fps=60, target_fps=60, resolution=(640, 480), scale=1, logo='', font='', font_size=24):
        pygame.init()

        self.title = title
        self.data_path = data_path
        self.colorkey = colorkey
        self.fps = fps
        self.target_fps = target_fps
        self.resolution = resolution
        self.logo = logo
        self.scale = scale
        self.font = font
        self.font_size = font_size
        self.dt = 0
        self.camera = Camera(self, (0, 0))
        self.utils = Utils(self, self.data_path)

        if not self.font == '':
            pass # TODO: Add custom fonts
        else:
            self.font = pygame.freetype.SysFont('freesans', self.font_size)

        self.screen = pygame.display.set_mode(self.resolution)
        self.display = pygame.Surface((self.resolution[0] // self.scale, self.resolution[1] // self.scale))

        # Menus
        self.menus = []

        # Update to Sort into an Array
        self.data = {}
        self.data = self.utils.load_data(self.data_path, self.colorkey)

        pygame.display.set_caption(self.title)
        if not self.logo == '':
            # Load Logo With Utils
            pass
        self.clock = pygame.time.Clock()
        self.running = True

    def changeFontSize(self, size):
        self.font.size = size

    def addMenu(self, menu):
        self.menus.append(menu)

    def removeMenu(self, menu):
        self.menus.remove(menu)

    def run(self):
        # INITIALIZE DELTA TIME
        prev_time = time.time()
        self.dt = 0
        fps = self.fps

        # MAIN LOOP
        while self.running:
            # Limit Framerate
            self.clock.tick(fps)

            # Compute Delta Time
            now = time.time()
            self.dt = now - prev_time
            prev_time = now

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.utils.quit_game()
                self.eventHandler(event)

            # Tick (Update Method)
            self.tick(self.dt, self.target_fps)

            # Render (Render Method)
            self.render(self.display, offset=(int(self.camera.pos[0]), int(self.camera.pos[1])))

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()

    def tick(self, dt, target_fps):
        self.camera.tick(dt, target_fps)
        for menu in self.menus:
            menu.tick(dt, target_fps)

    def render(self, surf, offset=(0, 0)):
        surf.fill((0, 0, 0))
        for menu in self.menus:
            menu.render(surf, offset)

    def eventHandler(self, event):
        for menu in self.menus:
            menu.eventHandler(event)
