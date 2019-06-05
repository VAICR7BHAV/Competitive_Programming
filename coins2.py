import bisect

import math
def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = int(l + (r - l) / 2)

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1
n,q=map(int,input().split())
A=[int(i) for i in input().split()]
A.sort()
for i in range(0,q):
    v=int(input())
    b=bin(v)[2:]
    b=b[::-1]
    cond=True
    ans=0
    for j in range(0,len(b)):
        if(b[j]=='1'):
            val=int(math.pow(2,j))
            pos=binarySearch(A, 0, len(A)-1, val)
            if(pos==-1):
                ans=-1
                cond=False
                break
            else:
                ans+=1
                cond=True
    print(ans)

