def p(g):
 r=[r[:]for r in g];h=[(sum(g[i][c]==5for i in range(9)),c)for c in[1,3,5,7]];h.sort(reverse=1)
 for k,(z,c)in enumerate(h):
  for i in range(9):r[i][c]=r[i][c]==5and k+1or r[i][c]
 return r