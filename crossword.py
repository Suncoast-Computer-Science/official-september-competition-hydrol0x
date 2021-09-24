x = input()
y = input()
z = input() 

if len(x) < len(y):
  prefix = x
  word = y
else:
  prefix = y
  word = x
  
final = prefix + word
if len(final) != z:
  print("False")
else: 
  print(Final)
