'''
Created on Oct 18, 2012

@author: bhatt
'''
from edu.buffalo.ugm.util import ProcessingUtil
from edu.buffalo.ugm.model import ExactInferModel
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
                
        marginal = marginal/z
        print " marginal: " + str(marginal)
        print " logZ: " + str(math.log(z))
        
        inferModel = ExactInferModel.ExactInferModel()
        inferModel.nodeBel = marginal
        inferModel.logZ = math.log(z)
        #I don't really understand why we need edge marginals right now and hence deferring implementation
                    
        return inferModel 
    
    
    def chain(self, nodePot, edgePot, edgeStruct):
        nNodes = len(edgeStruct.nodes) #size of node
        nStates = edgeStruct.numberOfStates #assuming all have same possible states
        maximize = 0
        util = ProcessingUtil.ProcessingUtil()
        maxStates = edgeStruct.nStates
        #forward pass
        chainDecode =  util.chainFwd(nodePot, edgePot, nStates,nNodes, maximize) 
        
        #backward phase
        beta = numpy.zeros((nNodes,edgeStruct.nStates))
        beta[nNodes-1][range(0,nStates[nNodes-1])] = 1
        
        for i in xrange(nNodes-2, -1, -1):
            first = numpy.tile(nodePot[i+1][range(0,nStates[i+1])],(nStates[i],1))
            second = edgePot[i][range(0,nStates[i+1])][range(0,nStates[i])]
            print "first:  " + str(first)
            print "second: " + str(second)
            tmp = first*second
            print "tmp: " + str(tmp)
            tmp2 = numpy.tile(beta[i+1][range(0,nStates[i+1])], (nStates[i],1))
            betatmp = tmp*tmp2
            betatmp = numpy.sum(betatmp,axis=1)
            
            beta[i][range(0,nStates[i])] = betatmp.transpose()
            #Normalizing
            beta[i][range(0,nStates[i])] = beta[i][range(0,nStates[i])]/numpy.sum(beta[i][range(0,nStates[i])])
        print "something: " + str(beta)
        print "alpha:" + str(chainDecode.alpha)
        
        #node beliefs
        nodeBel = numpy.zeros((nodePot.shape[0], nodePot.shape[1]))
        for i in range(nNodes):
            #print "first: " + str(chainDecode.alpha[i][range(0,nStates[i])])
            #print "second: " + str(beta[i][range(0,nStates[i])])
            tmp = (chainDecode.alpha[i][range(0,nStates[i])])*(beta[i][range(0,nStates[i])])
            nodeBel[i][range(0,nStates[i])]= tmp/(numpy.sum(tmp))
            print "sum tmp: " + str(numpy.sum(tmp))
            print "tmp: " + str(tmp)
        
        #Edge beliefs
        edgeBel = numpy.zeros((edgePot.shape[0],edgePot.shape[1],edgePot.shape[2]))
        
        for i in xrange(nNodes-1):
            tmp = numpy.zeros((maxStates, maxStates))
            for j in xrange(nStates[i]):
                for k in xrange(nStates[i+1]):
                    tmp[j][k] = chainDecode.alpha[i][j]*nodePot[i+1][k]*beta[i+1][k]*edgePot[i][j][k]
                    
            edgeBel[i] = tmp/numpy.sum(tmp)
            #print "edgeBel: " + str(edgeBel)
        
        
        print "nodeBel: " + str(nodeBel)
        print "edgeBel: " + str(edgeBel)
        
        
        
        