import vis_jsonparser as vp
import visualizer as vis
data = vp.parser().get()['dots']

with open('code.vis','r') as ifile:
    code = str(ifile.read()).replace('\n','')
    if 'rotate' not in code:
        raise Exception("Sin error: can't find rotate keyword")
    elif '{' not in code or '}' not in code:
        raise Exception("Sin error: can't open/close bracket")
    else:
##        with open('machine.avis','a') as ofile:
##                    ofile.write('/Commands begin/')
##        code = code.replace('rotate{','').replace('}','')
##        commands = code.split(';')
##        for i in commands:
##            if i != '':
##                
##                with open('machine.avis','a') as ofile:
##                    ofile.write('rotating {} to {} for {} degs; '.format(i.split(' ')[0],i.split(' ')[1],i.split(' ')[2]))
##                    ofile.close()
##        with open('machine.avis','a') as ofile:
##                    ofile.write('/Commands end/')        
        keys = []
        for name,dict_ in data.items():
               keys.append(name)
##        with open('machine.avis','a') as ofile:
##                    ofile.write('/Code begin/')
        i2=0
        with open('machine.avis','w') as ofile:
            ofile.write("")
            
        for i in data:
            with open('machine.avis','a') as ofile:
                    ofile.write("point{}=ax.scatter([{}], [{}], [{}], zdir='z', s=20,c='{}');".format(i,data[keys[i2]]['cords'][0],data[keys[i2]]['cords'][1],data[keys[i2]]['cords'][2], data[keys[i2]]['color']))
            i2+=1
        i2=0

        with open('machine.avis','a') as ofile:
            ofile.write('plt.pause(0.05);')
        
        for i in data:
            with open('machine.avis','a') as ofile:
                ofile.write('point{}.remove();'.format(i))
##        with open('machine.avis','a') as ofile:
##                    ofile.write('/Code end/')    
        vis.vis()
