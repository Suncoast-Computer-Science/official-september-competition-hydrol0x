x = int(input())
for i in range(x):
  str1 = str(input()) 

  last = str1[-1] 
  first = str1[0]

  str1.replace(last, first)
  str1.replace(first, last)
  print(str1)
