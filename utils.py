from typing import List

from data_structures import ListNode


def create_LinkedList(nums: List) -> ListNode:
    if not nums:
        return None
    prev_node = head = ListNode(nums[0])
    for i in nums[1:]:
        prev_node.next = ListNode(i)
        prev_node = prev_node.next
    return head


def get_LinkedList_values(node: ListNode) -> List:
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


def create_function(cls, func_name):
    def _func(*args, **kwargs):
        return getattr(cls(), func_name)(*args, **kwargs)
    _func.__name__ = cls.__name__
    return _func


def parametrize_solution_cls(sol_cls_list: List, sol_func_name):
    return [
        create_function(sol_cls, sol_func_name)
        for sol_cls in sol_cls_list
    ]
