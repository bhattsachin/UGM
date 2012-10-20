'''
Created on Oct 18, 2012

@author: bhatt
'''
import unittest
import numpy
from edu.buffalo.ugm.model import EdgeStruct
from edu.buffalo.ugm.util import Decode


class EdgeStructTest(unittest.TestCase):


    def testEdgeStruct(self):
        
        nNodes = 4
        nStates = 2
        
        adj = numpy.zeros((nNodes, nNodes))
        i = -1 #incase of matlab make this 0
        adj[i+1][i+2] = 1
        adj[i+2][i+1] = 1
        adj[i+2][i+3] = 1
        adj[i+3][i+2] = 1
        adj[i+3][i+4] = 1
        adj[i+4][i+3] = 1
        
        edgeSt = EdgeStruct.EdgeStruct(adj,nStates)
        #edgeSt.init(adj,nStates)
        
        print "edges: " + str(edgeSt.edges)
        print "nStates: " + str(edgeSt.numberOfStates)
        print "nodes associated with edge 1: " + str(edgeSt.edgeEnds(1))
        #edgeSt.getEdges(2)
        print "edges with node 2: " + str(edgeSt.getEdges(2))
        print "neighbours of node 2: " + str(edgeSt.getNeighbour(2))
        
        
        #node potentials
        nodePot = numpy.array([[1,3],[9,1],[1,3],[9,1]])
        print "node pot " + str(nodePot)
        maximum = max(edgeSt.numberOfStates)
        print "max:" + str(maximum)
        
        # 3 dimensional array
        edgePot = numpy.zeros((edgeSt.nEdges,maximum,maximum)) #slightly different than Matlab implementation 
        print "edge pot:" + str(edgePot)
        
        #in this example edge potentials are homogeneous, but this may not be the case every time
        for e in range(edgeSt.nEdges):
            edgePot[e] = [[2,1],[1,2]]
        
        print "edge pot after: " + str(edgePot)
        
        
        #TODO: move this block to different test unit
        decode = Decode.Decode()
        decode.exact(nodePot,edgePot, edgeSt)
        
        
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'EdgeStructTest.testEdgeStruct']
    unittest.main()