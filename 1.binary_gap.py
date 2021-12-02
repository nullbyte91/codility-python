N = 10
g_count = 0
count = 0
count_start = False
while N >=1:
    binary = N % 2
    print(binary)
    if binary == 1:
        count = 0
        count_start = True
    elif binary == 0:
        if count_start:
            count += 1
            if count > g_count:
                g_count = count
    N = N >> 1