#runme like    $ python groups.py 3 to get 3 groups
import itertools
import numpy as np
import copy
import sys

#moving average
from filters import highPass

HP_SIZE = 10

def getData():
	return [1,2,3,4,2,3,4,1,1,1,1]

def dist(a, b):
	# return np.abs(np.average(a) - np.average(b))
	return 1/(len(a)*len(b)) * sum([ abs(i[0] - i[1]) for i in itertools.product(a, b)])

def merge(sets, num_groups):
	r = copy.deepcopy(sets)
	len_r = len(r)

	#calculate all distances
	distances = []
	for i in range(len_r-1):
		distances.append(dist(r[i], r[i+1]))

	#find minimum distance and then merge it until num_groups is correct
	while(len_r > num_groups):
		
		#i is index at minimum distance
		i = np.argmin(distances)

		#merge
		r[i] = r[i] + r[i+1]
		r.pop(i+1)
		distances.pop(i)

		#fix num of sets
		len_r -= 1
		
		#fix 2 distances around merged set
		if i < len_r-1:
			distances[i] = dist(r[i], r[i+1])
		if i > 0:
			distances[i-1] = dist(r[i-1], r[i])

	return r
	



def getGroups(arr):
	#set same int in one group
	return [ np.ones(len(val)) * i for i, val in enumerate(arr)]

data = [ float(i[2]) for i in getData()]

hp = highPass(data, HP_SIZE)

#get initial sets
s = [[ i ] for i in hp]
c = copy.deepcopy(s)

#groups
g = merge(c, int(sys.argv[1]))

result = getGroups(g)

#write results in file
with open(name + '_' + sys.argv[1] +'_groups.txt', 'w+') as f:
    for i in result:
    	for j in i:
        	f.write(str(j)+'\n')
