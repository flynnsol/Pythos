

class UIPanel:

    def __init__(self, pythos, pos, width, height):
        self.pythos = pythos
        self.pos = pos
        self.width = width
        self.height = height
        self.size = (self.width, self.height)
        self.id = 0

        self.uiobjects = []

    def addUIObject(self, uiobject):
        self.uiobjects.append(uiobject)

    def removeUIObject(self, uiobject):
        self.uiobjects.remove(uiobject)

    def tick(self, dt, target_fps):
        for uiobject in self.uiobjects:
            uiobject.tick(dt, target_fps)

    def render(self, surf, offset=(0, 0)):
        for uiobject in self.uiobjects:
            uiobject.render(surf, offset)

    def eventHandler(self, event):
        for uiobject in self.uiobjects:
            uiobject.eventHandler(event)
