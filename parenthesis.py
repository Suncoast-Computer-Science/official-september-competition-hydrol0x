x = input()

right = 0
left = 0
for i in x:
  if i == "("
    left += 1
  else:
    right += 1

if left == right:
  print("True")
else: 
  print("False")
