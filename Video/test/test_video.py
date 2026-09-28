import unittest
from video import Video


class TestVideo(unittest.TestCase):
    def test_that_the_play_button_prints_video_is_playing(self):
        test_video = Video("Avengers: Doomsday", 3.15, 0)

        self.assertEqual("Now playing, Avengers: Doomsday", test_video.play())  # add assertion here


if __name__ == '__main__':
    unittest.main()
