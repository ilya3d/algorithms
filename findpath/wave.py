# Волновой алгоритм поиска пути
m = [[0, 0, 0, 0, 0],
     [0, 1, 0, 1, 0],
     [0, 1, 0, 1, 0],
     [0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0]]

def fnd(maps, sx, sy, fx, fy):
    h = len(maps)
    w = len(maps[0])
    a = [[-1 for i in range(w)] for j in range(h)]
    a[sy][sx] = 0
    mt = 0
    while a[fy][fx] == -1:
        mt += 1
        for j in xrange(h):
            for i in xrange(w):
                if a[j][i] == mt - 1:
                    if i > 0 and maps[j][i - 1] == 0 and a[j][i - 1] == -1: a[j][i - 1] = mt
                    if i < w-1 and maps[j][i + 1] == 0 and a[j][i + 1] == -1: a[j][i + 1] = mt
                    if j > 0 and maps[j - 1][i] == 0 and a[j - 1][i] == -1: a[j - 1][i] = mt
                    if j < h-1 and maps[j + 1][i] == 0 and a[j + 1][i] == -1: a[j + 1][i] = mt
    path = []
    i = fx
    j = fy
    while mt > 0:
        mt -= 1
        path.append((i, j))
        if i > 0 and a[j][i - 1] == mt:
            i -= 1
        elif i < w-1 and a[j][i + 1] == mt:
            i += 1
        elif j > 0 and a[j - 1][i] == mt:
            j -= 1
        elif j < h-1 and a[j + 1][i] == mt:
            j += 1
        else:
            break
    return path

print(fnd(m, 0, 0, 4, 4))