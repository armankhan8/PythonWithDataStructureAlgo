visited = [0] * 7
adj = [
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0]
]

def DFS(i):
    print(i, end=" ")
    visited[i] = 1
    
    for j in range(7):
        if adj[i][j] == 1 and not visited[j]:
            DFS(j)

# Main function
if __name__ == "__main__":
    DFS(0)
