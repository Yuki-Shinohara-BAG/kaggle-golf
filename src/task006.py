def p(g):
 return[[g[r][c]*2if g[r][c]==g[r][c+4]and g[r][c]else 0for c in range(3)]for r in range(3)]