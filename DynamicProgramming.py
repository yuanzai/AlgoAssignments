"""
You are given an array D of n coin denomination values d1 < d2 < … < dn, where each di is a positive integer, and a positive integer A. You have an unlimited number of coins of each denomination. Assume d1 = 1, so you can always make change for any amount of money A. Give an efficient dynamic programming program that, given A and D, makes change for A using the minimum number of coins with denominations from D. 
"""

def denominate(D,v):
    # array to store results for each value v, ie min coins for each 1 to v
    # values are initialised with v as thats the maximum number possible for value v
    R = [v] * (v+1)

    #coin distribution array, for logging the coins need to form the minimum as per R
    c = [[0 for x in range(len(D))] for x in range(v+1)]

    #loop through each coin and each value to get the minimum for each value starting with the lowest coin
    for coin in range(len(D)):
        for i in range(1, v+1):
            # case where coin value is the same as v
            if i == D[coin]:
                # coin require is 1
                R[i] = 1
                # get coins from base case v = 0
                c[i] = c[i-D[coin]][:]
                # set coin need to 1
                c[i][coin] = 1
            # case where value is greater than coin value
            elif i > D[coin]:
                # compare the current minimum (based on not having the current coin value)
                # with having to add the current coin value to get the min of (value - coin value)
                if R[i] >= 1+R[i-D[coin]]:
                    # get the coin distribution needed for (v - coin value)
                    c[i] = c[i-D[coin]][:]
                    # increment coin needed for this coin value  by 1
                    c[i][coin] += 1
                    # record new min coins required for value i
                    R[i] = 1 + R[i-D[coin]]
    print " ".join(map(str,c[v]))

while True:
    try:
        D = map(int, raw_input().split(" "))
        v = int(raw_input())
        denominate(D,v)
    except EOFError:
        break

