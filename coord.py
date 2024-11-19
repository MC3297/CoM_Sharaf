f = open("data.txt", 'r')
L = f.readlines()
for line in L:
    
    if (line[0].isnumeric()):
        ls = line.split(' | ')
        ind = 0
        for i in ls[:-1]:
            j = i.split(',')
            if ind == 0 or ind == 3: print(f'{(float(j[0])-200):6.1f},{(float(j[1])-200):6.1f}|',end='')
            else: print(f'{(float(j[0])-200):8.3f},{(float(j[1])-200):8.3f}|',end='')
            ind+=1
        print(ls[-1],end='')
    else:
        print(line,end='')
    