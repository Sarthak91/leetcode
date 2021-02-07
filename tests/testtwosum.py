import unittest
from  arrays.two_sum import TwoSum

class TestTwoSum(unittest.TestCase):

    def test_two_sum(self):
        arr = [1,3, 2, 1]
        target = 5
        two_sum = TwoSum(arr=arr, target=target)
        self.assertEqual(two_sum.get_to_sum(), [1,2])

if __name__ == "__main__":
    unittest.main()