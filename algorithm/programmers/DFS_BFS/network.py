def dfs(n,computers,com,visited):
    visited[com]=True
    for connect in range(n):
        if connect != com and computers[com][connect]==1:
            if visited[connect]==False:
                dfs(n,computers,connect,visited)

def solution(n, computers):
    answer = 0
    visited=[False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            dfs(n,computers,i,visited)
            answer+=1

    return answer