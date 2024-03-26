import sys


def measurements_per_second(generation):
    if generation == 0:
        return 1
    elif generation == 1:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, generation + 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    limit = int(sys.stdin.readline().rstrip())
    print(measurements_per_second(limit))