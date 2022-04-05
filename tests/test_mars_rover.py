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
        ["RRRRR", "0:0:E", ],
    ])
    def test_given_a_mars_rover_when_executing_a_right_rotate_command_should_rotate(self, rotate_right_command,
                                                                                    expected):
        rover = MarsRover()
        state = rover.execute(rotate_right_command)
        self.assertEqual(expected, state)

    @parameterized.expand([
        ["L", "0:0:W", ],
        ["LL", "0:0:S", ],
        ["LLL", "0:0:E", ],
        ["LLLL", "0:0:N", ],
        ["LLLLL", "0:0:W", ],
    ])
    def test_given_a_mars_rover_when_executing_a_left_rotate_command_should_rotate(self, rotate_left_command, expected):
        rover = MarsRover()
        state = rover.execute(rotate_left_command)
        self.assertEqual(expected, state)

    @parameterized.expand([
        ["LR", "0:0:N", ],
        ["RL", "0:0:N", ],
        ["LRR", "0:0:E", ],
        ["RLL", "0:0:W", ],
        ["LLR", "0:0:W", ],
        ["RRL", "0:0:E", ],
        ["RLLL", "0:0:S", ],
        ["LRRR", "0:0:S", ],
    ])
    def test_given_a_mars_rover_when_executing_a_mixed_rotate_command_should_rotate(self, mixed_rotate_command,
                                                                                    expected):
        rover = MarsRover()
        state = rover.execute(mixed_rotate_command)
        self.assertEqual(expected, state)

    @parameterized.expand([
        ["Ñ", ],
        ["?", ],
        ["c", ],
        ["v", ],
    ])
    def test_given_a_mars_rover_when_executing_a_unknown_command_should_rise_an_exception(self, unknown_command):
        rover = MarsRover()
        with self.assertRaises(ValueError) as context:
            rover.execute(unknown_command)

        self.assertTrue('is not a valid' in str(context.exception))
        self.assertTrue(unknown_command in str(context.exception))

    @parameterized.expand([
        ["MMMMMMMMMMMMMMMMMMM", "0:19:N", ],
        ["MMMMMMMMMMMMMMMMMMMM", "0:0:N", ],
    ])
    def test_given_a_mars_rover_with_a_20_x_1_plateau_when_executing_a_mixed_rotate_command_should_rotate(self,
                                                                                                           long_command,
                                                                                                           expected):
        rover = MarsRover(20, 1)
        state = rover.execute(long_command)
        self.assertEqual(expected, state)

    @parameterized.expand([
        ["RMMMMMMMMMMMMMMMMMMM", "19:0:E", ],
        ["RMMMMMMMMMMMMMMMMMMMM", "0:0:E", ],
    ])
    def test_given_a_mars_rover_with_a_1_x_20_plateau_when_executing_a_mixed_rotate_command_should_rotate(self,
                                                                                                           long_command,
                                                                                                           expected):
        rover = MarsRover(1, 20)
        state = rover.execute(long_command)
        self.assertEqual(expected, state)

if __name__ == '__main__':
    unittest.main()
