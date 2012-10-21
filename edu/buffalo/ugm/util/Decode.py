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
        
        nNodes = len(edgeStruct.nodes)
        
        #lets apply permutation to first n(nodes) columns and list all possible values
        #assuming states will be numbers starting from zero to stated value. FIXME: we should not live on these assumptions
        self.enumerateAll(0, len(edgeStruct.nodes) - 1, [3], edgeStruct.nStates)
        
        #multiply the state with their nodePotentials
        for k in range(rows):
            for j in range(len(edgeStruct.nodes)):
                self.table[k][nNodes + j] = nodePot[j][self.table[k][j]]
                
        #get the edge potentials
        for k in range(rows):
            for p in range(edgeStruct.nEdges):
                edgeEnds = edgeStruct.edges[p]
                endOne = self.table[k][edgeEnds[0]]
                endTwo = self.table[k][edgeEnds[1]]
                #print " edgePot:" + str(edgePot[p][endOne][endTwo])
                self.table[k][2*nNodes + p] = edgePot[p][endOne][endTwo]
                
        #compute product of potentials
        for k in range(rows):
            prod = 1
            for p in range(nNodes + edgeStruct.nEdges):
                prod = prod*self.table[k][nNodes + p]
            self.table[k][cols-2] = prod
            
        #decoding outputs most optimal parameters
        #max = self.table[][col-2]
        #for k in range(rows):
            
        
        print str(self.table)
      
    '''
    Recursive function to enlist all set of possibilities for given input
    @param cNode: current node (starts with zero), assuming they are in increasing order
    @param tNode: total nodes, enumeration starts with cNode and runs till it has been incremented to tNode
    @param vArray: records all the assignments during that backtrack from root to leaf node
    @param tState: total number of states. Again it starts with zero and runs till currState<tState. incrementing by one each time   
    '''    
    def enumerateAll(self, cNode, tNode, vArray, tState):
        for i in range(tState):
            #print "cNode:" + str(cNode) + " i:" + str(i)
            if cNode == 0: #if this is first node - reinitialize the array - not so necessary though
                vArray = [0 for x in range(tNode + 1)]
            vArray[cNode]=i
            if cNode < tNode: #if we are not at the last dude, keep diving inside
                self.enumerateAll(cNode+1,tNode, vArray, tState)
            else:
                for j in range(tNode + 1):
                    self.table[self.cRow][j] = vArray[j]
                self.cRow = self.cRow+1
                
        
            
        
        