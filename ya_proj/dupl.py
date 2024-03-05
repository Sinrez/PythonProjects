import sys


def main():
    elements_count = int(sys.stdin.readline().rstrip())
    line = sys.stdin.readline().rstrip().split()

    unique_nums = ['_'] * elements_count
    unique_index = 0

    for i in range(elements_count):
        val = int(line[i])
        if val not in unique_nums:
            unique_nums[unique_index] = val
            unique_index += 1

    print(*unique_nums)


if __name__ == '__main__':
    main()
