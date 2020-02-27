import sys


def best(start, end, E, r, tasks):
    if len(tasks) == 0:
        return 0
    most = max(tasks)
    pivot = tasks.index(most)
    get = min(E, start + pivot * r)
    recover = (len(tasks) - pivot - 1) * r
    can_spend = max(0, min(E, get + recover - end))
    energy = min(get, can_spend)
    gain = energy * most
    left = best(start, max(end, energy - r), E, r, tasks[:pivot])
    right = best(r, end, E, r, tasks[pivot + 1:])
    return left + gain + right


def solve(e, r, n, tasks):
    return best(e, 0, e, r, tasks)


def readline():
    return sys.stdin.readline().strip()


numcases = int(readline())
for casenum in range(1, numcases+1):
    params = readline().split()
    e = int(params[0])
    r = int(params[1])
    n = int(params[2])
    data = readline().split()
    tasks = [int(x) for x in data]
    print("Case #{}: {}".format(casenum, solve(e, r, n, tasks)))
