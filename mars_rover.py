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
    LEFT: str = 'L'
    MOVE: str = 'M'


class CommandList:
    commands: list[Command] = []

    def __init__(self, commands: str):
        self.commands = [Command(command) for command in commands]

    def get_all_commands(self) -> list[Command]:
        return self.commands


class MarsRover:
    __PLATEAU_SIZE = 10
    __COLUMN_INCREMENT: int = 1
    __ROW_INCREMENT: int = 0

    def __init__(self):
        self.__compass = _Compass()
        self.__column: int = 0
        self.__row: int = 0

    def __move(self):
        self.__column = ((self.__column + self.__COLUMN_INCREMENT) % self.__PLATEAU_SIZE)
        self.__row = ((self.__row + self.__ROW_INCREMENT) % self.__PLATEAU_SIZE)

    def __rotate_right(self):
        self.__compass.rotate_right()
        self.__COLUMN_INCREMENT = 0
        self.__ROW_INCREMENT = 1

    def execute(self, commands: str):
        commands_list: list[Command] = [Command(command) for command in commands]
        for command in commands_list:
            if command == Command.MOVE:
                self.__move()
            if command == Command.LEFT:
                self.__compass.rotate_left()
            if command == Command.RIGHT:
                self.__rotate_right()
        return str(self.__row) + ':' + str(self.__column) + ':' + self.__compass.orientation()
