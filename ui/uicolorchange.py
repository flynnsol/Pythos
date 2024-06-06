from ui.uicomponent import UIComponent, UIAnimationType

class UIColorChange(UIComponent):

    def __init__(self, pythos, id, uiobject, is_animation, color, color_to_change, hover=False, select=False, activate=False, constant=False, animation_time=0.0):
        super().__init__(pythos, 'color_change', id, uiobject, True, is_animation, hover, select, activate, constant, animation_time)
        self.color = color
        self.color_to_change = color_to_change
        self.red_difference = 0
        self.green_difference = 0
        self.blue_difference = 0

        self.animation = UIAnimationType.COLOR_CHANGE

        self.findColorDifference()
        self.red_additive = 0
        self.green_additive = 0
        self.blue_additive = 0

    def tick(self, dt, target_fps):
        if self.is_animation:
            if self.animation_frames > 0:
                self.red_additive = self.red_difference / self.animation_frames * dt * target_fps
                self.green_additive = self.green_difference / self.animation_frames * dt * target_fps
                self.blue_additive = self.blue_difference / self.animation_frames * dt * target_fps
            if self.hover:
                if not self.uiobject.selected:
                    self.changeColor(self.uiobject.hovered)
            if self.activate:
                self.changeColor(self.uiobject.activated)
            if self.select:
                self.changeColor(self.uiobject.selected)
            if self.constant:
                self.changeColor(not self.constant_flip)
        else:
            if self.hovered != self.uiobject.hovered and not self.uiobject.selected:
                if self.hover:
                    self.changeColor(self.uiobject.hovered)

            if self.activated != self.uiobject.activated:
                if self.activate:
                    self.changeColor(self.uiobject.activated)

            if self.selected != self.uiobject.selected:
                self.changeColor(self.uiobject.hovered)
                self.changeColor(self.uiobject.activated)
                if self.select:
                    self.changeColor(self.uiobject.selected)
        super().tick(dt, target_fps)

    def changeColor(self, boolean):
        if self.color_to_change == 1:
            self.changeMainColorBoolean(boolean)
        if self.color_to_change == 2:
            self.changeSecondaryColorBoolean(boolean)
        if self.color_to_change == 3:
            self.changeBorderColorBoolean(boolean)

    def changeMainColorBoolean(self, boolean):
        if not self.is_animation:
            if boolean:
                self.uiobject.main_color = self.color
            else:
                self.uiobject.main_color = self.original_main_color
        else:
            if boolean:
                if abs(self.uiobject.main_color[0] - self.color[0]) >= abs(self.red_additive) or abs(self.uiobject.main_color[1] - self.color[1]) >= abs(self.green_additive) or abs(self.uiobject.main_color[2] - self.color[2]) >= abs(self.blue_additive):
                    new_color = self.uiobject.main_color
                    new_colorRGB = self.changeColorTime(new_color, True)
                    if not self.constant_flip:
                        if self.color == new_colorRGB:
                            self.constant_flip = True
                    self.uiobject.main_color = new_colorRGB
            else:
                if abs(self.uiobject.main_color[0] - self.original_main_color[0]) >= abs(self.red_additive) or abs(self.uiobject.main_color[1] - self.original_main_color[1]) >= abs(self.green_additive) or abs(self.uiobject.main_color[2] - self.original_main_color[2]) >= abs(self.blue_additive):
                    new_color = self.uiobject.main_color
                    new_colorRGB = self.changeColorTime(new_color, False)
                    if self.constant_flip:
                        if self.original_main_color == new_colorRGB:
                            self.constant_flip = False
                    self.uiobject.main_color = new_colorRGB

    def changeSecondaryColorBoolean(self, boolean):
        if not self.is_animation:
            if boolean:
                self.uiobject.secondary_color = self.color
            else:
                self.uiobject.secondary_color = self.original_secondary_color
        else:
            if boolean:
                if abs(self.uiobject.secondary_color[0] - self.color[0]) >= abs(self.red_additive) or abs(self.uiobject.secondary_color[1] - self.color[1]) >= abs(self.green_additive) or abs(self.uiobject.secondary_color[2] - self.color[2]) >= abs(self.blue_additive):
                    new_color = self.uiobject.secondary_color
                    new_colorRGB = self.changeColorTime(new_color, True)
                    if not self.constant_flip:
                        if self.color == new_colorRGB:
                            self.constant_flip = True
                    self.uiobject.secondary_color = new_colorRGB
            else:
                if abs(self.uiobject.secondary_color[0] - self.original_secondary_color[0]) >= abs(self.red_additive) or abs(self.uiobject.secondary_color[1] - self.original_secondary_color[1]) >= abs(self.green_additive) or abs(self.uiobject.secondary_color[2] - self.original_secondary_color[2]) >= abs(self.blue_additive):
                    new_color = self.uiobject.secondary_color
                    new_colorRGB = self.changeColorTime(new_color, False)
                    if self.constant_flip:
                        if self.original_main_color == new_colorRGB:
                            self.constant_flip = False
                    self.uiobject.secondary_color = new_colorRGB

    def changeBorderColorBoolean(self, boolean):
        if not self.is_animation:
            if boolean:
                self.uiobject.border_color = self.color
            else:
                self.uiobject.border_color = self.original_border_color
        else:
            if boolean:
                if abs(self.uiobject.border_color[0] - self.color[0]) >= abs(self.red_additive) or abs(self.uiobject.border_color[1] - self.color[1]) >= abs(self.green_additive) or abs(self.uiobject.border_color[2] - self.color[2]) >= abs(self.blue_additive):
                    new_color = self.uiobject.border_color
                    new_colorRGB = self.changeColorTime(new_color, True)
                    if not self.constant_flip:
                        if self.color == new_colorRGB:
                            self.constant_flip = True
                    self.uiobject.border_color = new_colorRGB
            else:
                if abs(self.uiobject.border_color[0] - self.original_border_color[0]) >= abs(self.red_additive) or abs(self.uiobject.border_color[1] - self.original_border_color[1]) >= abs(self.green_additive) or abs(self.uiobject.border_color[2] - self.original_border_color[2]) >= abs(self.blue_additive):
                    new_color = self.uiobject.border_color
                    new_colorRGB = self.changeColorTime(new_color, False)
                    if self.constant_flip:
                        if self.original_border_color == new_colorRGB:
                            self.constant_flip = False
                    self.uiobject.border_color = new_colorRGB

    def changeColorTime(self, color, positive):
        if positive:
            r = color[0] + self.red_additive
            g = color[1] + self.green_additive
            b = color[2] + self.blue_additive
        else:
            r = color[0] - self.red_additive
            g = color[1] - self.green_additive
            b = color[2] - self.blue_additive

        if r > 255:
            r = 255
        elif r < 0:
            r = 0

        if g > 255:
            g = 255
        elif g < 0:
            g = 0

        if b > 255:
            b = 255
        elif b < 0:
            b = 0

        new_color = (r, g, b)
        return new_color

    def findColorDifference(self):
        if self.color_to_change == 1:
            if self.original_main_color is not None:
                self.red_difference = self.color[0] - self.original_main_color[0]
                self.green_difference = self.color[1] - self.original_main_color[1]
                self.blue_difference = self.color[2] - self.original_main_color[2]
        if self.color_to_change == 2:
            if self.original_secondary_color is not None:
                self.red_difference = self.color[0] - self.original_secondary_color[0]
                self.green_difference = self.color[1] - self.original_secondary_color[1]
                self.blue_difference = self.color[2] - self.original_secondary_color[2]
        if self.color_to_change == 3:
            if self.original_border_color is not None:
                self.red_difference = self.color[0] - self.original_border_color[0]
                self.green_difference = self.color[1] - self.original_border_color[1]
                self.blue_difference = self.color[2] - self.original_border_color[2]