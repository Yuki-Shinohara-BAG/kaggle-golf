def p(g):
 p1,p2=g[:3],g[3:]
 r=[[x*2for x in row]for row in g]
 r+=[[x*2for x in row[::1-2*(p1!=p2)]]for row in p1]
 return r