# my_code

N, M, K = map(int, input().split())
n = list(map(int, input().split()))

n.sort()
n = n[::-1]

a = M // K
b = M % K

sum = a * K * n[0] + b * n[1]
print(sum)
