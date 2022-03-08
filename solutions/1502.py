from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True
        arr.sort()
        diff = arr[0] - arr[1]
        for i in range(1, len(arr) - 1):
            if arr[i] - arr[i + 1] != diff:
                return False
        else:
            return True


def test_1():
    assert Solution().canMakeArithmeticProgression([3, 5, 1]) == True


def test_2():
    assert Solution().canMakeArithmeticProgression([1, 2, 4]) == False
