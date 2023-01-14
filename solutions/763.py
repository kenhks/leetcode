from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    DP
    Time Complexity: O(n^2)
    Space Complexity: O(n) = 2n
    """

    def partitionLabels(self, s: str) -> List[int]:
        dp = []
        for c in s:
            for i in range(len(dp)):
                partition_set, _ = dp[i]
                if c in partition_set:
                    new_partition_set = set()
                    new_partition_size = 1
                    while len(dp) > i:
                        prev_partition_set, prev_partition_size = dp.pop()
                        new_partition_set |= prev_partition_set
                        new_partition_size += prev_partition_size
                    dp.append((new_partition_set, new_partition_size))
                    break
            else:
                dp.append((set(c), 1))
        return [i[1] for i in dp]


class Solution2:
    """
    Hashmap for last occurence
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {c: i for i, c in enumerate(s)}
        ans = []
        partition_size = 1
        partition_end_index = 0
        for i, c in enumerate(s):
            partition_end_index = max(partition_end_index, last_occurence[c])
            if i >= partition_end_index:
                ans.append(partition_size)
                partition_size = 0
            partition_size += 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "partitionLabels",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(s="ababcbacadefegdehijhklij") == [9, 7, 8]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(s="eccbbbbdec") == [10]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(s="abcde") == [1, 1, 1, 1, 1]
