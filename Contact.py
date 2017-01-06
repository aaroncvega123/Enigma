


class Contact(object):
    """
    Represents a contact point on an enigma wheel
    """
    
    def __init__(self, ent, ex):
        self.ent = ent
        self.ex = ex
        
    def turn(self):
        """
        Represents the changing of a contact point as a wheel turns
        """
        self.ent = self.ent + 1
        self.ex = self.ex + 1
        if(self.ent > 94):
            self.ent = 0
        if(self.ex > 94):
            self.ex = 0
    
    def getEntrance(self):
        ret = self.ent
        return ret
        
    def getExit(self):
        ret = self.ex
        return ret