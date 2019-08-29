import json
c = {'dots':{'0xAA':{'cords':[0,0,0],'color':'b','allowation':'lr','mother':''},\
             '0xAB':{'cords':[0,0,100],'color':'r','allowation':'ud','mother':'0xAA'},\
             '0xAC':{'cords':[2,0,150],'color':'r','allowation':'ud','mother':'0xAA0xAB'},\
             '0xAD':{'cords':[10,0,200],'color':'r','allowation':'ud','mother':'0xAA0xAB0xAC'}}\
     }

with open('config.json', 'w') as outfile:
    json.dump(c, outfile, indent=4)            
