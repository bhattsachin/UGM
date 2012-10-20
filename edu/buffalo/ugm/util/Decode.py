'''
Created on Oct 18, 2012

@author: bhatt
'''
import numpy

class Decode(object):
    '''
    Contains all decoding functions
    '''
    table = []
    #counter for current row during recursion
    cRow = 0

    def __init__(self):
        '''
        Constructor
        '''
    
    
    
    '''
    Exact decoding 
    Enumerates all of them as size is small
    will result in a table with all values
    '''    
    def exact(self, nodePot, edgePot, edgeStruct):
        
        #number of rows = (numberOfVariables)^(nStates)
        rows = len(edgeStruct.nodes)**(edgeStruct.nStates)
        #number of columns = 2*(numberOfVariables) + nEdges + 2 (for prodpot and probability)
        cols = 2*(len(edgeStruct.nodes)) + edgeStruct.nEdges + 2
        print " " + str(len(edgeStruct.nodes)) + " " + str((edgeStruct.nStates))
        print "rows: " + str(rows) + " cols: " + str(cols)
        self.table = numpy.zeros((rows, cols))
        
        
        #lets apply permutation to first n(nodes) columns and list all possible values
        #assuming states will be numbers starting from zero to stated value. FIXME: we should not live on these assumptions
        self.enumerateAll(0, 3, [3], 1)
        
        print str(self.table)
        
    def enumerateAll(self, cNode, tNode, vArray, tState):
        
        for i in range(tState):
            print "cNode:" + str(cNode) + " i:" + str(i)
            if cNode == 0: #if this is first node - reinitialize the array - not so necessary though
                vArray = []
            vArray.append(i)
            if cNode < tNode: #if we are not at the last dude, keep diving inside
                self.enumerateAll(cNode+1,tNode, vArray, tState)
            else:
                for j in range(tNode):
                    self.table[self.cRow][j] = vArray[j]
                self.cRow = self.cRow+1
                #return
        
            
        
        