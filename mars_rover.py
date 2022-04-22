from abc import ABC, abstractmethod
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


class Rover(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def rotate_right(self):
        pass

    @abstractmethod
    def rotate_left(self):
        pass

    @abstractmethod
    def print_status(self):
        pass


class MarsRover(Rover):

    __COS90 = 0
    __SIN90 = 1

    def __init__(self, plateau_column_size: int = 10, plateau_row_size: int = 10):
        self.__compass = _Compass()
        self.__column: int = 0
        self.__row: int = 0
        self.__row_increment: int = self.__COS90
        self.__column_increment: int = self.__SIN90
        self.__plateau_column_size = plateau_column_size
        self.__plateau_row_size = plateau_row_size

    def move(self):
        self.__column = ((self.__column + self.__column_increment) % self.__plateau_column_size)
        self.__row = ((self.__row + self.__row_increment) % self.__plateau_row_size)

    def rotate_right(self):
        self.__compass.rotate_right()
        self.__row_increment = self.__COS90 * self.__row_increment + self.__SIN90 * self.__column_increment
        self.__column_increment = -self.__SIN90 * self.__row_increment + self.__COS90 * self.__column_increment

    def rotate_left(self):
        self.__compass.rotate_left()
        self.__row_increment = -1
        self.__column_increment = 0

    def print_status(self) -> str:
        return str(self.__row) + ':' + str(self.__column) + ':' + self.__compass.orientation()

    # def execute(self, commands: str) -> str:
    #    mars_rover_control = MarsRoverControl(self)
    #    mars_rover_control.execute(commands)
    #    return self.print_status()


class Command(ABC):

    @abstractmethod
    def __call__(self):
        pass


class Move(Command):
    def __init__(self, rover: Rover):
        self.__mars_rover = rover

    def __call__(self):
        self.__mars_rover.move()


class RotateLeft(Command):
    def __init__(self, rover: Rover):
        self.__mars_rover = rover

    def __call__(self):
        self.__mars_rover.rotate_left()


class RotateRight(Command):
    def __init__(self, rover: Rover):
        self.__mars_rover = rover

    def __call__(self):
        self.__mars_rover.rotate_right()


class CommandSymbol(Enum):
    MOVE = 'M'
    LEFT = 'L'
    RIGHT = 'R'


class RoverCommandFactory:

    def __init__(self, rover: Rover):
        self.__rover = rover

    def __call__(self, command: CommandSymbol) -> Command:
        if command == CommandSymbol.MOVE:
            return Move(self.__rover)
        if command == CommandSymbol.LEFT:
            return RotateLeft(self.__rover)
        return RotateRight(self.__rover)


class RoverControl:

    def __init__(self, rover: Rover, rover_command_factory: RoverCommandFactory):
        self.__rover = rover
        self.__rover_command_factory = rover_command_factory

    def execute(self, commands) -> str:
        [self.__rover_command_factory(CommandSymbol(command))() for command in commands]
        return self.__rover.print_status()
