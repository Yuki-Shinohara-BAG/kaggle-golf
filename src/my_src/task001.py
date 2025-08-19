def p(g):
 r=[[0]*9for _ in range(9)];[[r[i*3+k].__setitem__(j*3+l,g[k][l])for k in[0,1,2]for l in[0,1,2]]for i in[0,1,2]for j in[0,1,2]if g[i][j]];return r