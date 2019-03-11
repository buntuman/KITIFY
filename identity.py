'''
@Author : Daniel Gitahi
This document comtains the definition of an identity object.
The Identity object is an object that defines and or brands a components ensemble

'''

class Identity:
    #This method accepts a  finite number of model-count pairs(dictionary)
    def __init__(self,name,compositions):
        self.name = name
        self.compositions = compositions

    def __str__(self):
        len
        data = "====="+ str(self.name) + "=====\n"
        for key in self.compositions.keys():
            data += str(key) +" : "+ str(self.compositions[key])+"\n"
        return data

    def __len__(self):
        return self.length