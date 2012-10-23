'''
Created on Oct 22, 2012

@author: bhatt

'''

import numpy
import random
from random import uniform

class ProcessingUtil(object):
    
    #counter for current row during recursion
    cRow = 0

    def __init__(self):
        '''
        '''
        
        
    def createTable(self,nodePot, edgePot, edgeStruct):
        #number of rows = (numberOfVariables)^(nStates)
        rows = len(edgeStruct.nodes)**(edgeStruct.nStates)
        #number of columns = 2*(numberOfVariables) + nEdges + 2 (for prodpot and probability)
        cols = 2*(len(edgeStruct.nodes)) + edgeStruct.nEdges + 2
        print " " + str(len(edgeStruct.nodes)) + " " + str((edgeStruct.nStates))
        print "rows: " + str(rows) + " cols: " + str(cols)
        table = numpy.zeros((rows, cols))
        
        nNodes = len(edgeStruct.nodes)
        
        #lets apply permutation to first n(nodes) columns and list all possible values
        #assuming states will be numbers starting from zero to stated value. FIXME: we should not live on these assumptions
        self.enumerateAll(0, len(edgeStruct.nodes) - 1, [3], edgeStruct.nStates, table)
        
        #multiply the state with their nodePotentials
        for k in range(rows):
            for j in range(len(edgeStruct.nodes)):
                table[k][nNodes + j] = nodePot[j][table[k][j]]
                
        #get the edge potentials
        for k in range(rows):
            for p in range(edgeStruct.nEdges):
                edgeEnds = edgeStruct.edges[p]
                endOne = table[k][edgeEnds[0]]
                endTwo = table[k][edgeEnds[1]]
                #print " edgePot:" + str(edgePot[p][endOne][endTwo])
                table[k][2*nNodes + p] = edgePot[p][endOne][endTwo]
                
        #compute product of potentials
        for k in range(rows):
            prod = 1
            for p in range(nNodes + edgeStruct.nEdges):
                prod = prod*table[k][nNodes + p]
            table[k][cols-2] = prod
            
        #computing Z
        z = 0
        for k in range(rows):
            z = z + table[k][cols-2]
        
        #computing probability of each
        for k in range(rows):
            table[k][cols-1] = table[k][cols-2]/z
        
        return table
    
    '''
    Recursive function to enlist all set of possibilities for given input
    @param cNode: current node (starts with zero), assuming they are in increasing order
    @param tNode: total nodes, enumeration starts with cNode and runs till it has been incremented to tNode
    @param vArray: records all the assignments during that backtrack from root to leaf node
    @param tState: total number of states. Again it starts with zero and runs till currState<tState. incrementing by one each time   
    '''    
    def enumerateAll(self, cNode, tNode, vArray, tState, table):
        for i in range(tState):
            #print "cNode:" + str(cNode) + " i:" + str(i)
            if cNode == 0: #if this is first node - reinitialize the array - not so necessary though
                vArray = [0 for x in range(tNode + 1)]
            vArray[cNode]=i
            if cNode < tNode: #if we are not at the last dude, keep diving inside
                self.enumerateAll(cNode+1,tNode, vArray, tState, table)
            else:
                for j in range(tNode + 1):
                    table[self.cRow][j] = vArray[j]
                self.cRow = self.cRow+1
    
    '''
    creates nSamples number between a and b. uniformly distributed
    '''            
    def uniformDistribution(self,a,b,nSamples):
        step = (b-a)/float(nSamples) #casting one to float
        distr = numpy.zeros(nSamples)
        pointA = a
        pointB = a+step
        print "step: " + str(step)
        for i in range(nSamples):
            distr[i] = uniform(pointA,pointB)
            pointA = pointB
            pointB = pointA+step
        return distr
       
    
    
        