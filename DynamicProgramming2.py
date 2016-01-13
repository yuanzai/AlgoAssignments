"""
Suppose you are given an n × n bitmap, represented by a matrix M[1 .. n, 1 .. n] whose entries are zeros and ones. A solid square block is a submatrix of the form M[i .. i′, j .. j′] in which every bit is equal to 1, i.e., a square submatrix with all 1s. You wish to find the size of the largest solid square block in M.
"""

def largestSquare(M, n):
    # results 2d array
    # extra column and row created as base cases 
    R = [[0 for i in range(0, n+1)] for i in range(0,n+1)]
    # variables to record max, as well as i and j where max occurred
    current_max = 0
    x = 0
    y = 0

    # start from bottom right most corner of the matrix
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            # if entry is zero, resulting max square length is also zero
            if M[i][j] == 0:
                R[i][j] = 0
            else:
                # otherwise, if entry is one,
                # consider 3 adjacent inputs, bottom, right, and bottom right result
                # take the min length value and increment by 1
                R[i][j] = min(R[i+1][j], R[i][j+1], R[i+1][j+1]) +1
                # if the current maximum has been redefined, get the i,j values as well
                if R[i][j] >= current_max:
                    current_max = R[i][j]
                    x = i
                    y = j
    return current_max, x+1, y+1

while True:
    try:
        n = int(raw_input())
        if n == 0:
            break
        M = []
        for _ in range(0,n):
            M.append(map(int, raw_input().split(" ")))
        current_max, x,y = largestSquare(M,n)
        print current_max
        print str(x) + " " + str(y)
    except EOFError:
        break
