'''
Created on Oct 12, 2012

@author: bhatt
'''

import numpy

class Small(object):

        
    def run(self):
        nNodes = 4;
        nStates = 2;
        
        adj = numpy.zeros((nNodes, nNodes));
        i = -1; #incase of matlab make this 0
        adj[i+1][i+2] = 1;
        adj[i+2][i+1] = 1;
        adj[i+2][i+3] = 1;
        adj[i+3][i+2] = 1;
        adj[i+3][i+4] = 1;
        adj[i+4][i+3] = 1;