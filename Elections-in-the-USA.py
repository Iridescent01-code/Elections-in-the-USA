n = int(input())
d = {}
for i in range(n):
    p1, k1 = input().split()
    votes = int(k1)
    d[p1] = d.get(p1, 0) + votes

for p1, k1 in sorted(d.items()):
    print(p1, k1)
  