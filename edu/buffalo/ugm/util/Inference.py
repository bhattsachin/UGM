'''
Created on Oct 18, 2012

@author: bhatt
'''
from edu.buffalo.ugm.util import ProcessingUtil;
import numpy
import math

class Inference(object):
    '''
    Inference functions
    '''


    def __init__(self):
        '''
        Constructor
        '''
    '''
    find marginals for nodes and all possible states
    '''
    def exact(self, nodePot, edgePot, edgeStruct):
        #number of rows = (numberOfVariables)^(nStates)
        rows = len(edgeStruct.nodes)**(edgeStruct.nStates)
        #number of columns = 2*(numberOfVariables) + nEdges + 2 (for prodpot and probability)
        cols = 2*(len(edgeStruct.nodes)) + edgeStruct.nEdges + 2
        util = ProcessingUtil.ProcessingUtil()
        table = util.createTable(nodePot, edgePot, edgeStruct)
        nNodes = len(edgeStruct.nodes)
        
        #marginal for each state of every node
        marginal = numpy.zeros((nNodes,edgeStruct.nStates)) #nodes by states
        
        #compute Z
        z = 0
        for k in range(rows):
            z = z + table[k][cols-2]
            
        for i in range(nNodes):
            for j in range(edgeStruct.nStates):
                sum = 0
                for k in range(rows): #sum all values
                    if table[k][i]==j: #equals to a particular state
                        sum = sum + table[k][cols-2]
                marginal[i][j] = sum
                
        print " marginal: " + str(marginal)
        marginal = marginal/z
        print " marginal: " + str(marginal)
        print " logZ: " + str(math.log(z))
        
                    
            
        
        
        