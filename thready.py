import multiprocessing

import time
def slowFn(n):
	sumTotal = sum([1 for _ in range(n)])


if __name__ == '__main__':
    for m in [10,100,1000,10000]:
	for n in [10,100,1000,10000,100000]:
		res = []		
		b = time.time()    		
		for i in range(m):
			p = multiprocessing.Process(target=slowFn,args=(n,))
			p.start()
    			e = time.time()
    		res.append(str(e-b)) 
    		b = time.time()
    		for i in range(m):
    			slowFn(n)
   		e = time.time()
    		res.append(str(e-b)) 
    		print res
    


'''
	for article
    

'''
