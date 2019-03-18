'''
@Author : Daniel Gitahi
This document comtains the definition of an identity object.
The Identity object is an object that defines and or brands a components ensemble

'''

class Identity:
    #This method accepts a  finite number of model-count pairs(dictionary)
    def __init__(self,composition):
        self.composition=dict()
        self.name = composition["name"]
        del composition["name"]
        self.composition = composition

    def __str__(self):
        data = "====="+ str(self.name) + "=====\n"
        for key in self.composition.keys():
            data += str(key) +" : "+ str(self.composition[key])+"\n"
        return data

    def __len__(self):
        size = 0
        for key in self.composition.keys():
            size += self.composition[key]
        return size

    def __eq__(self, other):
        return ((self.name == other.name) and (self.composition == other.composition))