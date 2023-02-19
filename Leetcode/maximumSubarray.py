# O(n^3) solution
# have i indicate the start of the array
# have j indicate the end of the subarray
# have k to calculate the sum of the subarray[i:j]


def maximumSubarray_n3 (arr):
    maximumSum = arr[0]
    currentSum = 0
    for i in  range (len (arr)):
        for j in range (i, len (arr)):
            for k in range (i, j):
                currentSum += arr[k]
                if currentSum > maximumSum:
                    maximumSum = currentSum
            currentSum = 0

    return maximumSum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print (maximumSubarray_n3 (arr))



# O(n^2) solution
# have i indicate the start of the subarray
# have j indicate the end of the subarray
# at every iteration of the i loop the currentSum will be set to 0
# to keep track of the currentSum of any given subarray[i:j]



def maximumSubarray_n2 (arr):
    maximumSum = arr[0]
    for i in range (len (arr)):
        currentSum = 0
        for j in range (i, len (arr)):
            currentSum += arr [j]
            if currentSum > maximumSum:
                maximumSum = currentSum

    return maximumSum

print (maximumSubarray_n2(arr))



# O(n) solution
# at every iteration we add the value to the currentSum
# if the value of individual element is higher than currentSum
# then we update the currentSum with the higher value of the individual
# element otherwise we keep currentSum as it is after adding the element
# then we check if the maximumSum is higher than the currentSum
# if not then we update maximumSum with the currentSum 


def maximumSubarray (arr):
    maximumSum = arr[0]
    currentSum = arr[0]


    for i in range (1, len (arr)):
        currentSum += arr[i]
        currentSum = max (currentSum, arr[i])
        maximumSum = max (maximumSum, currentSum)

    return maximumSum


print (maximumSubarray (arr))


