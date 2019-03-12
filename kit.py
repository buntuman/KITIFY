'''
@uthor DANIEL GITAHI
@recomended enviroment - python 3.5 and above
The python code contined defines the properties of a kit object.
'''
from component import Component

class Kit:
    # number of kits
    kits = 0

    def __init__(self, name, component=None):
        self.name = name
        self.components = list()  # the number of components in this kit
        Kit.kitCount()

    @classmethod
    def kitCount(cls):
        cls.kits += 1

    def addComponent(self, component):
        self.components.append(component)

    def getKitName(self):
        return self.name

    def __str__(self):
        data=""
        for component in self.components:
            data+="\n"+str(component)
        return data

    def __len__(self):
        return len(self.components)

    ''' 
    This collects all the model numbers in the kit and returns it as a list
    '''
    def modelSignature(self):
      pass

    def fullKit(self,ModelList):
        pass


    def __eq__(self, other):
        if len(self) != len(other):
            return False
        return self.modelSignature() == other.modelSignature()
