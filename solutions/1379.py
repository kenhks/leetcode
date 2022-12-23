from collections import deque

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

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node1: TreeNode, node2: TreeNode) -> TreeNode:
            if not node1:
                return
            if node1.val == target.val:
                return node2
            else:
                return dfs(node1.left, node2.left) or dfs(node1.right, node2.right)

        return dfs(original, cloned)


class Solution2:
    """
    BFS, Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ans = None
        stack = deque([(original, cloned)]) if original and cloned else []
        while stack and not ans:
            for _ in range(len(stack)):
                node1, node2 = stack.popleft()
                if node1.val == target.val:
                    ans = node2
                    break
                else:
                    if node1.left:
                        stack.append((node1.left, node2.left))
                    if node1.right:
                        stack.append((node1.right, node2.right))
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "getTargetCopy",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root1 = create_Tree([7, 4, 3, None, None, 6, 19])
    root2 = create_Tree([7, 4, 3, None, None, 6, 19])
    target = root1.right  # val = 3
    expected = root2.right  # val = 3
    assert solution(root1, root2, target) == expected


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root1 = create_Tree([7])
    root2 = create_Tree([7])
    target = root1  # val = 7
    expected = root2  # val = 7
    assert solution(root1, root2, target) == expected


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root1 = create_Tree([8, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])
    root2 = create_Tree([8, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])
    target = root1.right.right.right  # val = 4
    expected = root2.right.right.right  # val = 4
    assert solution(root1, root2, target) == expected
