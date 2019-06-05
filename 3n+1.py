arr=[0]*100
def f(n):
    count=0
    while(n!=1):
        if(arr[n]!=0):
            count+=arr[n]
            break
        count+=1
        if(n%2!=0):
            n=3*n+1
        else:
            n=n//2
    return count
print(f(7))