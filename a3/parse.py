import math
from decimal import Decimal

factory = []


def read_milliseconds(FILE):
	max_number = -1
	T = []
	with open('%s' % (FILE), 'r') as infile:
		for line in infile:
			T = line.split()
			if(T[0] == 'Statistics:'):
				for i in range(max_number+1):
					factory.append([])
				break
			if (max_number < int(T[0])):
				max_number = int(T[0])
		infile.seek(0)
		for line in infile:
			T = line.split()
			if(T[0] == 'Statistics:'):
				return factory
			for i in range(int((len(T)/2))):
				factory[int(T[0])].append(float(T[1]))

def compare(FILE,LIST):
	A = []
	i = 0
	with open('%s' % (FILE), 'r') as infile:
		for line in infile:
			A = line.split()
			if(A[0] == 'Factory#'):
				break
		for line in infile:
			B = []
			A = line.split()
			B.append(A[0])
			B.append(A[3])
			B.append(A[4])
			B.append(A[5])
			if(int(B[0]) == LIST[i][0] and float(B[1]) == LIST[i][1] and Decimal(B[2]) == LIST[i][2] and float(B[3]) == LIST[i][3]):
				print("Pass")
			elif(B[0] == "ERROR:"):
				print("Mismatch on Made and Eaten on Factory# "+ str(i))
			else:
				if(int(B[0]) != LIST[i][0]):
					print("Factory doesnt match on Factory# " + str(i))
				elif(float(B[1]) != LIST[i][1]):
					print("Min value doesnt match on Factory# " + str(i))
				elif(Decimal(B[2]) != LIST[i][2]):
					print("Avg value doesnt match on Factory# "+ str(i))
				elif (float(B[3]) == LIST[i][3]):
					print("Max value doesnt match on Factory# "+ str(i))
			i += 1
def mean(A):
	m = sum(A)
	n = len(A)
	m = Decimal(m)/Decimal(n)
	return m

def max_delay(A):
	return max(A)

def min_delay(A):
	return min(A)



def main():

	wut = []
	actual = []
	lol = read_milliseconds("test.txt")
	for i in range(len(lol)):
		actual.append([i,min_delay(lol[i]),mean(lol[i]),max_delay(lol[i])])
		wut.append([i,round(min_delay(lol[i]),5),round(mean(lol[i]),5),round(max_delay(lol[i]),5)])
	# compare("test.txt", wut) #uncomment for results.txt
	# print("Actual Array Values") 
	# for i in range(len(actual)): #uncomment for actualvaules.txt
	# 	print(actual[i])

	# print("Calculated Array Values") 
	for i in range(len(wut)): #uncomment for cacluatedvalues.txt
		print(wut[i])

if __name__ == '__main__':
	main()