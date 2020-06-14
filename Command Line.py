# Commandline Calc.py
# Last edited by David Hernandez
# 5/23/2020 4:21 PM PT
try:
    import sys
    print('The sum of your arguments will be printed out below')
    # Gets list of integers from command line.
    n = []
    for myargnum in range(1,len(sys.argv)):
        temp = int(sys.argv[myargnum]) #print('Error in' + myargnum + 'was expecting an integer') # print exit
        n.append(temp)

    total = sum(n)
    lmax = len(str(total)) # lmax is length of longest integer
    for num in n:
        if len(str(num)) > lmax:
            lmax = len(str(num))

    for num in n:
        print(' ' * (lmax-len(str(num))) + str(num))

    print('-' * lmax)
    print(' ' * (lmax-len(str(total))) + str(total))
except:
    print('error')

#This is for Github