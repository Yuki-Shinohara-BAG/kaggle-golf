def p(g):
 r=[[0]*10for _ in range(10)];t=b=T=B=0
 for i in range(10):
  for j in range(10):
   if g[i][j]:
    if i<5:t,T=g[i][j],i
    else:b,B=g[i][j],i
 for i in range(10):c,C=(t,T)if i<5else(b,B);r[i]=[c]*10if i in[0,9,C]else[c if j<1or j>8else 0for j in range(10)]
 return r