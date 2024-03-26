import sys


def get_min_platforms(weights: list[int], limit: int) -> int:
    sorted_weights = sorted(weights)
    platforms = 0  # Счетчик платформ
    left, right = 0, len(weights) - 1

    while left <= right:
        # Если сумма весов крайних роботов не превышает лимит,
        # перемещаем оба индекса
        if sorted_weights[left] + sorted_weights[right] <= limit:
            left += 1
        right -= 1
        platforms += 1
    return platforms


if __name__ == "__main__":
    robots = [int(robot) for robot in sys.stdin.readline().rstrip().split()]
    limit = int(sys.stdin.readline().rstrip())
    print(get_min_platforms(robots, limit))
