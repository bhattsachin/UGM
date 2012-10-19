'''
Created on Oct 12, 2012

@author: bhatt
'''

class EdgeStruct(object):
    '''
    classdocs
    '''
    #assuming we are working on 2D array at max. Hence states would always be one Dimensional
    numberOfStates = []
    
    #edges will 2 D array
    #edges = []


    def __init__(self):
        '''
        Constructor
        '''
       
                        
    '''
    Kind of initialization. creates two columns for each edge and it's end points
    '''                    
    def init(self, adj, nStates):
        'find all the edges'
        edges = []
        for idx,row in enumerate(adj):
            line = row;
            
            for idy, col in enumerate(line):
                if idy > idx: #considering only upper half of adjoint matrix
                    if adj[idx][idy] == 1:
                        item=[]
                        item.append(idx)
                        item.append(idy)
                        edges.append([idx,idy]);
        
        return edges;