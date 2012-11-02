'''
Created on Nov 2, 2012

@author: bhatt
'''

class ChainDecode(object):
    '''
    classdocs
    '''
    
    alpha = []
    kappa = []
    maxState = []


    def __init__(self):
        '''
        Constructor
        '''
    def __str__(self):
        return "[[alpha:" + str(self.alpha) +  "], [kappa:" + str(self.kappa) + "],, [maxState:" + str(self.maxState) + "]]"
            