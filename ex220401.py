n = int(input())
s = []
for _ in range(n):
    a, b = map(int,input().split())
    s.append(a+b)
print(s)