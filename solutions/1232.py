from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dy, dx = (y1 - y0), (x1 - x0)
        return all(dy * (x - x0) == dx * (y - y0) for x, y in coordinates)


def test_1():
    assert (
        Solution().checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
        == True
    )


def test_2():
    assert (
        Solution().checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])
        == False
    )


def test_3():
    assert Solution().checkStraightLine([[0, 0], [0, 1], [0, -1]]) == True


def test_4():
    assert Solution().checkStraightLine([[0, 0], [0, 1], [1, 0]]) == False
