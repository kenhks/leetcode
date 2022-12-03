from collections import Counter

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap for frequency count
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        ans = ""
        for c, f in counter.most_common():
            ans += f"{c}" * f
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "frequencySort",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(s="tree") == "eetr"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(s="cccaaa") == "cccaaa"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(s="Aabb") == "bbAa"
