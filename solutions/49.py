from typing import List
import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap for sorted word
    Time Complexity: O(mn(log(2, n))
    Space Complexity: O(m)
    m = the number of words in string
    n = the number of character in word
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        size_map = dict()
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in size_map:
                size_map[sorted_word] = [word]
            else:
                size_map[sorted_word].append(word)
        return list(size_map.values())


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "groupAnagrams",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    expected = sorted(
        [
            ["bat"],
            ["nat", "tan"],
            ["ate", "eat", "tea"],
        ],
        key=lambda x: sorted(x[0]),
    )
    actual = sorted(solution(["eat", "tea", "tan", "ate", "nat", "bat"]), key=lambda x: sorted(x[0]))
    assert len(expected) == len(actual)
    for actual_ele, expected_ele in zip(actual, expected):
        assert set(actual_ele) == set(expected_ele)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([""]) == [[""]]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(["a"]) == [["a"]]
