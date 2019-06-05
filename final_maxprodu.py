from sys import stdin,stdout
def arr(n,k):
    if (k % 2 != 0):
        rem = n % k
        quo = n // k
        x = [quo] * k
        count = 0
        i = 0
        np = k // 2
        while (count != np):
            x[i] = x[i] - (count + 1)
            x[i + 1] = x[i + 1] + (count + 1)
            count += 1
            i += 2
        x.sort()
        if (rem == 1):
            x[k - 1] += 1
        elif (rem != 0):
            diff = rem
            x[k - 1] += 1
            diff -= 1
            i = k - 2
            x.sort()
            while (diff != 0):
                x[i] += 1
                i -= 1
                diff -= 1
        return (x)
    else:
        rem = n % k
        quo = n // k
        x = [quo] * k
        if (rem >= k // 2):
            np = k // 2
            npa = np
            if (np % 2 == 0):
                npa -= 1
            '''
            if(rem+quo<k+npa):
                count=0
                i=0
                while(count!=np-1):
                   x[i]=x[i]-(count+1)
                   x[i+1]=x[i+1]+(count+1)
                   count+=1
                   i+=2
                x[k-1]+=rem
            else:
                count = 0
                i = 0
                while (count != np - 1):
                    x[i] = x[i] - (count + 1)
                    x[i + 1] = x[i + 1] + (count + 1)
                    count += 1
                    i += 2
                temp=x[k-1]
                x[k-1]=k+npa-1
                diff=x[k-1]-temp
                rem-=diff
                x.sort()
                for g in range(k-2,k-2-rem,-1):
                    x[g]+=1
                    rem-=1
                print(x)
            '''
            count = 0
            i = 0
            while (count != np - 1):
                x[i] = x[i] - (count + 1)
                x[i + 1] = x[i + 1] + (count + 1)
                count += 1
                i += 2
            if (rem == k // 2 or rem == (k // 2 + 1)):
                x[k - 1] += rem
            else:
                temp = x[k - 1]
                x[k - 1] += k // 2 + 1
                diff = x[k - 1] - temp
                x.sort()
                diff = rem - diff
                pos = k - 2
                while (diff != 0):
                    x[pos] += 1
                    diff -= 1
                    pos -= 1
        else:
            count = 0
            i = 0
            np = k // 2
            while (count != np):
                x[i] = x[i] - (count + 1)
                x[i + 1] = x[i + 1] + (count + 1)
                count += 1
                i += 2
            i = 0
            diff = rem
            while (diff != 0):
                x[i] += 1
                i += 2
                diff -= 1
        return (x)
def prod(arr):
    mod = 1000000007
    p = 1
    for j in range(0, len(arr)):
        p = (p * arr[j] * (arr[j] - 1)) % 1000000007
    return p
t=int(stdin.readline())
while(t>0):
    n,k=map(int,stdin.readline().split())
    x=arr(n,k)
    #print(x)
    x.sort()
    ans=-1
    if(x[0]<=0):
        ans=-1
    elif(x[0]==1):
        ans=0
    else:
        ans=prod(x)
    stdout.write(str(ans)+'\n')
    t-=1