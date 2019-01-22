number = [10,20,30,40]

print(number[2])

number[2] = 200
# print(number[2])

for num in number:
	print(num)

for num in range(len(number)):
	print(number[num])

print(number[:-2])
maximum = number[0]
for num in number:
	if num>maximum:
		maximum = num

print(maximum)