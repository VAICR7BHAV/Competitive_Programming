A=[int(i) for i in input().split()]
K=2
count=[]
start=[]
end=[]
for i in range(0,len(A)):
    star=max(0,i-K)
    en=min(len(A),i+K)
    start.append(star)
    end.append(en)
    '''
    arr=A[star:en+1]
    print(arr)
    num=0
    for j in range(0,len(arr)):
        if(arr[j]<=A[i]):
            num+=1
    count.append(num)
    '''
#print(count)
print(start)
print(end)
for j in range(0,len(start)):
    arr=A[start[j]:end[j]+1]
    num=0
    for k in range(0, len(arr)):
        if (arr[k] <= A[j]):
            num += 1
    count.append(num)
print(count)
numbers_can_be_used=max(count)-1
if(numbers_can_be_used==0):
    numbers_can_be_used=1
print(numbers_can_be_used)
B=[]
for i in range(0,len(A),numbers_can_be_used):
    arr=(A[i:i+numbers_can_be_used])
    val_dict={}
    C=list(set(arr))
    C.sort()
    '''
    for j in range(0,numbers_can_be_used):
        val_dict[C[j]]=j+1
    '''
    for j in range(0,len(C)):
            val_dict[C[j]]=j+1
    for j in range(0,len(arr)):
        B.append(val_dict[arr[j]])
print(B)