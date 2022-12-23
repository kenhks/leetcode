from collections import deque
from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive with hashset
    Time Complexity: O(n(log(2, n)))
    Space Complexity: O(n)
    h = height of tree ~= log(2, n)
    """

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        node_values = set()

        def dfs(node: TreeNode):
            node_values.add(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        if root:
            dfs(root)
        return sorted(node_values)[1] if len(node_values) >= 2 else -1


class Solution2:
    """
    DFS, Recursive with two pointer
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min_1, min_2 = -1, -1

        def dfs(node: TreeNode):
            nonlocal min_1, min_2
            if min_1 == -1:
                min_1 = node.val
            elif node.val < min_1:
                min_1, min_2 = node.val, min_1
            elif min_1 < node.val and (min_2 == -1 or node.val < min_2):
                min_2 = node.val
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        return min_2


class Solution3:
    """
    BFS, Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min_1, min_2 = -1, -1
        stack = deque([root]) if root else []
        while stack:
            for _ in range(len(stack)):
                node = stack.popleft()
                if min_1 == -1:
                    min_1 = node.val
                elif node.val < min_1:
                    min_1, min_2 = node.val, min_1
                elif min_1 < node.val and (min_2 == -1 or node.val < min_2):
                    min_2 = node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return min_2


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "findSecondMinimumValue",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([2, 2, 5, None, None, 5, 7])
    assert solution(root) == 5


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([2, 2, 2])
    assert solution(root) == -1
