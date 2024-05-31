from pythos import Pythos
from utils.utils import Colors
from ui.menu.menu import Menu
from ui.uipanel import UIPanel
from ui.uitext import UIText
from ui.uicolorchange import UIColorChange

class Test(Pythos):

    def __init__(self):
        super().__init__('Sidescroller', './data')

        self.addMenu(Menu(self, UIPanel(self, (0, 0), self.resolution[0], self.resolution[1]), True))
        test_string = UIText((50, 50), 'Test String', self.font)
        test_string.secondary_color = Colors.BLACK()
        self.menus[0].panel.addUIObject(test_string)
        test_string.addComponent(UIColorChange(self, 0, test_string, True, Colors.RED(), 1, hover=True, animation_time=0.25))
        # test_string.addComponent(UIColorChange(self, 1, test_string, False, Colors.BLUE(), 1, select=True, animation_time=0.25))
        # test_string.addComponent(UIColorChange(self, 2, test_string, True, Colors.WHITE(), 2, hover=True, animation_time=0.25))
        # test_string.addComponent(UIColorChange(self, 3, test_string, True, Colors.GREEN(), 2, select=True, animation_time=0.25))
        self.menus[0].panel.addUIObject(UIText((250, 50), 'John is Lame', self.font))
        self.run()


Test()