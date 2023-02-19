# You are given an array of length n, and an integer value of x
# Find the average of the elements in the array using x
# Example:
#   [1, 2, 3, 4, 5] x = 3
# You should return another array [0, 0, 2, 3, 4]
# [1]/3 = 0 # bcz subarray isn't 3
# [1, 2] /3 = 0 #  bcz subarray isn't 3
# [1, 2, 3] / 3 = 2
# [2, 3, 4] / 3 = 3
# [3, 4, 5] / 3 = 4


# Design:
# Have 2 pointers i and j 
# Have a temp array of size n and initialize with 0
# i will iterate through the array one by one grabbing each element
# j will anchor at one position so that we can have a subarray [j:i]
# if subarray [j:i] == x then calculate the average and put them into temp[i]
# then increment j by 1  

def runningAvergae (arr, x):
    j = 0
    temp = [0] * len (arr)
    runningSum = 0
    for i in range (len (arr)):
        runningSum += arr[i]
        if (i - j) + 1 == x:
            temp[i] = runningSum / x
            runningSum -= arr[j]
            j += 1

    return temp


arr = [1, 2, 3, 4, 5, 6, 7, 9]
print (runningAvergae (arr, 3))


