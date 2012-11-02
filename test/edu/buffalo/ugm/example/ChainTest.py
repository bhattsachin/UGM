'''
Created on Nov 1, 2012

@author: bhatt
'''
import unittest
import numpy
from edu.buffalo.ugm.model import EdgeStruct
from edu.buffalo.ugm.util import Decode

class Test(unittest.TestCase):


    def testChain(self):
        nNodes = 60
        nStates = 7
        
        adj = numpy.zeros((nNodes, nNodes))
        
        #lets connect them as chain
        for i in range(nNodes - 1):
            adj[i][i + 1] = 1
            
        #make it symmetric now. matrix + transpose(matrix)
        adj = adj + zip(*adj)
        
        print " adj: " + str(adj)
        
        edgeSt = EdgeStruct.EdgeStruct(adj, nStates)
        
        #initial transitions
        initial = numpy.array([.3, .6, .1, 0, 0, 0, 0])
        
        nodePot = numpy.zeros((nNodes, nStates))
        nodePot[0] = initial
        for i in range(1, nNodes):
            for k in range(nStates):
                nodePot[i][k] = 1
        transitions = numpy.array([[.08, .9, .01, 0, 0, 0, .01], [.03, .95, .01, 0, 0, 0, .01], [.06, .06, .75, .05, .05, .02, .01], [0, 0, 0, .3, .6, .09, .01], [0, 0, 0, .02, .95, .02, .01], [0, 0, 0, .01, .01, .97, .01], [0, 0, 0, 0, 0, 0, 1]])
            
        print "nodePot: " + str(nodePot)
        
        maximum = max(edgeSt.numberOfStates)
        edgePot = numpy.zeros((edgeSt.nEdges, maximum, maximum))
        
        #repeat transitions for all edge potentials
        #at each edge we could have had previous state in any of possible states and the same for next one.
        #so each edge has maxstates by maxstates size
        for e in range(edgeSt.nEdges):
            edgePot[e] = transitions
        
        print "edge pot after: " + str(edgePot)
        
        decode = Decode.Decode()
        nodeLabels = decode.chain(nodePot,edgePot, edgeSt)
        print "nodelabels: " + str(nodeLabels)
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testChain']
    unittest.main()
