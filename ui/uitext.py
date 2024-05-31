from ui.uiobject import UIObject, UIType


class UIText(UIObject):

    def __init__(self, pos, string, font):
        super().__init__(pos, UIType.TEXT, string=string, font=font)

    def tick(self, dt, target_fps):
        super().tick(dt, target_fps)

    def render(self, surf, offset=(0, 0)):
        super().render(surf, offset)
