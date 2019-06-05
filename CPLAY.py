from sys import stdin
def decider(teamA,teamB,s):
    ans=''
    kick=0
    v1={}
    for i in range(0,len(s)):
        if(i%2==0):
            teamA.append(int(s[i]))
        else:
            teamB.append(int(s[i]))
    if(sum(teamA[0:5])>sum(teamB[0:5])):
        ans='A'
        kick=10
    elif(sum(teamB[0:5])>sum(teamA[0:5])):
        ans='B'
        kick=10
    else:
        if(teamA[5]==1 and teamB[5]==0):
            ans='A'
            kick=12
        elif(teamA[5]==0 and teamB[5]==1):
            ans='B'
            kick=12
        else:
            if(teamA[6]==1 and teamB[6]==0):
                ans='A'
                kick=14
            elif(teamA[6] == 0 and teamB[6] == 1):
                ans='B'
                kick=14
            else:
                if(teamA[7]==1 and teamB[7]==0):
                    ans='A'
                    kick=16
                elif(teamB[7]==1 and teamA[7]==0):
                    ans='B'
                    kick=16
                else:
                    if(teamA[8]==1 and teamB[8]==0):
                        ans='A'
                        kick=18
                    elif(teamA[8]==0 and teamB[8]==1):
                        ans='B'
                        kick=18
                    else:
                        if(teamA[9]==1 and teamB[9]==0):
                            ans='A'
                            kick=20
                        elif(teamA[9]==0 and teamB[9]==1):
                            ans='B'
                            kick=20
                        else:
                            ans='T'
                            kick=20
    v1['W']=ans
    v1['K']=kick
    return(v1)
def decider2(A,B):
    scoreA=sum(A[0:3])
    scoreB=sum(B[0:3])
    ans=''
    kick=0
    v={}
    if(scoreA>scoreB+2):
        ans='A'
        kick=6
    elif(scoreA+2<scoreB):
        ans='B'
        kick=6
    else:
        if(A[3]==1):
            scoreA+=1
            if(scoreA>scoreB+2):
                ans='A'
                kick=7
            elif(scoreA+1<scoreB):
                ans='B'
                kick=7
        elif(A[3]==0):
            scoreA += 0
            if (scoreA > scoreB + 2):
                ans = 'A'
                kick = 7
            elif (scoreA + 1 < scoreB):
                ans = 'B'
                kick = 7
        elif(B[3]==1):
            scoreB+=1
            if(scoreB>scoreA+1):
                ans='B'
                kick=8
            elif(scoreA>scoreB+1):
                ans='A'
                kick=8
        elif (B[3] == 0):
            scoreB += 0
            if (scoreB > scoreA + 1):
                ans = 'B'
                kick = 8
            elif (scoreA > scoreB + 1):
                ans = 'A'
                kick = 8
        else:
            if(A[4]==1):
                scoreA+=1
                if(scoreA>scoreB+1):
                    ans='A'
                    kick=9
                elif(scoreA<scoreB):
                    ans='B'
                    kick=9
            elif(A[4]==0):
                scoreA += 0
                if (scoreA > scoreB + 1):
                    ans = 'A'
                    kick = 9
                elif (scoreA < scoreB):
                    ans = 'B'
                    kick = 9
            elif(B[4]==1):
                scoreB+=1
                if(scoreB>scoreA):
                    ans='B'
                    kick=10
                if(scoreA>scoreB):
                    ans='A'
                    kick=10
            elif (B[4] == 0):
                scoreB += 0
                if (scoreB > scoreA):
                    ans = 'B'
                    kick = 10
                if (scoreA > scoreB):
                    ans = 'A'
                    kick = 10
    v['W']=ans
    v['K']=kick
    return(v)
lines=stdin.read().splitlines()
for i in range(0,len(lines)):
    teamA=[]
    teamB=[]
    v=decider(teamA,teamB,lines[i])
    #print(teamA[0:5],teamB[0:5])
    if(v['K']==10):
        v1=decider2(teamA[0:5],teamB[0:5])
        v['W']=v1['W']
        v['K']=v1['K']
    if(v['W']=='A'):
        print("TEAM-A",v['K'])
    elif(v['W']=='B'):
        print("TEAM-B",v['K'])
    else:
        print("TIE")