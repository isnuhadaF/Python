
class Video():
    def __init__(self, title: str, duration: float, playback_position: float):
        self.title = title
        self.duration = duration
        self.playback_position = 0

    def play(self):
        return f"Now playing, {self.title}"

    def advance(self, minutes):
        if minutes < self.time_remaining():
            self.playback_position += minutes
        else:
            pass

    def is_finished(self):
        if self.playback_position == self.duration:
            return True
        else:
            return False

    def restart(self):
        self.playback_position = 0

    def time_remaining(self):
        return f"{(self.duration - self.playback_position) * 60} minutes remaining."