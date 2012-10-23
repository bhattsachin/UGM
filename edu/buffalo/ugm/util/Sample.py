'''
Created on Oct 19, 2012

@author: bhatt
'''
import numpy
from edu.buffalo.ugm.util import ProcessingUtil

class Sample(object):
    '''
    sampling related functions
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def exact(self, nodePot, edgePot, edgeStruct, nSamples):
        #number of rows = (numberOfVariables)^(nStates)
        rows = len(edgeStruct.nodes)**(edgeStruct.nStates)
        #number of columns = 2*(numberOfVariables) + nEdges + 2 (for prodpot and probability)
        cols = 2*(len(edgeStruct.nodes)) + edgeStruct.nEdges + 2
        util = ProcessingUtil.ProcessingUtil()
        table = util.createTable(nodePot, edgePot, edgeStruct)
        nNodes = len(edgeStruct.nodes)
        
        #creating nSample points between 0 and 1
        distr = util.uniformDistribution(0, 1, nSamples)
        
        samples = numpy.zeros((nSamples, nNodes))
        for i in range(nSamples):
            cf = 0
            for k in range(rows):
                cf = cf + table[k][cols-1]
                if cf > distr[i]:
                    for j in range(nNodes):
                        samples[i][j] = table[k][j] 
                    break
            #print " cf: " + str(cf) + " distr[i]:" + str(distr[i])
               
        
        #print "samples: " + str(samples)
        return samples
        
        
        