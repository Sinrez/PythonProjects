import sys


def find_index(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if int(arr[mid]) == target:
            while mid > 0 and int(arr[mid - 1]) == target:
                mid -= 1
            return mid
        elif int(arr[mid]) < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def main():
    arr = sys.stdin.readline().rstrip().split()
    target = int(sys.stdin.readline().rstrip())

    index = find_index(arr, target)
    print(index)


if __name__ == '__main__':
    main()
