def find_two_indexes(nums, target):
    for i1 in range(len(nums)):
        if nums[i1] > target:
            continue

        for i2 in range(i1 + 1, len(nums)):
            if nums[i1] + nums[i2] == target:
                return i1, i2

    return None


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))