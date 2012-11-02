'''
Created on Oct 27, 2012

@author: bhatt
'''
import unittest
from edu.buffalo.io import PIL

class PILTest(unittest.TestCase):


    def testPIL(self):
        
        pil = PIL.PIL()
        pil.readWrite()
        
        
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'PILTest.testPIL']
    unittest.main()