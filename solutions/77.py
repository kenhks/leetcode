from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Recursive
    Time Complexity: O(k * nCk)
    Space Complexity: O(k)
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == k:
            return [[i for i in range(1, n + 1)]]
        elif k == 1:
            return [[i] for i in range(1, n + 1)]
        else:
            ans = []
            for prev in self.combine(n, k - 1):
                for i in range(prev[-1] + 1, n + 1):
                    ans.append(prev + [i])
            return ans


class Solution2:
    """
    Iterative
    Time Complexity: O(k * nCk)
    Space Complexity: O(k)
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = [[i] for i in range(1, 1 + n)]
        while k > 1:
            new_ans = []
            for comb in ans:
                for i in range(comb[-1] + 1, 1 + n):
                    new_ans.append(comb + [i])
            ans = new_ans
            k -= 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "combine",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    expected = [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 4],
    ]
    assert sorted(solution(n=4, k=2), key=lambda x: tuple(x)) == expected


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    expected = [[1]]
    assert sorted(solution(n=1, k=1), key=lambda x: tuple(x)) == expected


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    expected = [
        [1, 2, 3],
        [1, 2, 4],
        [1, 2, 5],
        [1, 3, 4],
        [1, 3, 5],
        [1, 4, 5],
        [2, 3, 4],
        [2, 3, 5],
        [2, 4, 5],
        [3, 4, 5],
    ]
    assert sorted(solution(n=5, k=3), key=lambda x: tuple(x)) == expected


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    expected = [
        [1, 2],
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 3],
        [2, 4],
        [2, 5],
        [3, 4],
        [3, 5],
        [4, 5],
    ]
    assert sorted(solution(n=5, k=2), key=lambda x: tuple(x)) == expected
