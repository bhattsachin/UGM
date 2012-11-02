'''
Created on Oct 18, 2012

@author: bhatt
'''
from edu.buffalo.ugm.util import ProcessingUtil
from edu.buffalo.ugm.model import ChainDecode
import numpy


class Decode(object):
    '''
    Contains all decoding functions
    '''
    #table = []
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
    returns 
    '''    
    def exact(self, nodePot, edgePot, edgeStruct):
        #number of rows = (numberOfVariables)^(nStates)
        rows = len(edgeStruct.nodes)**(edgeStruct.nStates)
        #number of columns = 2*(numberOfVariables) + nEdges + 2 (for prodpot and probability)
        cols = 2*(len(edgeStruct.nodes)) + edgeStruct.nEdges + 2
        util = ProcessingUtil.ProcessingUtil()
        table = util.createTable(nodePot, edgePot, edgeStruct)
        nNodes = len(edgeStruct.nodes)
        
        
        #decoding outputs most optimal parameters
        #max = self.table[][col-2]
        #for k in range(rows):
        vMax = 0 #assuming we will always have positive potentials
        iMax = 0
        
        for k in range(rows):
            if vMax < table[k][cols-2]:
                vMax = table[k][cols-2]
                iMax = k
            
        
        print str(table)
        print "optimum values: " + str(vMax) + " " + str(iMax)
        exactOptimalDecode = []
        for k in range(nNodes):
            exactOptimalDecode.append(table[iMax][k])
            #print " " + str(self.table[iMax][k])
        print str(exactOptimalDecode)
        #print str("optimum values: " + str(self.table[iMax][0] + " , " + str(self.table[iMax][1] + " , " + str(self.table[iMax][0]))
        return exactOptimalDecode
    
    '''
    Chain decoding
    uses Viterbi algorithm
    algo given in http://en.wikipedia.org/wiki/Viterbi_algorithm
    involves emmision matrix and observation, which i don't see in this example
    and hence following the way it is in UGM
    '''
    def chain(self, nodePot, edgePot, edgeStruct):
        nNodes = len(edgeStruct.nodes) #size of node
        
        nStates = edgeStruct.numberOfStates #assuming all have same possible states
        maximize = 1 #maximize and sum are two options.
        print "nstates is:" + str(nStates)
        util = ProcessingUtil.ProcessingUtil()
        #forward phase
        chainDecode = util.chainFwd(nodePot, edgePot, nStates,nNodes, maximize) 
        
        #backward phase
        nodeLabels = [i for i in range(nNodes)]
        #setting the last one
        nodeLabels[nNodes-1] = chainDecode.alpha[nNodes-1].argmax(axis=0)
        for i in xrange(nNodes-2,-1,-1): #reverse for loop xrange(last, first-1, step)
            nodeLabels[i] = chainDecode.maxState[i+1][nodeLabels[i+1]]
        return nodeLabels
        
        
      
    