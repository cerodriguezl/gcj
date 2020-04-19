def solve(matrix, N):
    traspose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    trace = sum([matrix[x][x] for x in range(0, N)])
    a = [x for x in range(1, N + 1)]
    rows = 0
    cols = 0
    for row in matrix:
        row.sort()
        if (row != a):
            rows = rows + 1
    for col in traspose:
        col.sort()
        if (col != a):
            cols = cols + 1
    return (trace, rows, cols)


t = input().split()
t = int(t[0])
for test in range(1, t + 1):
    N = input().split()
    N = int(N[0])
    matrix = [list(map(int, input().rstrip().split())) for x in range(0, N)]
    (x, r, c) = solve(matrix, N)
    print("Case #{}: {} {} {}".format(test, x, r, c))