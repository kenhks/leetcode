from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float("inf")
        ans = -1
        for i, (pt_x, pt_y) in enumerate(points):
            if x == pt_x or y == pt_y:
                pt_distance = abs(x - pt_x) + abs(y - pt_y)
                if pt_distance < min_distance:
                    ans = i
                    min_distance = pt_distance
        return ans

def test_1():
    points = [
        [1,2],
        [3,1],
        [2,4],
        [2,3],
        [4,4],
    ]
    assert Solution().nearestValidPoint(3, 4, points) == 2


def test_2():
    points = [
        [3,4],
    ]
    assert Solution().nearestValidPoint(3, 4, points) == 0

def test_3():
    points = [
        [2,3],
    ]
    assert Solution().nearestValidPoint(3, 4, points) == -1