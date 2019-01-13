'''
@uthor DANIEL GITAHI
@recomended enviroment - python 3.5 and above
The python code contined defines the properties of a kit object.
'''


class Kit:
    # number of kits
    kits = 0

    def __init__(self, name, component=None):
        self.name = name
        self.component = dict()  # details about the component. Its a dictionary
        self.components = list()  # the number of components in this kit
        Kit.kitCount()

    @classmethod
    def kitCount(cls):
        cls.kits += 1

    def addComponent(self, model, serial, internal=False, parent_serial=None):
        component = dict()
        component['model'] = model
        component['serial'] = serial
        component['internal'] = internal
        component['parent_serial'] = parent_serial
        self.component = component
        self.components.append(component)

    def getKitName(self):
        return self.name

    def __str__(self):
        data = str(self.name) + "\n"
        compIndx = 0
        components = self.components
        for component in components:
            data += " ->"+str(component['serial'])+"\n"
        return data

    def __len__(self):
        return len(self.components)

    '''
    This collects all the model numbers in the kit and returns it as a list
    '''
    def modelSignature(self):
        modelList = list()
        for component in self.components:
            modelList.append(component['model'])
        return modelList

    def fullKit(self,ModelList):
        pass
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        return self.modelSignature() == other.modelSignature()
