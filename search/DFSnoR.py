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

st = []

f = False
for i in range(n):
    for j in range(m):
        if 'A' <= w[i][j] <= 'Z':
            sm = w[i][j]
            st.append((i, j))
            w[i][j] = '.'
            while len(st):
                x, y = st.pop()
                if y < m-1:
                    if sm == w[x][y+1]:
                        st.append((x, y+1))
                        w[x][y+1] = '.'
                    elif (x, y+1) in st:
                        f = True
                if y > 0:
                    if sm == w[x][y-1]:
                        st.append((x, y-1))
                        w[x][y-1] = '.'
                    elif (x, y-1) in st:
                        f = True                   
                if x < n-1:
                    if sm == w[x+1][y]:
                        st.append((x+1, y))
                        w[x+1][y] = '.'
                    elif (x+1,y) in st:
                        f = True        
                if x > 0:
                    if sm == w[x-1][y]:
                        st.append((x-1, y))
                        w[x-1][y] = '.'
                    elif (x-1, y) in st:
                        f = True 
                if f: break
        if f: break
    if f: break

print('Yes' if f else 'No')