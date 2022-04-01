class MarsRover:
    __PLATEAU_SIZE = 10
    __compass = ['N', 'E', 'S', 'W']
    def execute(self, commands: str):
        if commands.startswith('R'):
            return '0:0:' + self.__compass[len(commands)]
        return '0:' + str(len(commands) % self.__PLATEAU_SIZE) + ':N'
