from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.testCases = {
            1: {'nums': [10,10,10,10,10], 'k': 5, 'output': 50},
            2: {'nums': [1,10,3,3,3], 'k': 3, 'output': 17}
        }
        self.obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        nums, k, output = self.testCases[1].values()
        result = self.obj.maxKelements(nums = nums, k = k)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        nums, k, output = self.testCases[2].values()
        result = self.obj.maxKelements(nums = nums, k = k)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()