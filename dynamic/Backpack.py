# кол-во предметов
# n = 6
# вместительность рюкзака
# v = 10
# вес предметов
# w = [1, 1, 1, 2, 2, 3]
# стоимость предметов
# p = [1, 1, 2, 3, 3, 5]


def fnd(w, p, v):
    n = len(w)
    a = [[0 for i in range(v + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(v + 1):
            if j > w[i - 1]:
                a[i][j] = max(a[i - 1][j], a[i - 1][j - w[i - 1]] + p[i - 1])
            else:
                a[i][j] = a[i - 1][j]
    ans = list()
    i = n
    j = v
    while a[i][j] > 0:
        if a[i - 1][j] == a[i][j]:
            i -= 1
        else:
            j = j - w[i - 1]
            i -= 1
            ans.append(j)
    return ans


x = [1, 1, 1, 1]
y = [1, 1, 1, 1]

print(fnd(x, y, 10))