from ui.uicomponent import UIComponent, UIAnimationType

class UIChangeHeight(UIComponent):

    def __init__(self, pythos, id, uiobject, height, is_animation=False, hover=False, select=False, activate=False, constant=False, animation_time=0.0):
        super().__init__(pythos, 'change_height', id, uiobject, False, is_animation, hover, select, activate, constant, animation_time)
        self.height = height
        self.height_difference = self.findDifference()
        self.height_additive = 0

        self.animation = UIAnimationType.CHANGE_HEIGHT

    def tick(self, dt, target_fps):
        if self.is_animation:
            if self.animation_frames > 0:
                self.height_additive = self.height_difference / self.animation_frames * dt * target_fps
            if self.hover:
                self.changeHeightTime(self.uiobject.hovered)
            if self.select:
                self.changeHeightTime(self.uiobject.selected)
            if self.activate:
                self.changeHeightTime(self.uiobject.activated)
            if self.constant:
                self.changeHeightTime(not self.constant_flip)
        else:
            if self.hover:
                self.changeHeight(self.uiobject.hovered)
            if self.select:
                self.changeHeight(self.uiobject.selected)
            if self.activate:
                self.changeHeight(self.uiobject.activated)
        super().tick(dt, target_fps)

    def changeHeight(self, boolean):
        if boolean:
            self.uiobject.height = self.height
            self.uiobject.updateSize()
        else:
            self.uiobject.height = self.original_height
            self.uiobject.updateSize()

    def changeHeightTime(self, boolean):
        if boolean:
            if abs(self.uiobject.height - self.height) >= 0:
                newHeight = self.uiobject.height - self.height_additive
                if newHeight < self.height and self.height_additive > 0:
                    newHeight = self.height
                elif newHeight > self.height and self.height_additive < 0:
                    newHeight = self.height
                self.uiobject.height = newHeight
                self.uiobject.updateSize()
        else:
            if abs(self.uiobject.height - self.original_height) >= 0:
                newHeight = self.uiobject.height + self.height_additive
                if newHeight > self.original_height and self.height_additive > 0:
                    newHeight = self.original_height
                elif newHeight < self.original_height and self.height_additive < 0:
                    newHeight = self.original_height
                self.uiobject.height = newHeight
                self.uiobject.updateSize()

    def findDifference(self):
        return  self.uiobject.height - self.height