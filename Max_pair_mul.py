n = int(input())
num = [int(x) for x in input().split()]
num.sort()
num=num[::-1]
print(num[0]*num[1])
