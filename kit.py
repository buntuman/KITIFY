'''
@uthor DANIEL GITAHI
@recomended enviroment - python 3.5 and above
The python code contined defines the properties of a kit object.
'''
from component import Component
from identity import Identity
import ast

class Kit:
    # number of kits
    kits = 0
    identities=list()

    def __init__(self, name, component=None):
        self.name = name
        self.components = list()  # the number of components in this kit

        Kit.kitCount()
    @classmethod
    def setIdentities(cls,identities):
        cls.identities = identities


    #procedure to load identities from either a file or any external data source
    @classmethod
    def loadIdentities(cls,file=None):
        if file != None:
            try:
                infile = open(file,"r")
                for line in infile:
                    line = ast.literal_eval(line)
                    cls.identities.append(Identity(line))
            except:
                print("Unable to open file")
                return False

    @classmethod
    def kitCount(cls):
        cls.kits += 1

    def addComponent(self, component):
        self.components.append(component)

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

