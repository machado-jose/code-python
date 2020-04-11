n = int(input())
#A função map retorna um generator (Python 3)
arr = list(map(int, input().split()))

arr = [number for number in arr if number != max(arr)]

print(max(arr))

