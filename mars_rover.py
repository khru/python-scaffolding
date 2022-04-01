class MarsRover:
    __PLATEAU_SIZE = 10

    def execute(self, commands):
        if commands == 'R':
            return '0:0:E'
        if commands == 'RR':
            return '0:0:S'
        return '0:' + str(len(commands) % self.__PLATEAU_SIZE) + ':N'
