

class Menu:

    def __init__(self, pythos, panel, active):
        self.pythos = pythos
        self.panel = panel
        self.active = active

    def tick(self, dt, target_fps):
        self.panel.tick(dt, target_fps)

    def render(self, surf, offset=(0, 0)):
        self.panel.render(surf, offset)

    def eventHandler(self, event):
        self.panel.eventHandler(event)
