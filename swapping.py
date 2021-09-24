str1 = str(input())

last = str1[-1] 
first = str1[0]

str1.pop(0)
str1.pop(-1)

output = str1.append(first)
output = output.insert(0, last)
print(output)
