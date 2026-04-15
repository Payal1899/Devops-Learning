#print('Hello from docker from python latest image')

#print('Hello from docker from python V2 image')

with open('names.txt') as f:
    name=f.read()
    #print(name)
    ''''
    name=name.split()
    print(name)
    '''
    name=name.split() #converting to list
    for i,nam in enumerate(name): 
        '''
        enum puts it like below
        (0, 'Achal')
        (1, 'Vansh')
        (2, 'Punam')
        (3, 'Ridu')
        i, nam two var
        '''
        print(f"{i+1}. {nam}")
        #f: formated string
