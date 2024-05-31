from utils.utils import Colors
from enum import Enum
import pygame

class UIObject:

    def __init__(self, pos, type, string='', font=None):
        self.string = string
        self.pos = pos
        self.type = type
        self.font = font
        self.width = 0
        self.height = 0
        text_rect = self.font.get_rect(self.string)
        self.width = text_rect[2]
        self.height = text_rect[3]
        self.size = (self.width, self.height)

        self.main_color = Colors.WHITE()
        self.secondary_color = None
        self.border_color = None

        # Component Set Up

        self.hovered = False
        self.selected = False
        self.activated = False

        self.components = []

    def addComponent(self, component):
        self.components.append(component)

    def removeComponent(self, component):
        self.components.remove(component)

    def render(self, surf, offset=(0, 0)):
        if not self.string == '':
            # TODO: Render Characters Individually to Add More Color/Animation Options
            self.font.render_to(surf, ((self.pos[0] - offset[0]), self.pos[1] - offset[0]), self.string, self.main_color, self.secondary_color)

    def tick(self, dt, target_fps):
        if self.check_mouse_pos():
            if not self.selected:
                self.hovered = True
        else:
            self.hovered = False
        for component in self.components:
            component.tick(dt, target_fps)

    def eventHandler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.check_mouse_pos():
                self.selected = not self.selected
                if self.selected:
                    self.hovered = False
            else:
                self.selected = False

    def activate(self):
        self.hovered = False
        self.selected = False
        self.activated = True

    def deactivate(self):
        self.hovered = False
        self.selected = False
        self.activated = False

    def check_mouse_pos(self):
        if self.pos[0] <= pygame.mouse.get_pos()[0] <= (self.pos[0] + self.width):
            if self.pos[1] <= pygame.mouse.get_pos()[1] <= (self.pos[1] + self.height):
                return True
            return False
        return False


class UIType(Enum):

    TEXT = 0
    BUTTON = 1
    TOGGLE_BUTTON = 2
    INPUT = 3
    SLIDER = 4
