import sys
N,r=map(int,input().split())
for i in range(0,N):
    R=int(input())
    if(R>=r):
        print("Good boi")
    else:
        print("Bad boi\n")
    sys.stdout.flush()