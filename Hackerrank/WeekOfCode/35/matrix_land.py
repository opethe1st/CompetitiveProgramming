class Solution:

    def __init__(self, arr):
        n, m = len(arr), len(arr[0])
        self.arr = arr
        self.values = {m*i+j: arr[i][j] for i in range(n) for j in range(m)}
        self.visitedEdge = set()
        self.visitedNode = [False for i in range(n*m)]
        self.ans = -float('inf')

    def _in_last_row(self, node):
        n = len(self.arr)
        m = len(self.arr[0])
        if (n-1)*m <= node < n*m:
            return True
        else:
            return False

    def _buildGraph(self):
        arr = self.arr
        n = len(self.arr)
        m = len(self.arr[0])
        G = [[] for i in range(n*m+1)]
        for i in range(n):
            for j in range(m):
                G[i*m + j].append(i*m + j-1) if j > 0 else None
                G[i*m + j].append((i+1)*m + j) if i < n-1 else None
                G[i*m + j].append(i*m + j+1) if j < m-1 else None
        for i in range(m):
            G[n*m].append(i)
        self.values[n*m] = 0
        self.visitedNode.append(False)
        # print(G)
        # print(G, self.values, self.visitedNode)
        return G

    def dfs(self, G, u, s, path=''):
        print(path)
        s += self.values[u] if not self.visitedNode[u] else 0
        self.visitedNode[u] +=1
        if self._in_last_row(u):
            # print('s',s, self.ans)
            self.ans = max(self.ans, s)
        for v in G[u]:  # pylint: disable=C0103
            if self.visitedNode[v] < 2:
                self.dfs(G, v, s, path=path+'{} '.format(u))
        # s -= self.values[u] if self.visitedNode[u] == 2 else 0
        self.visitedNode[u] -=1

    def maxans(self):
        graph = self._buildGraph()
        u = len(self.arr)*len(self.arr[0])  
        self.dfs(G=graph, u=u, s=0)
        return self.ans

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    Arr = []
    for i in range(n):
        Arr.append(list(map(int, input().split())))
    solution = Solution(arr=Arr)
    print(solution.maxans())
