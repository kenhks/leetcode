from collections import deque
from typing import List, Optional, Tuple, Union

from data_structures import ListNode, Node, TreeNode


def create_LinkedList(
    nums: List, return_tail=False
) -> Union[Tuple[Optional[ListNode], Optional[ListNode]], Optional[ListNode]]:
    if not nums:
        return None
    prev_node = head = ListNode(nums[0])
    for i in nums[1:]:
        prev_node.next = ListNode(i)
        prev_node = prev_node.next
    if return_tail:
        return head, prev_node
    else:
        return head


def create_LinkedListCycle(nums: List, cycle: Tuple[int, int]) -> Optional[ListNode]:
    if not nums:
        return None
    nodes = [ListNode(i) for i in nums]
    for i, j in zip(nodes, nodes[1:]):
        i.next = j
    nodes[cycle[0]].next = nodes[cycle[-1]]
    return nodes[0]


def get_LinkedList_values(node: ListNode) -> List:
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


def create_Tree(nums: List, node_cls=None) -> Optional[TreeNode]:
    if not nums or nums[0] is None:
        return None
    nums = deque(nums)
    node_cls = node_cls or TreeNode
    root = node_cls(nums.popleft())
    level_nodes = [root]

    def create_node(val):
        if val is not None:
            return node_cls(val)

    while level_nodes and len(nums):
        new_level_nodes = []
        for node in level_nodes:
            if not nums:
                break
            left_node = create_node(nums.popleft())
            right_node = create_node(nums.popleft()) if nums else None
            if left_node:
                node.left = left_node
                new_level_nodes.append(left_node)
            if right_node:
                node.right = right_node
                new_level_nodes.append(right_node)
        level_nodes = new_level_nodes
    return root


def get_Tree_values(root: TreeNode) -> List:
    level_nodes = [root]
    values = []
    while any(i is not None for i in level_nodes):
        values.extend([i.val if i is not None else None for i in level_nodes])
        new_level_nodes = []
        for n in level_nodes:
            if not n:
                continue
            new_level_nodes.append(n.left)
            new_level_nodes.append(n.right)
        level_nodes = new_level_nodes
    return values


def create_GenericTree(values):
    if not values:
        return None
    root = Node(values[0])
    n = len(values)
    level_left = level_right = 2
    prev_level_nodes = [root]
    while level_left <= level_right < n:
        none_count = 0
        while level_right < n:
            if values[level_right] is None:
                none_count += 1
                if none_count == len(prev_level_nodes):
                    break
            level_right += 1
        parent = prev_level_nodes.pop(0)
        level_nodes = []
        for v in values[level_left:level_right]:
            if not v:
                parent = prev_level_nodes.pop(0)
            else:
                new_node = Node(v)
                if parent.children:
                    parent.children.append(new_node)
                else:
                    parent.children = [new_node]
                level_nodes.append(new_node)
        prev_level_nodes = level_nodes
        level_right = level_left = level_right + 1
    return root


def get_perfect_BinaryTree_next_values(root: Optional[TreeNode]) -> List:
    values = []
    if root:
        node = next_node = root
        while node:
            while next_node:
                values.append(next_node.val)
                next_node = next_node.next
            else:
                values.append(None)
            node = next_node = node.left
    return values


def create_function(cls, func_name):
    def _func(*args, **kwargs):
        return getattr(cls(), func_name)(*args, **kwargs)

    _func.__name__ = cls.__name__
    return _func


def parametrize_solution_cls(sol_cls_list: List, sol_func_name):
    return [create_function(sol_cls, sol_func_name) for sol_cls in sol_cls_list]
