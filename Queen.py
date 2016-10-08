#!/usr/local/bin/python
#-*-coding:utf-8-*-

def queens(num=4,state=()):
	
	result = []

	#定义冲突条件
	def conflict(state,nextx):
		nexty = len(state)

		#核心限制条件
		for i in xrange(nexty):
			
			if abs(state[i] - nextx) in (0, nexty - i):
				return True

		return False 

	def queen(num,state):

		for pos in range(num):
			
			if not conflict(state,pos):
				
				if len(state) == num-1:
					result.append(state+(pos,))

				else:
					queen(num,state+(pos,))

			else:
				continue

	queen(num,state)
	return result

def main():

	for i in queens(8): print i

if __name__ == '__main__':

	main()
