def group(n, gn):
    for i in range(1, n + 1):
        g = (i - 1) % gn + 1
        print(i, "號同學：第", g, "組")
