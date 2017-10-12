import multiprocessing
from multiprocessing import Pool

import time
def randomFn(n):
	for i in range(2000):
		print 'so random! lol '+str(n)

def expo(a):
	return 2**a


def runOnPool(n,f,l):
	p = Pool(n)
	b = time.time()
	p.map(f,l)
	e = time.time()
	print(str(e-b))


if __name__ == '__main__':
    lista = []
    '''for i in range(1000):
    	lista.append(i)
    for j in range(31):
    	print(str(j))	
    	runOnPool(j+1,expo,lista)'''
    res = []
    b = time.time()
    for i in range(3000):
        p = multiprocessing.Process(target=randomFn,args=(i,))
        p.start()
    e = time.time()
    res.append(str(e-b)) 
    b = time.time()
    for i in range(3000):
    	randomFn(i)
    e = time.time()
    res.append(str(e-b)) 	
    print res
    
	