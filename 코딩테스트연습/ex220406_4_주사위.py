# 백준 9295번
import sys
T = int(sys.stdin.readline())
s = []
for _ in range(T):
    a, b = map(int,sys.stdin.readline().split())
    s.append(a+b)
for i in range(T):
    print('Case ',i+1,': ',s[i],sep='')