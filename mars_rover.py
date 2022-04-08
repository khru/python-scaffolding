from enum import Enum


class _Compass:
    __compass = ['N', 'E', 'S', 'W']

    def __init__(self):
        self.__orientation = 0

    def rotate_right(self):
        self.__orientation = (self.__orientation + 1) % len(self.__compass)

    def rotate_left(self):
        self.__orientation = (self.__orientation - 1) % len(self.__compass)

    def orientation(self):
        return self.__compass[self.__orientation]


class Command(Enum):
    RIGHT: str = 'R'


class CommandList:
    commands: list[Command]

    def __create_command(self, command: str, mars_rover):
        if command == 'M':
            return Move(mars_rover)
        if command == 'L':
            return RotateLeft(mars_rover)
        return Command(command)

    def __init__(self, commands: str, mars_rover):
        self.commands = [self.__create_command(command, mars_rover) for command in commands]

    def get_all_commands(self) -> list[Command]:
        return self.commands


class MarsRover:

    def __init__(self, plateau_column_size: int = 10, plateau_row_size: int = 10):
        self.__compass = _Compass()
        self.__column: int = 0
        self.__column_increment: int = 1
        self.__row: int = 0
        self.__row_increment: int = 0
        self.__plateau_column_size = plateau_column_size
        self.__plateau_row_size = plateau_row_size

    def move(self):
        self.__column = ((self.__column + self.__column_increment) % self.__plateau_column_size)
        self.__row = ((self.__row + self.__row_increment) % self.__plateau_row_size)

    def __rotate_right(self):
        self.__compass.rotate_right()
        self.__column_increment = 0
        self.__row_increment = 1

    def rotate_left(self):
        self.__compass.rotate_left()

    def execute(self, commands: str):
        # commands_list: list[Command] = [Command(command) for command in commands]
        for command in CommandList(commands, self).get_all_commands():
            if isinstance(command, Move) or isinstance(command, RotateLeft):
                command()
            if command == Command.RIGHT:
                self.__rotate_right()
        return str(self.__row) + ':' + str(self.__column) + ':' + self.__compass.orientation()


class Move:
    def __init__(self, mars_rover: MarsRover):
        self.__mars_rover = mars_rover

    def __call__(self):
        self.__mars_rover.move()


class RotateLeft:
    def __init__(self, mars_rover: MarsRover):
        self.__mars_rover = mars_rover

    def __call__(self):
        self.__mars_rover.rotate_left()
