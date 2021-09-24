str1 = str(input())

output = []
for i in range(1, len(str)):
  for j in str1:
    output.append(j[-i])
print(output)
