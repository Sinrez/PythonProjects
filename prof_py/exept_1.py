import math
import logging


logger = logging.getLogger(__file__)


class OutsideRangeException(Exception):
    """свое исключение для пользовательского ввода"""
    pass


def range_check_user_input(parameter: int) -> float:
    """
    Проверка пользовательского ввоода
    """
    if not 0 < parameter <= 100:
        raise OutsideRangeException("Выход за пределы диапазона: ", parameter)

    return parameter


def get_data_from_user():
    """функция реализует пользовательский ввод
    """
    successful = False
    while not successful:
        parameter = input(
            "Please enter a integer greater than 0 and less than or equal to 100: ")

        try:
            parameter = int(parameter)
        except ValueError as e:
            logger.exception("Something happened", e)
            print(e)
            continue

        try:
            result = range_check_user_input(parameter)
        except OutsideRangeException as e:
            logger.exception("Parameter outside of range", e)
            print(
                "Entered value outside of acceptable range,"
                " please re-enter a valid number"
            )
        except Exception as ex:
            logger.exception("Другая ошибка,", ex)
            print(
                f'cлучилась другая ошибка: {ex}'
            )            
            continue

        print(f"Parameter within range = {result}")
        successful = True


def main():
    get_data_from_user()


if __name__ == "__main__":
    main()