

class Mat:
    def __init__(self, arr):
	self.arr = arr

    def __s__(self, oth):
	opt = [[0] * len(self.arr[0])] * len(self.arr)
	opt = list(map(list,opt))
	for j in range(len(self.arr[0])):
	    for i in range(len(self.arr)):
		#print opt
	        print i,j 
		opt[i][j] = self.arr[i][j] + oth.arr[i][j]
		print opt
	return opt
	
 

"""
a :=
head_address(a) = 0x0000

| 0x0000 , 1|
| 0x0001 , 2|
| 0x0002,  3|

b = a 

head_address(b) → (=) head_address(a)  
b :=
| 0x0000 , 1|
| 0x0001 , 2|
| 0x0002,  3|

b  = list(a)

| 0x0003 , 1|
| 0x0004 , 2|
| 0x0005,  3|


"""
