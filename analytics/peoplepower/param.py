'''
param
Created on June 25, 2013
@author: Arun Varma
'''


class Param(object):
    '''
    __init__
    defines a Parameter object with a name, index, multiplier, and value
    @param name: String
    @param index: String (optional - will be set to None if not specified)
    @param multiplier: String or enum
    @param value: String or int
    '''
    def __init__(self, name, value, index = None, units = None, multiplier = None):
        self.name = name
        self.value = value
        self.index = index
        self.units = None
        self.multiplier = multiplier

    '''
    getName
    @return the name of this parameter
    '''
    def getName(self):
        return self.name

    '''
    getIndex
    @return the index of this parameter
    '''
    def getIndex(self):
        return self.index

    '''
    getMult
    @return the multiplier of this parameter
    '''
    def getMult(self):
        return self.multiplier

    '''
    getVal
    @return the value of this parameter
    '''
    def getVal(self):
        return self.value

    '''
    setVal
    resets the value of the this parameter to the given newVal
    @param newVal: String or int
    '''
    def setVal(self, newVal):
        self.value = newVal