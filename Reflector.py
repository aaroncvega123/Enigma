
from Rotor import Rotor
#from Reflector import Reflector
from Contact import Contact

class Reflector( Rotor ):
    
    def __init__(self, seed):
        Rotor.__init__(self)
        self.exits = self.generateExits(seed)
        self.entrances = self.generateEntrances(self.exits)
        for i in range(len(self.exits)):
            self.wheelPaths.append(Contact(self.entrances[i], self.exits[i]))

    def generateEntrances(self, exits):
        entrances = []
        i = 0
        while(i < 93):
            entrances.append(exits[i + 1])
            entrances.append(exits[i])
            i += 1
        return entrances