def p(g):
 r=[[0]*len(g[0])for _ in g]
 for c in range(len(g[0])):
  s=[g[i][c]for i in range(len(g))if g[i][c]]
  for i,v in enumerate(s):r[-len(s)+i][c]=v
 return r