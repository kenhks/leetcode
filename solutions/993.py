from collections import deque
from typing import Optional

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

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        ans = False

        def dfs(node: TreeNode, target: int, parent, depth=0) -> int:
            if node:
                if node.val == target:
                    return parent, depth
                else:
                    return dfs(node.left, target, node, depth + 1) or dfs(node.right, target, node, depth + 1)

        if root:
            x_parent, x_depth = dfs(root, x, None)
            y_parent, y_depth = dfs(root, y, None)
            ans = x_depth == y_depth and x_parent != y_parent
        return ans


class Solution2:
    """
    DFS, Recursive with hashmap
    Time Complexity: O(n) = n
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        ans = False
        target = {}

        def dfs(node: TreeNode, parent, depth=0) -> int:
            if node and (x not in target or y not in target):
                if node.val == x:
                    target[x] = (parent, depth)
                elif node.val == y:
                    target[y] = (parent, depth)
                else:
                    dfs(node.left, node, depth + 1)
                    dfs(node.right, node, depth + 1)

        if root:
            dfs(root, None)
            x_parent, x_depth = target[x]
            y_parent, y_depth = target[y]
            ans = x_depth == y_depth and x_parent != y_parent
        return ans


class Solution3:
    """
    BFS, Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        ans = False
        if root and root.val != x and root.val != y:
            stack = deque([(root, None)])
            while stack:
                x_parent, y_parent = None, None
                for _ in range(len(stack)):
                    node, parent = stack.popleft()
                    if node.val == x:
                        x_parent = parent
                    elif node.val == y:
                        y_parent = parent
                    if node.left:
                        stack.append((node.left, node))
                    if node.right:
                        stack.append((node.right, node))
                    if x_parent and y_parent:
                        ans = x_parent != y_parent
                        break
                else:
                    if x_parent or y_parent:
                        break
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "isCousins",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, 2, 3, 4])
    assert not solution(root, x=4, y=3)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1, 2, 3, None, 4, None, 5])
    assert solution(root, x=5, y=4)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([1, 2, 3, None, 4])
    assert not solution(root, x=2, y=3)
