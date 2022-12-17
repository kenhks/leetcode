from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if low <= node.val <= high:
                ans += node.val
            if low < node.val and node.left:
                dfs(node.left)
            if node.val < high and node.right:
                dfs(node.right)

        if root:
            dfs(root)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "rangeSumBST",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([10, 5, 15, 3, 7, None, 18])
    assert solution(root, low=7, high=15) == 32


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
    assert solution(root, low=6, high=10) == 23


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([1])
    assert solution(root, low=0, high=2) == 1
