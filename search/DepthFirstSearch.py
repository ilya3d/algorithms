# DFS - DepthFirstSearch
# поиск цикла алгоритмом поиска в глубину
n = 7
m = 6
w = [
    ['A', 'A', 'A', 'A', 'A', 'B'],
    ['A', 'B', 'B', 'B', 'A', 'B'],
    ['A', 'B', 'A', 'A', 'A', 'B'],
    ['A', 'B', 'A', 'B', 'B', 'B'],
    ['A', 'B', 'A', 'A', 'A', 'B'],
    ['A', 'B', 'B', 'B', 'A', 'B'],
    ['A', 'A', 'A', 'A', 'A', 'B'],
]

s = [[0 for j in range(m)] for i in range(n)]


def dfs(x, y, mt):
    s[x][y] = mt
    sm = w[x][y]
    mt += 1
    if y < m-1 and sm == w[x][y+1]:
        if s[x][y+1] == 0:
            if dfs(x, y+1, mt):
                return True
        elif mt - s[x][y+1] > 3:
            return True
    if y > 0 and sm == w[x][y-1]:
        if s[x][y-1] == 0:
            if dfs(x, y-1, mt):
                return True
        elif mt - s[x][y-1] > 3:
            return True
    if x < n-1 and sm == w[x+1][y]:
        if s[x+1][y] == 0:
            if dfs(x+1, y, mt):
                return True
        elif mt - s[x+1][y] > 3:
            return True
    if x > 0 and sm == w[x-1][y]:
        if s[x-1][y] == 0:
            if dfs(x-1, y, mt):
                return True
        elif mt - s[x-1][y] > 3:
            return True
    s[x][y] = 0
    w[x][y] = '.'
    return False


f = False
for i in range(n):
    for j in range(m):
        if 'A' <= w[i][j] <= 'Z':
            if dfs(i, j, 1):
                f = True
                break


print('Yes' if f else 'No')
