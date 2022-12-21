import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    Recursive
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree
    """

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = root
        if p.val == q.val:
            ans = p
        else:
            min_val = min(p.val, q.val)
            max_val = max(p.val, q.val)
            if max_val < root.val:
                ans = self.lowestCommonAncestor(root.left, p, q)
            elif root.val < min_val:
                ans = self.lowestCommonAncestor(root.right, p, q)
        return ans


class Solution2:
    """
    Iterative
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val == q.val:
            return p
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        ans = curr = root
        while curr:
            if curr.val >= min_val and curr.val <= max_val:
                ans = curr
                break
            elif curr.val < min_val and curr.val < max_val:
                curr = curr.right
            elif curr.val > min_val and curr.val > max_val:
                curr = curr.left
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "lowestCommonAncestor",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = root.left  # p = 2
    q = root.right  # q = 8
    expected = root  # ans = 6
    assert solution(root, p, q) == expected


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = root.left  # p = 2
    q = root.left.right  # q = 4
    expected = p  # ans = 2
    assert solution(root, p, q) == expected


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([2, 1])
    p = root  # p = 2
    q = root.left  # q = 1
    expected = p  # ans = 2
    assert solution(root, p, q) == expected
