import string
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Use Hashmap
    Time Complexity: O(S)
    Space Complexity: O(S)
    S = the sum of the lengths of words
    """

    code_map = {
        i: j
        for i, j in zip(
            string.ascii_lowercase,
            [
                ".-",
                "-...",
                "-.-.",
                "-..",
                ".",
                "..-.",
                "--.",
                "....",
                "..",
                ".---",
                "-.-",
                ".-..",
                "--",
                "-.",
                "---",
                ".--.",
                "--.-",
                ".-.",
                "...",
                "-",
                "..-",
                "...-",
                ".--",
                "-..-",
                "-.--",
                "--..",
            ],
        )
    }

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if len(words) == 1:
            return 1
        code_set = set()
        for word in words:
            code_set.add("".join(map(lambda x: self.code_map[x], word)))
        return len(code_set)


class Solution2:
    """
    Use fixed size array
    Time Complexity: O(S)
    Space Complexity: O(S)
    S = the sum of the lengths of words
    """

    code_map = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
    ]

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if len(words) == 1:
            return 1
        offset = ord("a")
        code_set = set()
        for word in words:
            code_set.add("".join(map(lambda x: self.code_map[ord(x) - offset], word)))
        return len(code_set)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "uniqueMorseRepresentations",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(["gin", "zen", "gig", "msg"]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(["a"]) == 1
