import sys

def solve(r, t):
    a = 0
    lo = 1
    hi = t
    while lo <= hi:
        k = (lo + hi) // 2
        if k * (2*r + 2*k - 1) > t:
            hi = k - 1
        else:
            lo = k + 1
            a = k
    return a

numcases = int(sys.stdin.readline())
for casenum in range(1, numcases+1):
    data = sys.stdin.readline().strip().split()
    r = int(data[0])
    t = int(data[1])
    print("Case #{}: {}".format(casenum, solve(r,t)))