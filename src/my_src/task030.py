def p(g):
    r = [[0]*len(g[0]) for _ in range(len(g))]
    t = {}
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] in [1,2,4] and g[i][j] not in t:
                t[g[i][j]] = i
    if 1 not in t: return r
    b = t[1]
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 1:
                r[i][j] = 1
            elif g[i][j] in [2,4] and g[i][j] in t:
                n = i + b - t[g[i][j]]
                if 0 <= n < len(r):
                    r[n][j] = g[i][j]
    return r