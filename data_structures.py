class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val, self.next}"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={id(self)},val={self.val})"


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val, self.left, self.right}"

    def __repr__(self):
        return f"{self.__class__.__name__}(val={self.val})"
