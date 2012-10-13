'''
Created on Oct 12, 2012

@author: bhatt
'''
import unittest
from edu.buffalo.ugm.example import Small;


class SmallTest(unittest.TestCase):


    def testRun(self):
        smallx = Small.Small()
        print "check this"
        smallx.run()
        
        
        
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'SmallTest.testRun']
    unittest.main()