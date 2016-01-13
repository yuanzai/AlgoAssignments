"""
An inversion in an array A[1.. n] is a pair of indices (i, j) such that i < j and A[i] > A[j]. 
The number of inversions in an n-element array is between 0 (if the array is sorted) and C(n, 2) (i.e., "n choose 2") (if the array is reverse-sorted). 
Let A[1.. n] be an array of n distinct real numbers. Give a divide-and-conquer program that counts the number of inversions in A using O(n log2 n) comparisons. (Hint: modify mergesort.) 
"""

import sys

def inversion(A, p, r):
    if p == r:
        return A, 0
    else:
        q = (p+r)/2
        array_result, count_left = inversion(A,p,q)
        array_result, count_right = inversion(array_result,q+1,r)
        array_result, count_merge = merge(array_result,p,q,r)
        return array_result, count_left + count_right + count_merge

def merge(A,p,q,r):
    result= []
    counter = 0
    i = 0
    j = 0
    left = A[p:q+1]
    right = A[q+1:r+1]
    length_left = len(left)
    while i < length_left and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            counter += length_left - i
            j+=1
    result = result + left[i:]
    result = result + right[j:]
    left_A = A[:p]
    result = left_A + result
    result = result + A[r+1:]
    return result, counter

input_file = sys.argv[1]
output_file = sys.argv[2]
f = open(input_file,"r")
w = open(output_file, "w")
for line in f:
    cleanedLine = line.strip()
    if cleanedLine: # is not empty
        array = map(int, cleanedLine.strip().split(" "))
        w.write(str(inversion(array,0,len(array)-1)[1]))
        w.write("\n")
f.close()
w.close()
