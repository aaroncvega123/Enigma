#from WheelSet import WheelSet
from Wheel import Wheel
#from Rotor import Rotor
from Reflector import Reflector
#from Contact import Contact

class WheelSet(object):
    
    def __init__(self, seedString):
        self.wheelSet = []
        self.turnsPerWheel = [0] * len(seedString)
        self.ASCIInumbers = range(32, 127)
        incrementer = 10
        for i in range(len(seedString) - 1):
            wheelSeed = ord(seedString[i]) + incrementer
            self.wheelSet.append(Wheel(wheelSeed))
            incrementer += 1
        self.wheelSet.append(Reflector(ord(seedString[len(seedString) - 1])))

    def encryptString(self, inputString):
        ret = ""
        for i in range(len(inputString)):
            ret += self.encryptChar(inputString[i])
        return ret
        
    def encryptChar(self, inputChar):
        ascii = ord(inputChar)
        index = 0
        if ascii >= 32 and ascii < 127:
            for i in range(95):
                if ascii == self.ASCIInumbers[i]:
                    index = i
                    break
            self.fullRotate()
            index = self.descend(self.ascend(index))
            inputChar = str(unichr(self.ASCIInumbers[index]))
        else:
            self.fullRotate()
        return inputChar
            
            
    def descend(self, integer):
        output = integer
        for i in range(len(self.wheelSet)):
            for k in range(len(self.wheelSet[i].wheelPaths)):
                if output == self.wheelSet[i].wheelPaths[k].getEntrance():
                    output = self.wheelSet[i].wheelPaths[k].getExit()
                    break
        return output
        
    def ascend(self, integer):
        output = integer
        for i in range(len(self.wheelSet) - 2).reverse():
            for k in range(len(self.wheelSet[i].wheelPaths)):
                if output == self.wheelSet[i].wheelPaths[k].getEntrance():
                    output = self.wheelSet[i].wheelPaths[k].getExit()
                    break
        return output

    def getWheelSet(self):
        ret = self.wheelSet[:]
        return ret

    def fullRotate(self):
        for i in range(len(self.turnsPerWheel)):
            if self.turnsPerWheel[i] < 94:
                self.rotateOne(i)
                self.turnsPerWheel[i] += 1
                break
            else:
                self.rotate(i)
                self.turnsPerWheel[i] = 0
    
    def rotateOne(self, index):
        for i in range(len(self.wheelSet[index].wheelPaths)):
            self.wheelSet[index].wheelPaths[i].turn()
    
    def printWheelSet(self):
        for i in range(len(self.wheelSet)):
            self.wheelSet[i].printWheel()
