from typing import Optional
from data_structures import TreeNode
import pytest

from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    Recursive, In-order Traversal
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []

        def dfs(node: TreeNode):
            if node.left:
                dfs(node.left)
            values.append(node.val)
            if node.right:
                dfs(node.right)

        if root:
            dfs(root)
        min_diff = float("inf")
        for i, j in zip(values, values[1:]):
            min_diff = min(min_diff, j - i)
            if min_diff == 1:
                break
        return min_diff


class Solution2:
    """
    Recursive, In-order Traversal
    Time Complexity: O(n)
    Space Complexity: O(h)
    h ~= log(2, n), the height of tree
    """

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, min_diff = float("-inf"), float("inf")

        def dfs(node: TreeNode):
            nonlocal prev, min_diff
            if min_diff > 1:
                if node.left:
                    dfs(node.left)
                min_diff = min(min_diff, node.val - prev)
                prev = node.val
                if node.right:
                    dfs(node.right)
        if root:
            dfs(root)
        return min_diff

solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "minDiffInBST",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([4, 2, 6, 1, 3])
    assert solution(root) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1, 0, 48, None, None, 12, 49])
    assert solution(root) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([90, 69, None, 49, 89, None, 52])
    assert solution(root) == 1
