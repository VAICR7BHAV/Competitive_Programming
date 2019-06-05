def binarySearch(arr, l, r, x):
    while l <= r:

        mid = l + (r - l) / 2;

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

            # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1
arr=[i for i in range(10)]
print(arr)
val=9
ll=0
ul=9
while(ll<=ul):
    mid = ll + (ul - ll) // 2
    if(arr[mid]==val):
        print("found")
        break
    elif(arr[mid]<val):
        ll=mid+1
    elif(arr[mid]>val):
        ul=mid-1