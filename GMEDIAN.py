from sys import stdout,stdin
import bisect
def median(arr):
    l=len(arr)
    arr.sort()
    med=0
    if(l%2==0):
        med=(arr[l//2]+arr[l//2-1])/2
    else:
        med=arr[l//2]
    if(int(med)==med):
        med=int(med)
    pos=bisect.bisect_right(arr,med)
    print(arr,med)
    if(arr[pos-1]==med):
        return True
    else:
        return False
t=int(stdin.readline())
while(t>0):
    N=int(stdin.readline())
    count=0
    A=[int(i) for i in stdin.readline().split()]
    for i in range(0,N):
        for j in range(i+1,N+1):
            arr=(A[i:j])
            if(median(arr)):
                count+=1
    print(count)
    t-=1