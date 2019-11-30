def solve(a, b):
    a.sort(reverse=True)
    b.sort(reverse=False)
    sum = 0
    for i in range(0, size):
        sum = sum + (a[i] * b[i])
    return sum


t = input().split()
t = int(t[0])
for test in range(1, t + 1):
    size = input().split()
    size = int(size[0])
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    print("Case #{}: {}".format(test, solve(a, b)))
