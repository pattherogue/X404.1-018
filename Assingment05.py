1.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_last_item(root):
    if not root:
        return None
    
    queue = [root]
    last_item = None
    
    while queue:
        node = queue.pop(0)
        last_item = node.val
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return last_item


2.
import heapq
def frequency_sort(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    
    heap = [(-freq, char) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    sorted_chars = []
    while heap:
        freq, char = heapq.heappop(heap)
        sorted_chars.append(char)
    
    return sorted_chars


3.
def longest_common_prefix(words):
    if not words:
        return ""
    
    min_word = min(words)
    max_word = max(words)
    
    for i, char in enumerate(min_word):
        if char != max_word[i]:
            return min_word[:i]
    
    return min_word


4.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def insert_word(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
        node.count += 1

def find_shortest_prefix(words):
    root = TrieNode()
    prefixes = []
    for word in words:
        insert_word(root, word)
    
    for word in words:
        prefix = ""
        node = root
        for char in word:
            prefix += char
            node = node.children[char]
            if node.count == 1:
                break
        prefixes.append(prefix)
    
    return prefixes

