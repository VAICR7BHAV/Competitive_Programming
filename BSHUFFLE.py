from sys import stdin,stdout
import random
def randomize(arr, n):
    for i in range(n - 1, -1, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
n=int(stdin.readline())
A=[int(i) for i in range(1,n+1)]
A=randomize(A,n)
for i in  range(0,n):
    stdout.write(str(A[i])+' ')
print()
A=randomize(A,n)
for i in  range(0,n):
    print(A[i],end=' ')