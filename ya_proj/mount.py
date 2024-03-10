import sys


def is_right_mountain(arr):
    L_cc = R_cc = 0
    for i in range(len(arr)-1):
        if int(arr[i]) < int(arr[i+1]):
            if R_cc:
                return False
            L_cc += 1
        elif int(arr[i]) > int(arr[i+1]):
            if not L_cc:
                return False
            R_cc += 1
        else:
            return False
    return bool(L_cc and R_cc)


if __name__ == '__main__':
    arr = sys.stdin.readline().rstrip().split()
    print(is_right_mountain(arr))