def group(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "號同學：第 1 組（偶數組）")
        else:
            print(i, "號同學：第 2 組（奇數組）")
