

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
        for i in self.identifier:    
            if i == identifier:   
                self.dict_th[identifier] = UmbrellaBot
                print("Thread Add")
        
