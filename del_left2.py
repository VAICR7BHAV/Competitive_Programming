s=input()
t=input()
S=list(s)
T=list(t)
lens=len(s)
lent=len(t)
ma=max(lens,lent)
count=0
for i in range(0,ma):
    try:
        if(S[len(S)-1]==T[len(T)-1]):
            count+=1
            del(S[len(S)-1])
            del(T[len(T)-1])
        else:
            break
    except:
        break
print(len(S)+len(T))