row = []
matrix = []
for i in range(1001):
	row.append(0)
for i in range(1001):
	matrix.append(row)
number = 0
count = 0
limit = 1
a = 500
b = 500
matrix[500][500]
while (number < 100):
	count = 0
	while (count < limit):
		number += 1
		b += 1
		matrix[a][b] = number
		print(a)
		print(b)
		count  += 1
	count = 0
	while (count < limit):
		number += 1
		a += 1
		matrix[a][b] = number
		count  += 1
	limit += 1
	if number < 1002000:
		count = 0
		while (count < limit):
			number += 1
			b -= 1
			matrix[a][b] = number
			count  += 1
		count = 0
		while (count < limit):
			number += 1
			
			a -= 1
			matrix[a][b] = number
			count  += 1
		print(number)
	limit += 1

