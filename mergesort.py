#!/usr/local/bin/python
#-*-coding:utf-8-*-

def merge(inlist1,inlist2):

	c1 = len(inlist1)
	c2 = len(inlist2)
	idx1 = 0
	idx2 = 0
	temp1 = inlist1[idx1]
	temp2 = inlist2[idx2]
	new = []

	while True:

		if temp1 <= temp2:
			new.append(temp1)
			idx1 += 1
			
			if idx1 < c1:
				temp1 = inlist1[idx1]
				continue
			
			else:
				new += inlist2[idx2:]
				break
		else:
			new.append(temp2)
			idx2 += 1
			
			if idx2 < c2:
				temp2 = inlist2[idx2]
				continue

			else:
				new += inlist1[idx1:]
				break
		

	return new

def mergesort(inlist):

	queue = [[i] for i in inlist]
	size = len(inlist)
	while size > 1:
		inlist1 = queue.pop(0)
		size -= 1
		inlist2 = queue.pop(0)
		size -= 1
		new = merge(inlist1,inlist2)
		queue.append(new)
		size += 1
	
	return queue[0]

if __name__ == '__main__':

	inlist = [0,100,55]
	print mergesort(inlist)




