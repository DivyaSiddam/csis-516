import unittest

def find_smallest_cycle(arr):

    n = len(arr)

    # Helper function to check if arr starts repeating at a given cycle length
    def check_cycle(cycle_length):
        for i in range(cycle_length, n):
            if arr[i] != arr[i % cycle_length]:
                return False
        return True

    # Try cycle lengths from 1 to n (but check divisors of n to optimize)
    for cycle_length in range(1, n + 1):
        if n % cycle_length == 0:  # Only check divisors of n
            if check_cycle(cycle_length):
                return cycle_length

    return n  # If no cycle is found, return the full length of the list

class TestFindSmallestCycle(unittest.TestCase):

    def test_case_1(self):
        # [1, 2, 3] perfectly repeats, so the smallest cycle length is 3.
        arr = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        expected = 3
        result = find_smallest_cycle(arr)
        self.assertEqual(result, expected)

    def test_case_2(self):
        # No smaller repeating cycle exists, so the full length (7) is returned.
        arr = [4, 5, 6, 4, 5, 6, 4]
        expected = 7
        result = find_smallest_cycle(arr)
        self.assertEqual(result, expected)

    def test_case_3(self):
        # No smaller repeating cycle exists, so the full length (7) is returned.
        arr = [1, 2, 1, 2, 1, 2, 1]
        expected = 7
        result = find_smallest_cycle(arr)
        self.assertEqual(result, expected)

    def test_case_4(self):
        # No repetition, so the cycle length is the length of the list (5).
        arr = [7, 8, 9, 10, 11]
        expected = 5
        result = find_smallest_cycle(arr)
        self.assertEqual(result, expected)

    def test_case_5(self):
        # The cycle [1] repeats throughout, so the smallest cycle length is 1.
        arr = [1, 1, 1, 1, 1]
        expected = 1
        result = find_smallest_cycle(arr)
        self.assertEqual(result, expected)

    def test_case_6(self):
        # No valid cycle shorter than the whole sequence exists, so the cycle length is 5.
        arr = [5, 10, 5, 10, 5]
        expected = 5
        result = find_smallest_cycle(arr)
        self.assertEqual(result, expected)

# This is needed to run the tests in Jupyter/Colab.
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
