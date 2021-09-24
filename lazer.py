x = int(input())

scores = []
total_scores = []
for i in range(x):
  scores.append(int(input()))
for j in range(int(x/2)):
  total_scores.append(int(scores[0])+int(scores[1]))
  scores.pop(0)
  scores.pop(0)
  

print(sorted(total_scores))
