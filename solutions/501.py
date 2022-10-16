from typing import List, Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    Use hashmap store frequency
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = {}

        def dfs(node):
            if node is not None:
                count[node.val] = count.get(node.val, 0) + 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        ans = []
        max_count = 0
        for i, j in count.items():
            if j > max_count:
                ans = [i]
                max_count = j
            elif j == max_count:
                ans.append(i)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findMode",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    # nums = [1, None, 2, 2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    assert solution(root) == [2]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([0])
    assert solution(root) == [0]
