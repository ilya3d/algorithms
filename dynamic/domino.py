# Найти количество способов замостить таблицу n\times m с помощью доминошек размерами  1-2, 2-1.
input = raw_input
n, m = map(int, input().split())

def num2list(x):
    q = []
    for i in xrange(n):
        q.append(x % 2)
        x //= 2
    return q


def ddd(a, b):
    res = 1
    qa = num2list(a)
    qb = num2list(b)
    for i in xrange(n):
        if qb[i] == 1:
            if qa[i] == 0:
                qa[i] = 2
            else:
                res = 0
                break
    for i in xrange(n):
        if qa[i] == 0:
            if (i == n - 1) or qa[i+1] != 0:
                res = 0
                break
            else:
                qa[i+1] = 2
    return res


d = [[ddd(i, j) for j in xrange(2 ** n)] for i in xrange(2 ** n)]

a = [[0 for j in xrange(2 ** n)] for j in xrange(m)]
a[0][0] = 1
for k in xrange(m):
    for i in xrange(2 ** n):
        for j in xrange(2 ** n):
            a[k][i] += a[k-1][j] * d[j][i]

ans = 0
for i in xrange(2 ** n):
    if ddd(i, 0):
        ans += a[m - 1][i]

print ans
