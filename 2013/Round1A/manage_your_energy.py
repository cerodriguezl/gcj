import sys


def best(energy, recovery, tasks, E):
    if len(tasks) == 1:
        return energy * tasks[0]
    else:
        solution = 0
        for x in range(0, energy + 1):
            gain = x * tasks[0]
            remaining = min(energy - x + recovery, E)
            total = gain + best(remaining, recovery, tasks[1:], E)
            if total > solution:
                solution = total
        return solution


def solve(e, r, n, tasks):
    return best(e, r, tasks, e)


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
