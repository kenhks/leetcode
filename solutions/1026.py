from collections import deque
from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS with recursion
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, min_val, max_val):
            nonlocal ans
            ans = max(
                abs(node.val - min_val),
                abs(node.val - max_val),
                ans,
            )
            min_val = min(node.val, min_val)
            max_val = max(node.val, max_val)
            if node.left:
                dfs(node.left, min_val, max_val)
            if node.right:
                dfs(node.right, min_val, max_val)

        if root:
            dfs(root, root.val, root.val)
        return ans


class Solution2:
    """
    BFS, Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        nodes = deque([(root, root.val, root.val)]) if root else []
        while nodes:
            for _ in range(len(nodes)):
                node, min_val, max_val = nodes.popleft()
                ans = max(
                    abs(node.val - min_val),
                    abs(node.val - max_val),
                    ans,
                )
                min_val = min(node.val, min_val)
                max_val = max(node.val, max_val)
                if node.left:
                    nodes.append((node.left, min_val, max_val))
                if node.right:
                    nodes.append((node.right, min_val, max_val))
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "maxAncestorDiff",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])
    assert solution(root) == 7


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1, None, 2, None, 0, 3])
    assert solution(root) == 3
