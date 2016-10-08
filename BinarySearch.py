#!/usr/local/bin/python
#-*-coding:utf-8-*-
import sys

def binarysearch(inlist,num):

	endidx = len(inlist) - 1
	minidx = 0
	maxidx = endidx
	mididx = (maxidx+minidx)/2
	mid = inlist[mididx]

	if num < inlist[0] or num > inlist[maxidx]:
		print "fail, num not in inlist"

	else:
		
		while num != mid:
			
			if num <= mid:
				maxidx = mididx - 1
				mididx = (maxidx + minidx)/2
				mid = inlist[mididx]

			else:
				minidx = mididx + 1
				mididx = (maxidx + minidx)/2
				mid = inlist[mididx]

			if minidx > maxidx:
				print "fail, num not in inlist"
				sys.exit()

		return mididx

def main():

	inlist = [2,4,6,8,10]
	num = 6
	print binarysearch(inlist,num)

if __name__ == '__main__':

	main()
