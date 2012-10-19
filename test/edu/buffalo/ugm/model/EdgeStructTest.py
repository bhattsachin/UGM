'''
Created on Oct 18, 2012

@author: bhatt
'''
import unittest
import numpy
from edu.buffalo.ugm.model import EdgeStruct


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
        
        edgeSt = EdgeStruct.EdgeStruct()
        edges = edgeSt.init(adj,nStates)
        
        print "edges: " + str(edges)
        
        
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'EdgeStructTest.testEdgeStruct']
    unittest.main()