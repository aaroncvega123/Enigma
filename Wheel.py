#from Wheel import Wheel
from Rotor import Rotor as Rotor
#from Reflector import Reflector
from Contact import Contact as Contact

class Wheel( Rotor ):
    
    def __init__(self, seed):
        rtr = Rotor.__init__(self)
        self.exits = rtr.generateExits(seed)
        for i in range(len(self.exits)):
            self.wheelPaths.append(Contact(i, self.exits[i]))

newSet = Wheel(10)
