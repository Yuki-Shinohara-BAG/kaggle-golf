def p(g):
 r=[row[:]for row in g]
 a=b=10;c=d=-1
 for i in range(10):
  for j in range(10):
   if g[i][j]==8:a,c,b,d=min(a,i),max(c,i),min(b,j),max(d,j)
 for i in range(10):
  for j in range(10):
   if g[i][j]not in[0,8]:
    v=g[i][j]
    if i<a:r[a][j]=v
    elif i>c:r[c][j]=v
    elif j<b:r[i][b]=v
    elif j>d:r[i][d]=v
 return r