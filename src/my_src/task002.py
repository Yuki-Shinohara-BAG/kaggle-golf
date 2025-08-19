def p(g):
 v,h,w=set(),len(g),len(g[0])
 r=[R[:]for R in g]
 for i in range(h):
  for j in range(w):
   if(i,j)in v or g[i][j]:continue
   s,t,q=[(i,j)],0,[]
   while s:
    x,y=s.pop()
    if(x,y)in v:continue
    v.add((x,y));q+=[(x,y)]
    if x<1or y<1or x>h-2or y>w-2:t=1
    for X,Y in[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
     if 0<=X<h and 0<=Y<w and(X,Y)not in v and g[X][Y]<1:s+=[(X,Y)]
   if not t:
    for X,Y in q:r[X][Y]=4
 return r