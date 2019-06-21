

from ..toolkit.umbrella_bot import UmbrellaBot


class Manipulator(object):
    def __init__(self):
        self.identifier=[]
        self.dict_th = {}
    
    def stop(self,identifier):
        xd= self.dict_th[identifier]
        xd._delete()

    def add_identifier(self,identifier):
        self.identifier.append(identifier)
    
    def add_thread(self,UmbrellaBot,identifier):
        result = self.checkExistenceIdentifier(identifier)
        if result == True:
            print("Identifier Exists in manipulator.")
        else:
            for i in self.identifier:    
                if i == identifier:   
                    self.dict_th[identifier] = UmbrellaBot
                    print("Thread Add")
    
    def checkExistenceIdentifier(self,identifier):
        cont = 0
        for i in range(len(self.identifier)):
            if identifier[i] == identifier:
                cont+=1
            if cont>=2:
                break
                return True
                
        return False
        
