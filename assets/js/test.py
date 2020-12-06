n = int(input())
arr = list(map(int, input().split()))
k = int(input())
for _ in range(k):
  a,b = map(int, input().split())
  arr[arr.index(a)] = b
  print(sum(arr))