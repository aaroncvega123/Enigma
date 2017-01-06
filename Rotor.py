

class Rotor( object ):
    
    def __init__(self):
        self.wheelPaths = []
        self.toBeUsed = []
        
        for i in range(94):
            self.toBeUsed.append(i)

    def generateExits(self, seed):
        place = seed
        exits = []
        while len(self.toBeUsed) > 0:
            if place < len(self.toBeUsed):
                exits.append(self.toBeUsed[place])
                self.toBeUsed.pop(place)
                place = place + seed
            elif place >= len(self.toBeUsed):
                place = place - len(self.toBeUsed)
        return exits[:]
        
    def printWheel(self):
        for i in range(len(self.wheelPaths)):
            print(self.wheelPaths[i].getEntrance() + " ")
        for i in range(len(self.wheelPaths)):
            print(self.wheelPaths[i].getExit() + " ")
        print("\n")

    def getToBeUsd(self):
        ret = self.toBeUsed[:]
        return ret
        