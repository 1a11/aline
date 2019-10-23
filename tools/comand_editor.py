def edit_obj_list(filename):
    import os
    f1 = open(filename,'r') 
    #print(f1.read())
    obj = list()
    for line in f1:
        if '\n' in line:
            line = line[:-1]
        obj.append(line)
    while True:        
        os.system('cls')
        print('Current objets list:')
        j = 0
        for i in obj:
            j+=1
            print(j,') ',i,sep = '')
        print()
        print('1. Add object')
        print('2. Remove object')
        print('3. Exit')
        n = int(input())
        if n == 1:
            s = input('(write smth): ')
            obj.append(s)
        elif n == 2:
            s = int(input('(index pls): '))
            obj.pop(s-1)    
        elif n == 3:
            break
    f2 = open(filename,'w')
    for i in obj:
        f2.write(i+'\n')
    f1.close()
    f2.close()
    os.system('cls')
