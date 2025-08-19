def p(g):
 r=[row[:]for row in g]
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]==2:
    for d,e in[(-1,1),(1,1),(-1,-1),(1,-1)]:
     n,s=i+d,j+e
     if 0<=n<len(g)and 0<=s<len(g[0]):r[n][s]=4
   elif g[i][j]==1:
    for d,e in[(-1,0),(1,0),(0,-1),(0,1)]:
     n,s=i+d,j+e
     if 0<=n<len(g)and 0<=s<len(g[0]):r[n][s]=7
 return r