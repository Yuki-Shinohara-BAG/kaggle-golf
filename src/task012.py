def p(g):
 r=[R[:]for R in g]
 for i in range(1,11):
  for j in range(1,11):
   c,t,b,l,R=g[i][j],g[i-1][j],g[i+1][j],g[i][j-1],g[i][j+1]
   if c*t*b*l*R*(t==b==l==R)*all(g[i+x][j+y]<1for x,y in[(-1,-1),(-1,1),(1,-1),(1,1)]):
    for x in range(5):
     for y in range(5):
      if-1<i+x-2<12>j+y-2>-1:r[i+x-2][j+y-2]=[[c,0,t,0,c],[0,c,t,c,0],[t,t,c,t,t],[0,c,t,c,0],[c,0,t,0,c]][x][y]
 return r