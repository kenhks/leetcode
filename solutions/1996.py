from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        weak = 0
        for i, (attack_i, defense_i) in enumerate(properties):
            for j, (attack_j, defense_j) in enumerate(properties):
                if i == j:
                    continue
                if attack_i < attack_j and defense_i < defense_j:
                    weak += 1
                    break
        return weak


class Solution2:
    """
    Sort first
    Time Complexity: O(n^2) = n^2 + nlog(2, n)
    Space Complexity: O(n)
    """

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        weak = 0
        properties.sort(key=lambda x: (x[0], x[1]))
        for i, (attack_i, defense_i) in enumerate(properties):
            for attack_j, defense_j in properties[i + 1 :]:
                if attack_i < attack_j and defense_i < defense_j:
                    weak += 1
                    break
        return weak


class Solution3:
    """
    Sort descending by attack, ascending by defence
    Time Complexity: O(nlog(2, n)) = nlog(2, n) + n
    Space Complexity: O(n)
    """

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        weak, max_defense = 0, 0
        for _, defense in properties:
            if defense < max_defense:
                weak += 1
            else:
                max_defense = defense
        return weak


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "numberOfWeakCharacters",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([[5, 5], [6, 3], [3, 6]]) == 0


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([[2, 2], [3, 3]]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([[1, 5], [10, 4], [4, 3]]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([[1, 1], [10, 8], [4, 2]]) == 2
