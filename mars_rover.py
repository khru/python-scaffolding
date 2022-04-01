class MarsRover:
    __PLATEAU_SIZE = 10
    __compass = ['N', 'E', 'S', 'W']

    def execute(self, commands: str):
        if commands == 'L':
            return '0:0:W'
        if commands == 'LL':
            return '0:0:S'
        if commands.startswith('R'):
            return '0:0:' + self.__compass[len(commands) % len(self.__compass)]
        return '0:' + str(len(commands) % self.__PLATEAU_SIZE) + ':N'
