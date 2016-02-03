# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertRaises(ValueError, utils.fact, -1)
        self.assertEqual(utils.fact(0), 1)
        self.assertEqual(utils.fact(5), 120)
    
    def test_roots(self):
        
        pass
    
    def test_integrate(self):
        
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
