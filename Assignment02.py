'''
Give at least two examples (in real life and in programming) and a short description for:
Stacks: 

Real Life Example: Stack of Plates
Description: Imagine stacking plates on top of each other. To take a plate, you remove the one on top first.

Programming Example: Browser History
Description: When you click the back button in your web browser, it takes you to the last page you visited. This works like a stack, with each page you visit being added to the top of the stack.

Queues

Real Life Example: Supermarket Checkout Line
Description: Picture standing in line at the supermarket. The person who joins first gets served first. It's like a line that moves in order.

Programming Example: Printer Queue
Description: When you print something, it goes into a queue. The first thing you sent to the printer gets printed first, just like waiting in line.

Deques
Real Life Example: Line at an Amusement Park
Description: Think about lining up for a roller coaster. You can enter and leave the line from either end, like a flexible queue.

Programming Example: Task Scheduler
Description: Imagine a list of tasks you need to do. A deque lets you add tasks to the front or back and remove them from either end, so you can manage your tasks in a flexible way.
'''

# 2.
def is_balanced(string):
    # Initialize an empty stack to track opening braces
    stack = []
    
    # Define sets of opening and closing braces
    opening_braces = "({["
    closing_braces = ")}]"
    
    # Define a dictionary mapping opening braces to their corresponding closing braces
    brace_pairs = {"(": ")", "{": "}", "[": "]"}
    
    # Iterate through each character in the string
    for char in string:
        # If the character is an opening brace, push it onto the stack
        if char in opening_braces:
            stack.append(char)
        # If the character is a closing brace
        elif char in closing_braces:
            # If the stack is empty or the top of the stack does not match the corresponding closing brace
            if not stack or brace_pairs[stack.pop()] != char:
                # The braces are not balanced, return False
                return False
    
    # If the stack is empty, all braces are balanced, return True; otherwise, return False
    return len(stack) == 0


# 3. 
class Deque:
    def __init__(self):
        # Initialize an empty list to store elements of the deque
        self.deque = []

    def append_left(self, element):
        # Add the specified element to the left end of the deque
        self.deque.insert(0, element)

    def append_right(self, element):
        # Add the specified element to the right end of the deque
        self.deque.append(element)

    def pop_left(self):
        # Remove and return the element from the left end of the deque
        if not self.is_empty():
            return self.deque.pop(0)
        else:
            # Print a message if the deque is empty and return None
            print("Deque is empty.")
            return None

    def pop_right(self):
        # Remove and return the element from the right end of the deque
        if not self.is_empty():
            return self.deque.pop()
        else:
            # Print a message if the deque is empty and return None
            print("Deque is empty.")
            return None

    def peek_left(self):
        # Return the element from the left end of the deque without removing it
        if not self.is_empty():
            return self.deque[0]
        else:
            # Print a message if the deque is empty and return None
            print("Deque is empty.")
            return None

    def peek_right(self):
        # Return the element from the right end of the deque without removing it
        if not self.is_empty():
            return self.deque[-1]
        else:
            # Print a message if the deque is empty and return None
            print("Deque is empty.")
            return None

    def get_count(self):
        # Return the number of elements in the deque
        return len(self.deque)

    def is_empty(self):
        # Check if the deque is empty and return True or False accordingly
        return len(self.deque) == 0

    def print_deque(self):
        # Print the contents of the deque
        print("Deque Contents:", self.deque)


# 4.
def binary_search(arr, low, high, target):
    if high >= low:
        mid = (low + high) // 2

        # If element is present at the middle itself
        if arr[mid] == target:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, target)

    else:
        # Element is not present in array
        return -1

