
import sys


def min_platforms(weights: list[str], limit: int) -> int:
    weights.sort()
    platforms = 0  # Счетчик платформ
    left, right = 0, len(weights) - 1

    while left <= right:
        # Если сумма весов крайних роботов не превышает лимит,
        # перемещаем оба индекса
        if int(weights[left]) + int(weights[right]) <= limit:
            left += 1
            right -= 1
        # Иначе перемещаем только правый индекс
        else:
            right -= 1
        platforms += 1

    return platforms


if __name__ == "__main__":
    robots = sys.stdin.readline().rstrip().split()
    limit = int(sys.stdin.readline().rstrip())
    print(min_platforms(robots, limit))
