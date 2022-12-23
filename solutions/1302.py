from collections import defaultdict, deque
from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive with hashmap
    Time Complexity: O(n + h)
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        depths_map = defaultdict(list)

        def dfs(node: TreeNode, depth: int = 0):
            if not node.left and not node.right:
                depths_map[depth].append(node.val)
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        if root:
            dfs(root)
        return sum(depths_map[max(depths_map.keys())]) if depths_map else 0


class Solution2:
    """
    BFS, Iterative with stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    h = height of tree ~= log(2, n)
    """

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        prev_stack = deque()
        stack = deque([root]) if root else []
        while stack:
            prev_stack.clear()
            for _ in range(len(stack)):
                node = stack.popleft()
                prev_stack.append(node)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return sum(i.val for i in prev_stack)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "deepestLeavesSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])
    assert solution(root) == 15


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])
    assert solution(root) == 19


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([1])
    assert solution(root) == 1
