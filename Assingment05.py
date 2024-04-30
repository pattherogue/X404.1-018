1.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_last_item(root):
    if not root:
        return None
    
    queue = [root]
    last_node = None
    while queue:
        node = queue.pop(0)
        last_node = node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return last_node.value


2.
import heapq
from collections import Counter

def sort_by_frequency(s):
    freq_map = Counter(s)
    max_heap = [(-freq, char) for char, freq in freq_map.items()]
    heapq.heapify(max_heap)
    sorted_chars = []
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        sorted_chars.append(char)
    return sorted_chars


3.
def longest_common_prefix(words):
    if not words:
        return ""
    prefix = words[0]
    for word in words[1:]:
        i = 0
        while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
            i += 1
        prefix = prefix[:i]
    return prefix


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

def shortest_unique_prefix(words):
    root = TrieNode()
    for word in words:
        insert_word(root, word)
    
    prefixes = []
    for word in words:
        node = root
        prefix = ""
        for char in word:
            prefix += char
            if node.children[char].count == 1:
                break
            node = node.children[char]
        prefixes.append(prefix)
    return prefixes

