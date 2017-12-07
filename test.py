import unittest
#from . import lab
import lab

class Test(unittest.TestCase):
    def test_exceptions(self):
        self.assertRaises(IndexError,lab.func,3312)
        self.assertRaises(IndexError,lab.func,12)
        self.assertRaises(IndexError,lab.func,0)
    def test_normal(self):
        result1, result2 = lab.func(123)
        self.assertEqual(result1, 6)
        self.assertEqual(result2, 6)

        result3, result4 = lab.func(521)
        self.assertEqual(result3, 8)
        self.assertEqual(result4, 10)

        result5, result6 = lab.func(774)
        self.assertEqual(result5, 18)
        self.assertEqual(result6, 196)
    def test_negative(self):
        self.assertRaises(ValueError,lab.func,-12)
        self.assertRaises(ValueError,lab.func,-1)
        self.assertRaises(ValueError,lab.func,'abc')
if __name__=='__main__':
    unittest.main()
