from ui.uicomponent import UIComponent, UIAnimationType

class UIChangeWidth(UIComponent):

    def __init__(self, pythos, id, uiobject, width, is_animation=False, hover=False, select=False, activate=False, constant=False, animation_time=0.0):
        super().__init__(pythos, 'change_width', id, uiobject, False, is_animation, hover, select, activate, constant, animation_time)
        self.width = width
        self.width_difference = self.findDifference()
        self.width_additive = 0

        self.animation = UIAnimationType.CHANGE_WIDTH

    def tick(self, dt, target_fps):
        if self.is_animation:
            if self.animation_frames > 0:
                self.width_additive = self.width_difference / self.animation_frames * dt * target_fps
            if self.hover:
                self.changeWidthTime(self.uiobject.hovered)
            if self.select:
                self.changeWidthTime(self.uiobject.selected)
            if self.activate:
                self.changeWidthTime(self.uiobject.activated)
            if self.constant:
                self.changeWidthTime(not self.constant_flip)
        else:
            if self.hover:
                self.changeWidth(self.uiobject.hovered)
            if self.select:
                self.changeWidth(self.uiobject.selected)
            if self.activate:
                self.changeWidth(self.uiobject.activated)
        super().tick(dt, target_fps)

    def changeWidth(self, boolean):
        if boolean:
            self.uiobject.width = self.width
            self.uiobject.updateSize()
        else:
            self.uiobject.width = self.original_width
            self.uiobject.updateSize()

    def changeWidthTime(self, boolean):
        if boolean:
            if abs(self.uiobject.width - self.width) >= 0:
                newWidth = self.uiobject.width - self.width_additive
                if newWidth < self.width and self.width_additive > 0:
                    newWidth = self.width
                elif newWidth > self.width and self.width_additive < 0:
                    newWidth = self.width
                self.uiobject.width = newWidth
                self.uiobject.updateSize()
        else:
            if abs(self.uiobject.width - self.original_width) >= 0:
                newWidth = self.uiobject.width + self.width_additive
                if newWidth > self.original_width and self.width_additive > 0:
                    newWidth = self.original_width
                elif newWidth < self.original_width and self.width_additive < 0:
                    newWidth = self.original_width
                self.uiobject.width = newWidth
                self.uiobject.updateSize()

    def findDifference(self):
        return  self.uiobject.width - self.width