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
        self.rect = (self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.centered_text = False

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
        if self.secondary_color:
            surf.fill(self.secondary_color, self.rect)
        if not self.string == '':
            # TODO: Render Characters Individually to Add More Color/Animation Options
            text_rect, text = self.font.render(self.string, self.main_color)
            x_dif = 0
            y_dif = 0
            if self.centered_text:
                text_rect_size = self.font.get_rect(self.string)
                x_dif = text_rect_size[2] - self.width
                y_dif = text_rect_size[3] - self.height
            surf.blit(text_rect, ((self.rect[0] - offset[0]) - (x_dif / 2), (self.rect[1] - offset[1]) - (y_dif / 2), self.rect[2], self.rect[3]))
            # self.font.render_to(surf, ((self.pos[0] - offset[0]), self.pos[1] - offset[0]), self.string, self.main_color)

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

    def updateSize(self):
        self.size = (self.width, self.height)
        self.updateRect()

    def updateRect(self):
        self.rect = (self.pos[0], self.pos[1], self.size[0], self.size[1])


class UIType(Enum):

    TEXT = 0
    BUTTON = 1
    TOGGLE_BUTTON = 2
    INPUT = 3
    SLIDER = 4
