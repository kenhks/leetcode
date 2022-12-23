from typing import Optional, Tuple

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(n) = 2n
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(node: TreeNode, depth=0) -> Tuple[int, int]:
            nonlocal ans
            left_depth = max(dfs(node.left, depth + 1)) if node.left else depth
            right_depth = max(dfs(node.right, depth + 1)) if node.right else depth
            if ans:
                ans = abs(left_depth - right_depth) <= 1
            return left_depth, right_depth

        if root:
            dfs(root)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isBalanced",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([3, 9, 20, None, None, 15, 7])
    assert solution(root)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1, 2, 2, 3, 3, None, None, 4, 4])
    assert not solution(root)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([])
    assert solution(root)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    root = create_Tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
    assert not solution(root)
