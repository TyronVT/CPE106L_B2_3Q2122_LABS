import code
import unittest

class TestCode(unittest.TestCase):
  def testsimple(self):
    self.assertEqual(code.return_zero(),0)
  
  def testdouble(self):
    test_values = [2, 4, 0, -2]
    correct_values = [4, 8, 0, -4]
    for (x, y) in zip(test_values, correct_values):
      self.assertEqual(code.double(x), y)
      

if __name__=='__main__':
  unittest.main()