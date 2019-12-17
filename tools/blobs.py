##x = [1189, 897, 606, 314, 1189, 897, 606, 314, 2064, 1189, 897, 606, 2356, 2064, 2356, 2064, 1772, 2064, 1772, 1481, 1189]
##y = [3209, 3209, 3209, 3209, 2807, 2807, 2807, 2807, 2405, 2405, 2405, 2405, 2002, 2003, 1600, 1601, 1601, 1199, 1199, 1198, 1199]
##
##xy = [(1189, 3209), (897, 3209), (606, 3209), (314, 3209), (1189, 2807), (897, 2807), (606, 2807), (314, 2807), (2064, 2405), (1189, 2405), (897, 2405), (606, 2405), (2356, 2002), (2064, 2003), (2356, 1600), (2064, 1601), (1772, 1601), (2064, 1199), (1772, 1199), (1481, 1198), (1189, 1199)]

import math

groups = []

def group(val,x,y):
    i=0
    global groups
    x1,y1 = val
    for xp in x:
        yp = y[i]
        if x1 != xp and y1 != yp:
            if math.sqrt((xp-x1)**2+(yp-y1)**2) <= 500:
                #print('X:{} Y:{} grouped with X:{} Y:{}'.format(x1,y1,xp,yp))
                groups.append([(xp,yp),(x1,y1)])
        i+=1
def start(x,y,xy):
    temp_x = x
    temp_y = y
    temp_xy = xy
    for i in xy:
        group(i, temp_x, temp_y)
    average = []
    for i in xy:
        temp = []
        
        for i2 in groups:
            if i in i2:
                if i2[1] not in temp and i!=i2[1]:
                    temp.append(i2[1])
                
        if len(temp) > 2:
            #print('Pairs for X:{} Y:{}'.format(i[0], i[1]))
##            for i2 in temp: 
##                print(i2)
            tx = 0
            ty = 0
            for i2 in temp:
                tx+=i2[0]
                ty+=i2[1]
            #print('Average X:{} Y:{}'.format(tx/len(temp), ty/len(temp)))
            average.append((tx/len(temp), ty/len(temp)))
    temp = []
    for i in average:
        for i2 in average:
            if math.fabs((i[0]-i2[0])) <300 and math.fabs((i[1]-i2[1])) <300:
                if i not in temp:
                    temp.append(i)
                    #print(i)
##    print()
##    for i in temp:
##        print(int(i[0]),',')
##    print()
##    for i in temp:
##        print(int(i[1]),',')
    #print(temp)
    return(temp)
def run(strg):
    eval(strg)
