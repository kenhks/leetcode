from collections import deque
from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: TreeNode):
            nonlocal ans
            left_sum = dfs(node.left) if node.left else 0
            right_sum = dfs(node.right) if node.right else 0
            ans += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum

        if root:
            dfs(root)
        return ans


class Solution2:
    """
    DFS, Iterative Post Order Traversal with stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = deque([(0, root)]) if root else []
        while stack:
            checked, node = stack.pop()
            node.sum = 0
            if not checked:
                stack.append((1, node))
                if node.right:
                    stack.append((0, node.right))
                if node.left:
                    stack.append((0, node.left))
            else:
                left_sum = node.left.sum if node.left else 0
                right_sum = node.right.sum if node.right else 0
                node.sum = node.val + left_sum + right_sum
                ans += abs(left_sum - right_sum)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "findTilt",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, 2, 3])
    assert solution(root) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([4, 2, 9, 3, 5, None, 7])
    assert solution(root) == 15


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([21, 7, 14, 1, 1, 2, 2, 3, 3])
    assert solution(root) == 9
