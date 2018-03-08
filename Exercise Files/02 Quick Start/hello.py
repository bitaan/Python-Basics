for i in range(int(input())):
    n = int(input())
    s = 0
    while n > 0:
        t = n % 10
        s = s + t
        n = n // 10
    print(s)