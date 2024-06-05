from ui.uicomponent import UIComponent, UIAnimationType

class UIMoveY(UIComponent):
    
    def __init__(self, pythos, id, uiobject, pos, is_animation=False, hover=False, select=False, activate=False, constant=False, animation_time=0.0):
        super().__init__(pythos, 'move_y', id, uiobject, False, is_animation, hover, select, activate, constant, animation_time)
        self.pos = pos
        self.y_difference = self.findDifference()
        self.y_additive = 0
        
        self.animation = UIAnimationType.MOVE_Y
    
    def tick(self, dt, target_fps):
        if self.is_animation:
            if self.animation_frames > 0:
                self.y_additive = self.y_difference / self.animation_frames * dt * target_fps
            if self.hover:
                self.moveYTIme(self.uiobject.hovered)
            if self.select:
                self.moveYTIme(self.uiobject.selected)
            if self.activate:
                self.moveYTIme(self.uiobject.activated)
            if self.constant:
                self.moveYTIme(not self.constant_flip)
        else:
            if self.hover:
                self.moveY(self.uiobject.hovered)
            if self.select:
                self.moveY(self.uiobject.selected)
            if self.activate:
                self.moveY(self.uiobject.activated)
        super().tick(dt, target_fps)

    def moveY(self, boolean):
        if boolean:
            self.uiobject.pos = self.pos
        else:
            self.uiobject.pos = self.original_pos

    def moveYTIme(self, boolean):
        if boolean:
            if abs(self.uiobject.pos[1] - self.pos[1]) >= 0:
                newY = self.uiobject.pos[1] - self.y_additive
                if newY < self.pos[1] and self.y_additive > 0:
                    newY = self.pos[1]
                elif newY > self.pos[1] and self.y_additive < 0:
                    newY = self.pos[1]
                self.uiobject.pos = (self.uiobject.pos[0], newY)
        else:
            if abs(self.uiobject.pos[1] - self.original_pos[1]) >= 0:
                newY = self.uiobject.pos[1] + self.y_additive
                if newY > self.original_pos[1] and self.y_additive > 0:
                    newY = self.original_pos[1]
                elif newY < self.original_pos[1] and self.y_additive < 0:
                    newY = self.original_pos[1]
                self.uiobject.pos = (self.uiobject.pos[0], newY)

    def findDifference(self):
        return self.uiobject.pos[1] - self.pos[1]