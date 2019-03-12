'''
@Author :Daniel Gitahi
This document contains the definition of a 'component' object.
'''

class Component:
    def __init__(self, serial = None,model = None, parentSerial = None):
        self.serial = serial
        self.model=model
        self.parentSerial = parentSerial

    '''
        This returns true if the component has a parent serial assigned.
        The presence of a parent serial means that the component phycally resides
        inside another component. 
    '''

    def isInternalComponent(self):
        return self.parentSerial == None

    def getModel(self):
        return self.model

    def getSerial(self):
        return self.serial

    def getParent(self):
        return self.parentSerial

    def __repr__(self):
        if not self.isEmpty():
            return str(self.serial)+"\t"+str(self.model)
        else:
            return "Empty Component"

    def __str__(self):
        if not self.isEmpty():
            return str(self.serial)+"\t"+str(self.model)
        else:
            return "Empty Component"

    def isEmpty(self):
        return self.serial == None or self.model == None