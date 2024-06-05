from ui.uicomponent import UIComponent, UIAnimationType

class UIMoveX(UIComponent):

    def __init__(self, pythos, id, uiobject, pos, is_animation=False, hover=False, select=False, activate=False, constant=False, animation_time=0.0):
        super().__init__(pythos, 'move_x', id, uiobject, False, is_animation, hover, select, activate, constant, animation_time)
        self.pos = pos
        self.x_difference = self.findDifference()
        self.x_additive = 0

        self.animation = UIAnimationType.MOVE_X

    def tick(self, dt, target_fps):
        if self.is_animation:
            if self.animation_frames > 0:
                self.x_additive = self.x_difference / self.animation_frames * dt * target_fps
            if self.hover:
                self.moveXTime(self.uiobject.hovered)
            if self.select:
                self.moveXTime(self.uiobject.selected)
            if self.activate:
                self.moveXTime(self.uiobject.activated)
            if self.constant:
                self.moveXTime(not self.constant_flip)
        else:
            if self.hover:
                self.moveX(self.uiobject.hovered)
            if self.select:
                self.movex(self.uiobject.selected)
            if self.activate:
                self.moveX(self.uiobject.activated)
        super().tick(dt, target_fps)

    def moveX(self, boolean):
        if boolean:
            self.uiobject.pos = self.pos
        else:
            self.uiobject.pos = self.original_pos

    def moveXTime(self, boolean):
        if boolean:
            if abs(self.uiobject.pos[0] - self.pos[0]) >= 0:
                newX = self.uiobject.pos[0] - self.x_additive
                if newX < self.pos[0] and self.x_additive > 0:
                    newX = self.pos[0]
                elif newX > self.pos[0] and self.x_additive < 0:
                    newX = self.pos[0]
                self.uiobject.pos = (newX, self.uiobject.pos[1])
        else:
            if abs(self.uiobject.pos[0] - self.original_pos[0]) >= 0:
                newX = self.uiobject.pos[0] + self.x_additive
                if newX > self.original_pos[0] and self.x_additive > 0:
                    newX = self.original_pos[0]
                elif newX < self.original_pos[0] and self.x_additive < 0:
                    newX = self.original_pos[0]
                self.uiobject.pos = (newX, self.uiobject.pos[1])

    def findDifference(self):
        return  self.uiobject.pos[0] - self.pos[0]