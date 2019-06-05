def BFS_FOR_UNDIRECTED_GRPAH_USING_ADJACENCY_MATRIX(graph,start):
    visited=[False]*len(graph)
    queue=[]
    queue.append(start)
    BFS=[]
    while(len(queue)!=0):
        v=queue[0]
        del queue[0]
        if(visited[v]==False):
            BFS.append(v)
        if(visited[v]==False):
            visited[v]=True
            for i in range(0,len(graph[v])):
                if(graph[v][i]==1):
                    queue.append(i)
    return BFS
def DFS_FOR_UNDIRECTED_GRPAH_USING_ADJACENCY_MATRIX(graph,start):
    visited=[False]*len(graph)
    stack=[]
    stack.append(start)
    DFS=[]
    while(len(stack)!=0):
        v=stack.pop()
        if(visited[v]==False):
            DFS.append(v)
        if(visited[v]==False):
            visited[v]=True
            for i in range(0,len(graph[v])):
                if(graph[v][i]==1):
                    stack.append(i)
    return DFS
def BFS_FOR_UNDIRECTED_GRAPH_USING_ADJACENCY_LIST(graph,start):
    visited = [False] * len(graph)
    queue = []
    queue.append(start)
    BFS = []
    while (len(queue) != 0):
        v = queue[0]
        del queue[0]
        if (visited[v] == False):
            BFS.append(v)
        if (visited[v] == False):
            visited[v] = True
            for i in range(0, len(graph[v])):
                queue.append(graph[v][i])
    return BFS
def DFS_FOR_UNDIRECTED_GRPAH_USING_ADJACENCY_LIST(graph,start):
    visited=[False]*len(graph)
    stack=[]
    stack.append(start)
    DFS=[]
    while(len(stack)!=0):
        print(stack)
        v=stack.pop()
        if(visited[v]==False):
            DFS.append(v)
        if(visited[v]==False):
            visited[v]=True
            for i in range(0,len(graph[v])):
                stack.append(graph[v][i])
    return DFS
def path_using_DFS(graph,start,end):
    visited=[False]*len(graph)
    stack=[]
    stack.append(start)
    path=[]
    while(len(stack)!=0):
        v=stack.pop()
        if(visited[v]==False):
            path.append(v)
        if(v==end):
            break
        if (visited[v] == False):
            visited[v] = True
            for i in range(0, len(graph[v])):
                stack.append(graph[v][i])
    return path
def path_using_BFS(graph,start,end):
    visited = [False] * len(graph)
    queue = []
    queue.append(start)
    BFS = []
    while (len(queue) != 0):
        v = queue[0]
        del queue[0]
        if (visited[v] == False):
            BFS.append(v)
        if(v==end):
            break
        if (visited[v] == False):
            visited[v] = True
            for i in range(0, len(graph[v])):
                queue.append(graph[v][i])
    return BFS
graph=[[0 for x in range(6)]for y in range(6)]
graph[0][1]=1
graph[0][2]=1
graph[1][3]=1
graph[1][4]=1
graph[2][4]=1
graph[3][4]=1
graph[3][5]=1
graph[4][5]=1
graph[1][0]=1
graph[2][0]=1
graph[3][1]=1
graph[4][1]=1
graph[4][2]=1
graph[4][3]=1
graph[5][3]=1
graph[5][4]=1
for i in range(0,len(graph)):
    print("Neighbour of ",i,"is",end=' ')
    for j in range(0,len(graph[i])):
        if(graph[i][j]==1):
            print(j,end=' ')
    print()
    '''
graph2=[[]for x in range(5)]
print(graph2)
print("Enter 7 edges")
for i in range(0,7):
    a1,a2=map(int ,input().split())
    graph2[a1].append(a2)
    graph2[a2].append(a1)
print(graph2)
'''
graph2=[[1,2],[2],[0,3],[3]]

print(DFS_FOR_UNDIRECTED_GRPAH_USING_ADJACENCY_LIST(graph2,0))
