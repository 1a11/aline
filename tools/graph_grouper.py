def eq(xy1,xy2):
    x1 = xy1[0] 
    y1 = xy1[1]
    x2 = xy2[0]
    y2 = xy2[1]
    if -1 <= (x1 - x2) <= 1:
        if -1 <= (y1 - y2) <= 1:
            return(True)
    else:
        return(False)

def nearby(a):
    x = a[0]
    y = a[1]
    return([(x+1,y),(x-1,y),(x,y+1),(x,y-1)])
##
##def group():    
##    from image_coord import div
##    g = div()
##    g.sort()
##    print(g)
##    obj = list()
##    obj.append([(-2,-2)])
##    prev = obj[0][0]
##    i2 = 0
##    q = list()
##    print(len(g))
##    i = 0
def group():
    from image_coord import div
    g = div()
    g.sort()
    print(g)
    obj = list()
    #obj.append([(-2,-2)])
    #prev = obj[0][0]
    i2 = 0
    q = list()
    print(len(g))
    #for i in range(len(g)):
    i = 0
    while g != []:
        a = []
        q.append(g[0])
        print('lol')
        while q != []:
            #print(q)
            n = nearby(q[0])
            nn =[]
            for j in n:
                if j in g:
                    nn.append(j)
                    g.pop(g.index(j))
            q += nn
            a.append(q[0])
            q.pop(0)
        obj.append(a)
        for i in obj[i2]:
            try:
                g.pop(g.index(i))
            except:
                pass
        i2+=1
        return obj
    #for i in range(len(g)):
##    while i < len(g):
##        print(i)
##        q.append(g[i])
##        for j in range(i+1,len(g)-1):
##            if eq(g[i],g[j]):
##                q.append(g[j])
##        print(q)
##        g.pop(0)
##        i += 1
##                
##    for i in g:
##        if eq(prev,i):
##            obj[0].append(i)
##        else:
##            i2+=1
##            obj.append([])
##            obj[i2].append(i)
##        prev = i
    #return(obj)
