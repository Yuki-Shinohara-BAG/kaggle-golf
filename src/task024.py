def p(g):
 r=[r[:]for r in g]
 for j in range(len(g[0])):
  if any(r[i][j]==2for i in range(len(g))):
   for i in range(len(g)):r[i][j]=2
 for i in range(len(g)):
  for v in[1,3]:
   if any(r[i][j]==v for j in range(len(g[0]))):
    for j in range(len(g[0])):r[i][j]=v
 return r