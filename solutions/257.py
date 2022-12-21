from collections import deque
from typing import List, Optional

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

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(node: TreeNode, path):
            path += f"->{node.val}" if path else f"{node.val}"
            if not node.left and not node.right:
                ans.append(path)
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

        if root:
            dfs(root, "")
        return ans


class Solution2:
    """
    BFS, Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        nodes = deque([(root, "")]) if root else []
        while nodes:
            for _ in range(len(nodes)):
                node, path = nodes.popleft()
                path += f"->{node.val}" if path else f"{node.val}"
                if node.left:
                    nodes.append((node.left, path))
                if node.right:
                    nodes.append((node.right, path))
                if not node.left and not node.right:
                    ans.append(path)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "binaryTreePaths",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, 2, 3, None, 5])
    assert set(solution(root)) == set(["1->2->5", "1->3"])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1])
    assert solution(root) == ["1"]
