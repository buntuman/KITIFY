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


