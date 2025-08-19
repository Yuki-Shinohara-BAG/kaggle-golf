def p(g):
 r=[row[:]for row in g]
 e=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j]==8]
 t=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j]==2]
 if not e or not t:return r
 er=[x[0]for x in e];ec=[x[1]for x in e];tr=[x[0]for x in t];tc=[x[1]for x in t]
 em,eM,en,eN=min(er),max(er),min(ec),max(ec);tm,tM,tn,tN=min(tr),max(tr),min(tc),max(tc)
 rd,cd=(em+eM-tm-tM)/2,(en+eN-tn-tN)/2
 mr=mc=0
 if abs(rd)>abs(cd):mr=em-tM-1if rd>0else eM-tm+1
 else:mc=en-tN-1if cd>0else eN-tn+1
 for i,j in t:r[i][j]=0
 for i,j in t:
  if 0<=i+mr<len(r)and 0<=j+mc<len(r[0]):r[i+mr][j+mc]=2
 return r