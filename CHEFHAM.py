from collections import Counter
from itertools import permutations
import random
from sys import stdin,stdout

def check(A,B,n):
    for i in range(0,n):
        if(A[i]==B[i]):
            return False
    return True
def randomize(arr, n):
    for i in range(n - 1, -1, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
def unique_A(A,n):
    if (n != 1):
        print(n)
    else:
        print(0)
    B = []
    for i in range(n - 1, -1, -1):
        B.append(A[i])
    if (n % 2 != 0 and n != 1 and A[(n - 1) // 2] == B[(n - 1) // 2]):
        B[(n - 1) // 2], B[((n - 1) // 2) + 1] = B[((n - 1) // 2) + 1], B[(n - 1) // 2]
    for i in range(0, len(B)):
        print(B[i], end=' ')
def n3(A,n):
    B=[0]*3
    print(2)
    if(A[0]==A[1]):
        B[1]=A[2]
        B[0]=A[1]
        B[2]=A[0]
    elif(A[1]==A[2]):
        B[0]=A[2]
        B[2]=A[0]
        B[1]=A[1]
    elif(A[0]==A[2]):
        B[1]=A[0]
        B[0]=A[1]
        B[2]=A[2]
    for i in range(0, len(B)):
        print(B[i], end=' ')
def one_shift(A,B,n):
    temp=B[0]
    for i in range(0,n-1):
        B[i]=B[i+1]
    B[n-1]=temp
def one_swap(A,B,n):
    for i in range(0,n-1):
        B[i],B[i+1]=B[i+1],B[i]
t=int(input())
for k in range(0,t):
    n=int(input())
    A=[int(i) for i in input().split()]
    d1=Counter(A)
    li=list(d1.values())
    l2=list(d1.keys())
    if(len(li)==n):
        unique_A(A,n)
    elif(n==3):
        n3(A,n)
    elif(n==2):
        print(0)
        for i in range(0,len(A)):
            print(A[i],end=' ')
    else:
        B=[]
        print(n)
        for i in range(n-1,-1,-1):
            B.append(A[i])
        if (check(A, B, n)):
            for i in range(0, len((B))):
                print(B[i], end=' ')
            continue
        if (n % 2 != 0 and n != 1 and A[(n - 1) // 2] == B[(n - 1) // 2]):
            B[(n - 1) // 2], B[((n - 1) // 2) + 1] = B[((n - 1) // 2) + 1], B[(n - 1) // 2]
        if(check(A,B,n)):
            for i in range(0, len((B))):
                print(B[i], end=' ')
            continue
        else:
            B=randomize(B,n)
            while(check(A,B,n)!=True):
                randomize(B,n)
                #print(B,check(A,B,n))
        #print(B)
        for i in range(0,len((B))):
            print(B[i],end=' ')