from collections import Counter, defaultdict
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Direct
    Time Complexity: O(n)
    Space Complexity: O(n) = 27n
    """

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_counter = defaultdict(int)
        for c in licensePlate:
            if c.isalpha():
                license_counter[c.lower()] += 1
        ans = None
        for word in words:
            word_counter = Counter(word)
            for char in license_counter:
                if word_counter.get(char, 0) < license_counter[char]:
                    break
            else:
                if ans is None or len(word) < len(ans):
                    ans = word
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "shortestCompletingWord",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    licensePlate = "1s3 PSt"
    words = ["step", "steps", "stripe", "stepple"]
    assert solution(licensePlate, words) == "steps"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    licensePlate = "1s3 456"
    words = ["looks", "pest", "stew", "show"]
    assert solution(licensePlate, words) == "pest"
