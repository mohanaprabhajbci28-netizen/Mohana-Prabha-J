n1, n2 = map(int, input().split())


for end_val in range(n2, n1 - 1, -1):
    row = [str(i) for i in range(n1, end_val + 1)]
    print(" ".join(row))
