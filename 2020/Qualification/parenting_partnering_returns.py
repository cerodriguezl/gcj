def canTake(person, s, e):
    if (s == e):
        if person[s] == 1:
            return False
    for x in range(s, e):
        if person[x] == 1:
            return False
    person[s] = 1
    for x in range(s, e):
        person[x] = 1
    return True


def solve(activities):
    a = [0] * (24 * 60)
    b = [0] * (24 * 60)
    activities.sort()
    assignations = [''] * len(activities)
    for activity in activities:
        (s, e, i) = activity
        if (canTake(a, s, e)):
            assignations[i] = 'C'
        elif (canTake(b, s, e)):
            assignations[i] = 'J'
        else:
            return 'IMPOSSIBLE'
    return ''.join(assignations)


# result = solve([(1, 2, 0), (5, 7, 1), (2, 6, 2), (1, 4, 3)])
# print(result)
# result = solve([(1, 2, 0), (1, 2, 1)])
# print(result)


t = input().split()
t = int(t[0])
for test in range(1, t + 1):
    N = input().split()
    N = int(N[0])
    damn = []
    for x in range(N):
        data = input().split()
        s = int(data[0])
        e = int(data[1])
        damn.append((s, e, x))
    result = solve(damn)
    print("Case #{}: {}".format(test, result))
