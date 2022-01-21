# Python Core
num = int(input())


def fibonacci(n):
    def core(f):
        if f < 1:
            return 0
        elif f <= 2:
            return 1
        else:
            return core(f-1) + core(f-2)

    for i in range(n):
        print(core(i))

fibonacci(num)