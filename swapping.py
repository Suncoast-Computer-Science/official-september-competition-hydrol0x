x = int(input())

for i in range(x):
  string = str(input()) 
  
  first = string[0]
  last = string[-1]
  middle = string[1:-1] 

  string = last + middle + first
  print(string)
