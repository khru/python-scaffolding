import unittest

from parameterized import parameterized
from mars_rover import MarsRover


class TestKata(unittest.TestCase):
    @parameterized.expand([
        ["", "0:0:N", ],
        ["M", "0:1:N", ],
        ["MM", "0:2:N", ],
        ["MMM", "0:3:N", ],
        ["MMMMMMMMMM", "0:0:N", ],
    ])
    def test_given_a_mars_rover_when_executing_a_move_command_should_move(self, command, expected):
        rover = MarsRover()
        state = rover.execute(command)
        self.assertEqual(expected, state)

    @parameterized.expand([
        ["R", "0:0:E", ],
        ["RR", "0:0:S", ],
        ["RRR", "0:0:W", ],
        ["RRRR", "0:0:N", ],
    ])
    def test_given_a_mars_rover_when_executing_a_right_rotate_command_should_rotate(self, rotate_right_command, expected):
        rover = MarsRover()
        state = rover.execute(rotate_right_command)
        self.assertEqual(expected, state)

    @parameterized.expand([
        ["L", "0:0:W", ],
        ["LL", "0:0:S", ],
    ])
    def test_given_a_mars_rover_when_executing_a_left_rotate_command_should_rotate(self, rotate_left_command, expected):
        rover = MarsRover()
        state = rover.execute(rotate_left_command)
        self.assertEqual(expected, state)

if __name__ == '__main__':
    unittest.main()
