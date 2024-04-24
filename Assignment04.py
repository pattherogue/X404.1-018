# 1. 
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def reverse(self):
        if not self.head:  # Check if the list is empty
            return  # Do nothing if the list is empty

        current = self.head
        while current:
            # Swap the prev and next pointers
            temp = current.prev
            current.prev = current.next
            current.next = temp
            # Move to the next node in the original list
            current = current.prev

        # Update head and tail after the reversal
        if temp:
            self.head = temp.prev

        # Ensure the new head's prev is None
        self.head.prev = None

        # Correctly update the tail to the old head
        self.tail = self.head
        while self.tail and self.tail.next:
            self.tail = self.tail.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# 2.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def union(head1, head2):
    seen = set()
    result_head = None
    result_tail = None

    # Function to add a node to the result list
    def add_to_result(data):
        nonlocal result_head, result_tail
        if data not in seen:
            seen.add(data)
            if result_head is None:
                result_head = Node(data)
                result_tail = result_head
            else:
                result_tail.next = Node(data)
                result_tail = result_tail.next

    current = head1
    while current:
        add_to_result(current.data)
        current = current.next

    current = head2
    while current:
        add_to_result(current.data)
        current = current.next

    return result_head


# 3.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBST(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return isBST(root.left, min_val, root.val) and isBST(root.right, root.val, max_val)

def find_min(root):
    if not root:
        return float('inf')
    return min(root.val, find_min(root.left), find_min(root.right))

def find_max(root):
    if not root:
        return float('-inf')
    return max(root.val, find_max(root.left), find_max(root.right))

def find_sum(root):
    if not root:
        return 0
    return root.val + find_sum(root.left) + find_sum(root.right)


# 4.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isBST(self):
        stack = []
        prev_val = float('-inf')
        current = self

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if current.val <= prev_val:
                return False
            
            prev_val = current.val
            current = current.right

        return True

