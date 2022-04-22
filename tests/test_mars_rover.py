import unittest

from parameterized import parameterized
from mars_rover import RoverControl, MarsRover, RoverCommandFactory


class TestKata(unittest.TestCase):
    
    def build_rover_control(self) -> RoverControl:
        mars_rover = MarsRover()
        return RoverControl(mars_rover, RoverCommandFactory(mars_rover))

    @parameterized.expand([
        ["", "0:0:N", ],
        ["M", "0:1:N", ],
        ["MM", "0:2:N", ],
        ["MMM", "0:3:N", ],
        ["MMMMMMMMMM", "0:0:N", ],
    ])
    def test_given_a_mars_rover_when_executing_a_move_command_should_move(self, command, expected):
        rover_control = self.build_rover_control()
        state = rover_control.execute(command)
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
        rover_control = self.build_rover_control()
        state = rover_control.execute(rotate_right_command)
        self.assertEqual(expected, state)

    @parameterized.expand([
        ["L", "0:0:W", ],
        ["LL", "0:0:S", ],
        ["LLL", "0:0:E", ],
        ["LLLL", "0:0:N", ],
        ["LLLLL", "0:0:W", ],
    ])
    def test_given_a_mars_rover_when_executing_a_left_rotate_command_should_rotate(self, rotate_left_command, expected):
        rover_control = self.build_rover_control()
        state = rover_control.execute(rotate_left_command)
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
        rover_control = self.build_rover_control()
        state = rover_control.execute(mixed_rotate_command)
        self.assertEqual(expected, state)

    @parameterized.expand([
        ["Ñ", ],
        ["?", ],
        ["c", ],
        ["v", ],
    ])
    def test_given_a_mars_rover_when_executing_a_unknown_command_should_rise_an_exception(self, unknown_command):
        rover_control =  self.build_rover_control()
        with self.assertRaises(ValueError) as context:
            rover_control.execute(unknown_command)

        self.assertTrue('is not a valid' in str(context.exception))
        self.assertTrue(unknown_command in str(context.exception))

    @parameterized.expand([
        ["MMMMMMMMMMMMMMMMMMM", "0:19:N", ],
        ["MMMMMMMMMMMMMMMMMMMM", "0:0:N", ],
    ])
    def test_given_a_mars_rover_with_a_20_x_1_plateau_when_executing_a_mixed_rotate_command_should_rotate(self,
            long_command,
            expected):
        plateau_mars_rover = MarsRover(20, 1)                                                                                                  
        rover_control = RoverControl(plateau_mars_rover, RoverCommandFactory(plateau_mars_rover))
        state = rover_control.execute(long_command)
        self.assertEqual(expected, state)

    @parameterized.expand([
        ["LM", "9:0:W", ],
        ["LMM", "8:0:W", ],
    ])
    def test_given_a_mars_rover_with_a_20_x_1_plateau_when_executing_a_mixed_rotate_command_should_rotate(self,
                                                                                                          long_command,
                                                                                                          expected):
        plateau_mars_rover = MarsRover()
        rover_control = RoverControl(plateau_mars_rover, RoverCommandFactory(plateau_mars_rover))
        state = rover_control.execute(long_command)
        self.assertEqual(expected, state)

    @parameterized.expand([
        ["RM", "1:0:E", ],
        ["RMMMMMMMMMMMMMMMMMMMM", "0:0:E", ],
    ])
    def test_given_a_mars_rover_with_a_1_x_20_plateau_when_executing_a_mixed_rotate_command_should_rotate(self,
            long_command,
            expected):
        plateau_mars_rover = MarsRover(20, 20)
        rover_control = RoverControl(plateau_mars_rover, RoverCommandFactory(plateau_mars_rover))
        state = rover_control.execute(long_command)
        self.assertEqual(expected, state)

if __name__ == '__main__':
    unittest.main()
