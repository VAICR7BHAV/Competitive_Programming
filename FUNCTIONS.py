from collections import Counter
#THIS FUNCTION TAKES IN A NUMBER AS INPUT AND RETURN THE SUM OF ITS DIGITS
def digsum(a):
	sum=0
	A=str(a)
	for i in range(0,len(A)):
		sum=sum+int(A[i])
	return sum


#THIS FUNCTION TAKES IN BINARY STRING AS INPUT AND RETURN THE DECIMAL VALUE


def binarytodecimal(s):
    c=int(a,2)
    return c
#THIS FUNCTION TAKES IN AN INTEGER AND RETURN ITS EQUIVALENT BINARY STRING
def decimaltobinary(n):
    b=bin(n)[2:]
    return b
n=int(input())
print(decimaltobinary(n))