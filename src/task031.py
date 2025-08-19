def p(g):
 r=[i for i,x in enumerate(g)if any(x)]
 c=[j for j in range(len(g[0]))if any(g[i][j]for i in r)]
 return[[g[i][j]for j in c]for i in r]