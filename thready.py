import multiprocessing
from PIL import Image, ImageDraw
import time
def slowFn(n):
	sumTotal = sum([1 for _ in range(n)])


if __name__ == '__main__':
    lista = []
    res = []
    b = time.time()
    m,n = 500,100000
    for i in range(m):
	p = multiprocessing.Process(target=slowFn,args=(n,))
	p.start()
    e = time.time()
    res.append(str(e-b)) 
    b = time.time()
    for i in range(m):
    	slown(n)
    e = time.time()
    res.append(str(e-b)) 
    print res


'''
	for article
    

'''
