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

if __name__ == '__main__':
    unittest.main()
