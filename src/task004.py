def p(g):
    h,w=len(g),len(g[0])
    cr=[r for r in range(h)if any(g[r])]
    if not cr:return g
    gs,s=[],cr[0]
    for i in range(1,len(cr)):
        if cr[i]!=cr[i-1]+1:gs+=[(s,cr[i-1])];s=cr[i]
    gs+=[(s,cr[-1])]
    for s,e in gs:
        for r in range(s,e-1):
            for c in range(w-1,-1,-1):
                if g[r][c]:
                    if c+1<w:g[r][c+1]=g[r][c]
                    g[r][c]=0
        lp=None
        for r in range(max(s,e-1),e+1):
            for c in range(w):
                if g[r][c]and(lp is None or(r,c)<lp):lp=r,c
        if lp and lp[1]+1<w:r,c=lp;g[r][c+1]=g[r][c];g[r][c]=0
    return g