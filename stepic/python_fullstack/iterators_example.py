import itertools

def main():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    dni = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

    # i = iter(days)
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))

    # with open("testfile.txt", "r") as fp:
    #     for line in iter(fp.readline, ''):
    #         print(line)

    # for i in range(len(days)):
    #     print(i, days[i])

    # cycle_days = itertools.cycle(days)
    # print(next(cycle_days))
    # print(next(cycle_days))
    # print(next(cycle_days))
    # print(next(cycle_days))
    # print(next(cycle_days))
    # print(next(cycle_days))
    # print(next(cycle_days))
    # print(next(cycle_days))

    # count_stuff = itertools.count(100, 10)
    # print(next(count_stuff))
    # print(next(count_stuff))
    # print(next(count_stuff))
    # print(next(count_stuff))
    # print(next(count_stuff))

    prices = [10, 20, 30, 40, 50, 40 ,30 ,20 , 10, 100]
    acc = itertools.accumulate(prices)
    print(list(acc))
   
    # chain_stuff = itertools.chain(days, prices)
    # print(list(chain_stuff))

    # def test_func(x):
    #     return x < 50

    # print(list(itertools.dropwhile(test_func, prices)))
    # print(list(itertools.takewhile(test_func, prices)))


if __name__ == "__main__":
    main()