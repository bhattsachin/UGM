'''
Created on Oct 18, 2012

@author: bhatt
'''
from edu.buffalo.ugm.util import ProcessingUtil;

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
      
    