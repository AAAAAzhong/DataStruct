#!/usr/local/bin/python
#-*-coding:utf-8-*-

def selectsort(inlist):
	
	endidx = len(inlist)

	for t in xrange(0,endidx):
		temp = inlist[t]
		mini = temp
		minidx = t
		beginidx = t+1

		for i in xrange(beginidx,endidx):
			currentnum = inlist[i]
			
			if currentnum < mini:
				mini = currentnum
				minidx = i
			
			else:
				continue
	
		if mini < temp:
			inlist[t] = mini
			inlist[minidx] = temp
		
		else:
			continue

	return inlist

def main():
	
	inlist = [2,4,12,1,4,6,7,3,2,8]
	print selectsort(inlist)

if __name__ == '__main__':

	main()
				




