from enum import Enum


class UIComponent:

    def __init__(self, pythos, name, id, uiobject, is_color=False, is_animation=False, hover=False, select=False, activate=False, constant=False, animation_time=0.0):
        self.pythos = pythos
        self.name = name
        self.id = id
        self.uiobject = uiobject
        self.is_color = is_color
        self.is_animation = is_animation
        self.hover = hover
        self.select = select
        self.activate = activate
        self.constant = constant
        self.constant_flip = False
        self.hovered = False
        self.selected = False
        self.activated = False

        # 1 = Main, 2 = Secondary, 3 = Border
        self.color_to_change = 1

        self.original_main_color = self.uiobject.main_color
        self.original_secondary_color = self.uiobject.secondary_color
        self.original_border_color = self.uiobject.border_color

        self.current_main_color = self.uiobject.main_color
        self.current_secondary_color = self.uiobject.secondary_color
        self.current_border_color = self.uiobject.border_color

        # Set Up Options
        self.color = None
        self.animation = None

        # Animation
        self.animation_time = animation_time
        self.animation_frames = (self.animation_time * self.pythos.target_fps)

    def getID(self):
        return self.id

    def setColor(self, color):
        self.color = color

    def setAnimation(self, animation):
        self.animation = animation

    def tick(self, dt, target_fps):
        self.hovered = self.uiobject.hovered
        self.selected = self.uiobject.selected
        self.activated = self.uiobject.activated

class UIAnimationType(Enum):

    COLOR_CHANGE = 1
    MOVE_X = 2
    MOVE_Y = 3
    CHANGE_WIDTH = 4
    CHANGE_HEIGHT = 5
