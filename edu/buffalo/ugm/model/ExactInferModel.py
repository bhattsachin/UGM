'''
Created on Oct 22, 2012

@author: bhatt
'''

class ExactInferModel(object):
    '''
    Holds variables returned after running inference on the input
    '''
    
    
    nodeBel = []
    edgeBel = []
    logZ = 0
    
    


    def __init__(self):
        '''
        Constructor
        '''
    def __str__(self):
        return "[[nodeBel:" + str(self.nodeBel) +  "], [logZ:" + str(self.logZ) + "]]"
        