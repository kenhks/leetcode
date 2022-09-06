from collections import Counter
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan with frequency hashmap
    Time Complexity: O(S) = S + 26
    Space Complexity: O(1) = 52
    S is the sum of all characters in all strings
    """

    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        for w in words[1:]:
            w_counter = Counter(w)
            common = {
                i: min(w_counter[i], common[i])
                for i in (w_counter.keys() & common.keys())
            }
            if not common:
                break
        result = []
        for char in common:
            for _ in range(common[char]):
                result.append(char)
        return result


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "commonChars",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert sorted(solution(["bella", "label", "roller"])) == ["e", "l", "l"]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert sorted(solution(["cool", "lock", "cook"])) == ["c", "o"]
