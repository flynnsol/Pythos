

class Camera:
    def __init__(self, pythos, pos, entity_to_track=None, parallax=15):
        self.pythos = pythos
        self.pos = list(pos)
        self.entity_to_track = entity_to_track
        self.parallax = parallax

    def setEntityToTrack(self, entity_to_track):
        self.entity_to_track = entity_to_track

    def setParallax(self, parallax):
        self.parallax = parallax

    def tick(self, dt, target_fps):
        if self.entity_to_track:
            self.pos[0] += ((self.entity_to_track.rect().centerx - self.pythos.display.get_width() / 2 - self.pos[0]) / self.parallax) * dt * target_fps
            self.pos[1] += ((self.entity_to_track.rect().centery - self.pythos.display.get_width() / 2 - self.pos[1]) / self.parallax) * dt * target_fps
