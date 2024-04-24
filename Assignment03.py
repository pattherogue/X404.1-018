'''
Bubble Sort:

Worst Case Data:
Description: Input array is in reverse sorted order.
Big O Notation: O(n^2)

Best Case Data:
Description: Input array is already sorted.
Big O Notation: O(n)

Selection Sort:

Worst Case Data:
Description: Same as the best case, as Selection Sort always performs the same number of comparisons and swaps regardless of input.
Big O Notation: O(n^2)

Best Case Data:
Description: Same as the worst case, as Selection Sort always performs the same number of comparisons and swaps regardless of input.
Big O Notation: O(n^2)

Insertion Sort:

Worst Case Data:
Description: Input array is in reverse sorted order.
Big O Notation: O(n^2)

Best Case Data:
Description: Input array is already sorted.
Big O Notation: O(n)

Merge Sort:

Worst Case Data:
Description: No matter the input, Merge Sort consistently performs with a time complexity of O(n log n).
Big O Notation: O(n log n)

Best Case Data:
Description: Same as the worst case, as Merge Sort consistently performs with a time complexity of O(n log n).
Big O Notation: O(n log n)

Quicksort:

Worst Case Data:
Description: When the pivot selection consistently results in unbalanced partitions, leading to O(n^2) time complexity.
Big O Notation: O(n^2)

Best Case Data:
Description: When the pivot selection consistently results in balanced partitions, leading to O(n log n) time complexity.
Big O Notation: O(n log n)

'''

2.
def insertion_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Traverse through the array starting from the second element
    for i in range(1, n):
        # Store the current element
        key = arr[i]
        # Move elements greater than 'key' to one position ahead
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Place key at its correct position in sorted subarray
        arr[j + 1] = key
    
    return arr

3.
def find_missing_numbers(arr):
    # Get the length of the array
    n = len(arr)
    # Initialize an empty list to store missing numbers
    missing_numbers = []
    # Initialize a boolean array to mark visited numbers
    visited = [False] * n
    
    # Mark visited numbers in the array
    for num in arr:
        # Check if the number is within the range
        if 0 <= num < n:
            # Mark the number as visited
            visited[num] = True
    
    # Iterate over the boolean array to find missing numbers
    for i in range(n):
        # If a number is not visited, it's missing
        if not visited[i]:
            missing_numbers.append(i)
    
    return missing_numbers

4.
def first_non_repeating_character(s):
    # Initialize a dictionary to store the count of each character
    char_count = {}
    
    # Iterate over the string and count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Iterate over the string again to find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
    
    # If no non-repeating character is found, return None
    return None

5.
def longest_subarray_with_sum(nums, target):
    # Initialize a dictionary to store the running sum and its corresponding index
    sum_index = {0: -1}
    max_length = 0
    current_sum = 0
    
    # Iterate over the array and update the running sum
    for i, num in enumerate(nums):
        current_sum += num
        
        # Check if the complement of the target exists in the dictionary
        complement = current_sum - target
        if complement in sum_index:
            max_length = max(max_length, i - sum_index[complement])
        
        # Update the dictionary with the current running sum and its index
        if current_sum not in sum_index:
            sum_index[current_sum] = i
    
    return max_length


