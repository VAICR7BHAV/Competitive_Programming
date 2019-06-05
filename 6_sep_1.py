from sys import stdin,stdout
lines=stdin.read().splitlines()
for i in range(0,len(lines)):
    if(int(lines[i])!=42):
        print(lines[i])
    else:
        break