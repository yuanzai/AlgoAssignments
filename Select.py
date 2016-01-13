"""
Given an unsorted array A[1.. n] of n distinct integers and a positive integer k ≤ n, give a program that takes expected O(n) time on all inputs which determines the k numbers in A that are closest in value (not closest in position) to the median of A. Note: The O(n) bound does not depend on k; e.g., running an O(n) time algorithm k times results in an O(nk) time algorithm, not an O(n) time algorithm. You may use the following test data for this problem: readme   input   output. Also note that since order does not matter for this problem and there may be ties, your output may still be correct even if it does not match the sample output perfectly.

"""

import sys
import random

def kClosestToMedian(A, k):
    # length of array
    n = len(A)
    # median of array determined by Randomised Select 
    m = Randomised_Select(A,0,n-1,(n+1)/2)
    
    # Create an array of the absolute difference between each element and the median
    difference_Array = []
    for i in A:
        difference_Array.append(abs(i-m))
    
    # Use randomise select to pick out the kth element from the array of absolute differences
    # The kth element is the difference of between the median of the original array and
    # the smallest or largest element of the elements of that are k closest to the median# 
    difference_of_k = Randomised_Select(difference_Array,0,n-1,k)
    result = []
    max_diff_result = []
    
    # determine all the elements that have a difference of less than the value found above and
    # defined as 'difference_of_k'
   
    for i in A:
        if abs(i-m) < difference_of_k:
            result.append(i)
        elif abs(i-m) == difference_of_k:
            # A second list is used to keep track of the elements with the maximum difference to
            # to avoid getting k+1 elements due to 2 elements having the same maximum difference.
            # ie one below the median and the other above it
            max_diff_result.append(i)
    # Add the max difference element back in depending on what k is required and how many of such elements
    # were found
    if len(result) == k - 2:
        result.extend(max_diff_result)
    else:
        result.append(max_diff_result[0])

    return result

def Randomised_Select(A,p,r,i):
    # end procedure when subarray are of length 1, ie ith element found
    if p == r:
        return A[p]
    # partition array using randomise partition
    q, A_partitioned = Randomised_Partition(A,p,r)
    # determine offset to use for subarray greater than pivot
    # offset used to adjust i as subarray is now starting from k+1 position of original array
    k = q - p + 1
    # if i == k, ie pivot is ith element since element at kth position of array is in place
    if i == k:
        return A_partitioned[q]

    # else recursively select from either subarray depending of whether ith element is before or 
    # after current pivot element position.
    elif i < k:
        return Randomised_Select(A_partitioned, p, q-1, i)
    else:
        return Randomised_Select(A_partitioned, q+1, r, i-k)

def Randomised_Partition(A,p,r):
    # picking out the random element to be used as a pivot in the partition procedure
    rand = random.randint(p,r)
    temp = A[rand]
    A[rand] = A[r]
    A[r] = temp
    
    #Regular partition procedure
    # Detemine the pivot
    x = A[r]
    # i is the position of elements smaller  than the pivot
    i = p -1
    for j in range(p, r):
        # swaps elements smaller or equal to pivot to i, which was the first position of 
        # elements greater than the pivot
        if A[j] <= x:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    # final swap pivot from the end of list with first position of elements greater than pivot
    # resultant list has subarray of smaller than pivot, pivot andsubarray of greater than pivot in that order
    temp = A[i+1]
    A[i + 1] = A[r]
    A[r] = temp
    return i+1, A


A=map(int, raw_input().split(" "))
k = int(raw_input())
print " ".join(map(str, kClosestToMedian(A,k)))
