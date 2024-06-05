from ui.uiobject import UIObject, UIType

class UIButton(UIObject):

    def __init__(self, string, pos, width, height, font):
        super().__init__(pos, UIType.BUTTON, string=string, font=font)
        self.width = width
        self.height = height
        self.centered_text = True
        self.updateSize()

    def tick(self, dt, target_fps):
        super().tick(dt, target_fps)

    def render(self, surf, offset=(0, 0)):
        super().render(surf, offset)
