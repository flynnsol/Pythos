import os
import sys
import pygame

class Utils:

    def __init__(self, pythos, data_path):
        self.pythos = pythos
        self.data_path = data_path
        self.data = {}

    def load_image(self, path, colorkey):
        img = pygame.image.load(path).convert()
        if not colorkey == '':
            img.set_colorkey(colorkey)
        return img

    def load_images(self, path, colorkey):
        images = []
        for img_name in sorted(os.listdir(path)):
            images.append(self.load_image(path + '/' + img_name, colorkey))
        return images

    def load_data(self, path, colorkey):
        try:
            previous_dir = ''
            count = 0
            for file_or_dir in sorted(os.listdir(path)):
                if '.' in file_or_dir:
                    full_path = path + '/' + file_or_dir
                    sp = full_path.split('/')
                    if '.png' in (sp[(len(sp) - 1)]):
                        current_dir = sp[(len(sp) - 2)]
                        if current_dir == previous_dir:
                            self.data[current_dir + str(count)] = self.load_image(full_path, colorkey)
                        else:
                            count = 0
                            self.data[current_dir + str(count)] = self.load_image(full_path, colorkey)
                        count += 1
                        previous_dir = current_dir
                    elif '.json' in (sp[(len(sp) - 1)]): # TODO: Load Maps
                        current_dir = sp[(len(sp) - 2)]
                        if current_dir == previous_dir:
                            self.data[current_dir + str(count)] = full_path
                        else:
                            count = 0
                            self.data[current_dir + str(count)] = full_path
                        count += 1
                        previous_dir = current_dir

                        # TODO: Add Custom Font Support

                        # TODO: Add modding support
                else:
                    self.load_data(path + '/' + file_or_dir, colorkey)
        except FileNotFoundError:
            print("Directory Not Found")

        return self.data

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def convert_velocity(self, velocity):
        new_velocity = velocity * self.pythos.dt * self.pythos.target_fps
        return new_velocity


class Colors:

    def __init__(self, pythos):
        self.pythos = pythos

    def BLACK(): return (0, 0, 0)

    def WHITE(): return (255, 255, 255)

    def RED(): return (255, 0, 0)

    def GREEN(): return (0, 255, 0)

    def BLUE(): return (0, 0, 255)
