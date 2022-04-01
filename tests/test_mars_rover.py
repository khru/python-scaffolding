import unittest
from mars_rover import MarsRover


class TestKata(unittest.TestCase):

    def test_fresh_mars_rover_does_not_move_on_empty_command(self):
        rover = MarsRover()
        state = rover.execute('')
        self.assertEqual('0:0:N', state)


if __name__ == '__main__':
    unittest.main()
