from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(mn)
    Space Complexity: O(1)
    m = len(list1)
    n = len(list2)
    """

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_index_sum = float("inf")
        ans = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    index_sum = i + j
                    if index_sum < min_index_sum:
                        min_index_sum = index_sum
                        ans.clear()
                        ans.append(list1[i])
                    elif index_sum == min_index_sum:
                        ans.append(list1[i])
        return ans


class Solution2:
    """
    Hashmap
    Time Complexity: O(mn)
    Space Complexity: O(min(m, n))
    m = len(list1)
    n = len(list2)
    """

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_index_sum = float("inf")
        list1_map = {}
        ans = []
        if len(list1) > len(list2):
            list1, list2 = list2, list1
        for i in range(len(list1)):
            list1_map[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in list1_map:
                index_sum = list1_map[list2[j]] + j
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    ans.clear()
                    ans.append(list2[j])
                elif index_sum == min_index_sum:
                    ans.append(list2[j])
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "findRestaurant",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    assert set(solution(list1, list2)) == set(["Shogun"])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    assert set(solution(list1, list2)) == set(["Shogun"])


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    list1 = ["happy", "sad", "good"]
    list2 = ["sad", "happy", "good"]
    assert set(solution(list1, list2)) == set(["sad", "happy"])
