'''
Created on Oct 12, 2012

@author: bhatt
'''

class EdgeStruct(object):
    '''
    classdocs
    '''
    #assuming we are working on 2D array at max. Hence states will always be one Dimensional
    numberOfStates = []
    
    #edges will 2 D array
    edges = []
    
    #nodes in this graph
    nodes = []
    
    #adjacency graph
    adj = []


    def __init__(self, adj, nStates):
        '''
        creates two columns for each edge and it's end points
        '''
        'find all the edges'
        edges = []
        line = 0
        for idx,row in enumerate(adj): #we don't really need to enumerate
            line = row;
            for idy, col in enumerate(line):
                if idy > idx: #considering only upper half of adjoint matrix
                    if adj[idx][idy] == 1:
                        item=[]
                        item.append(idx)
                        item.append(idy)
                        edges.append([idx,idy]);
        
        self.edges = edges
        self.adj = adj
        
        
        for i in range(len(line)):
            self.nodes.append(i)
            self.numberOfStates.append(nStates) #all variables have same number of states
       
                        
    '''
    Returns two nodes this edge belongs to
    @raise exception:index out of bound 
    '''    
    def edgeEnds(self,index):
        return self.edges[index]
    
    
    '''
    Returns edges connecting given node
    @param n: node number 
    '''
    def getEdges(self,n):
        cEdges = []
        for idx, row in enumerate(self.edges):
            if n in row:
                cEdges.append(idx)
            
        return cEdges
    '''
    Returns neighbors to given input node n
    @param n: input node 
    '''
    def getNeighbour(self,n):
        cNodes = []
        for row in self.edges:
            if n in row:
                for col in row:
                    if n!=col:
                        cNodes.append(col)
        return cNodes
        
    
    