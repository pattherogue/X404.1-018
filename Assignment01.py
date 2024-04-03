'''
1. 

O(1) - Constant Time
Turning on a light switch. Doesnt matter how big the room is or how many switches; flipping the switch itself takes the same amount of time.

O(log n) - Logarithmic Time
Guessing a number between 1 and 100. If you know that it is higher or lower after each guess, you can narrow down the possibilities by half each time. 
More efficiency than guessing one at a time. 

O(n) - Linear Time
Counting the number of students in a classroom by name one by one then adding them up. Time increases linearly in accordance to the number of students.

O(n log n) - Linearithmic Time
Sorting a collection of marbles by color. Divide marbles into groups based on color, sort each group, then put back together.
As you add more marbles, it may take longer to sort, but easier than comparing each marble to every other one. 

O(n^2) - Quadratic Time
Counting the total number of stickers on a sheet where each row and column has one sticker. If 3 x 3, you need 3 stickers for first row, 3 for second row, and 3 for third row, total 9 stickers. 
The total number of stickers counted grows quadratically with size of sheet. 


'''

# 2.

import random
#function that takes in argument "n"
def populate_and_shuffle(n):
    #list containing numbers from 0 to n-1
    arr = [i for i in range(n)]
    #loop through each index of list
    for i in range(n):
        #generate random index from i to n-1
        rand_index = random.randomint(i, n-1)
        #swap values
        arr[i], arr[rand_index] = arr[rand_index], arr[i]
    #return shuffled list
    return arr

'''
Big O notation
    Average: O(n)
    Worst Case: O(n)
'''

# 3.

def count_occurence(arr, target):
    #function to find leftmost index of target value
    def leftmost_index(arr, target):
        #initialze variables 
        left = 0
        right = len(arr) - 1
        result = -1

        #binary search to find leftmost index
        while left <= right:
            mid = (left + right) // 2
            #if midle elemnt is greater than or equal to target, move left subarray
            if arr[mid] >= target:
                right = mid - 1
            else:
                #otherwise move to the right subarray
                left = mid + 1

            #if leftmost index is within array and elemnt at index is target
            #update result value with leftmost index
            if left < len(arr) and arr[left] == target:
                result = left

            return result
    
    #functon to find rightmost index of target value
    def rightmost_index(arr, target):
        #initialize variables
        left = 0
        right = len(arr) - 1
        result = -1

        #binary search to find rightmost index
        while left <= right:
            mid = (left + right) // 2
            #if middle element less than or equal to target, move to right subarray
            if arr[mid] <= target:
                left = mid + 1
            else:
                #otherwise move to left subarray
                right = mid - 1

            #if rightmost index is within array and element at index is target
            #update result with rightmost index
            if right >= 0 and arr[right] == target:
                result = right 
            
            return result
        
        #find leftmost and rightmost indices of target
        left_index = leftmost_index(arr, target)
        right_index = rightmost_index(arr, target)

        #if neither is found, return 0
        if left_index == -1 or right_index == -1:
            return 0
        
        #otherwise retun count of occurence
        return right_index - left_index + 1
    
    '''
    Time Complexity: O(log n) 
    '''