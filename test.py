import unittest
import sonar

class Test(unittest.TestCase):

    # Test 1, should pass
    def test(self):
        self.assertEqual(sonar.sonar_sweep("input_7.txt"), 7)
    
    # Test 2, should fail
    def test2(self):
        self.assertNotEqual(sonar.sonar_sweep("input_7.txt"), 8)

    # Test 3, should pass.
    def test3(self):
        self.assertEqual(sonar.sonar_sweep("input_0.txt"), 0)
 