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
            #if midle elemnt is greater than or equal to target, move left side
            if arr[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1