import sys


def count_smaller(nums): 
    n = len(nums)
    result = [0] * n
    for i in range(n): 
        count = 0 
        for j in range(n): 
            if int(nums[j]) < int(nums[i]): 
                count += 1 
        result[i] = count 
    return result


if __name__ == '__main__':
    arr = sys.stdin.readline().rstrip().split()
    print(*count_smaller(arr))
