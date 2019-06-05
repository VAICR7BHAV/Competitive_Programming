import time
a=[i for i in range(1,11)]
print(a)
arr=[[0 for i in range(10)]for j in range(10)]
for i in range(0,10):
    ad=a[i]
    for j in range(i,10):
        ad=ad&a[j]
    arr[i][j]=ad
print(arr)