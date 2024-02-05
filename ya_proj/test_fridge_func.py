# from decimal import Decimal
# import datetime
# from pprint import pprint

# goods = {}

# def add(items, title, amount, expiration_date=None):
#     try:
#         title_in = title.strip()
#         if title_in in items:
#             items[title_in].append({'amount': Decimal(amount), 'expiration_date': expiration_date})
#         else:
#             items[title_in] = [{'amount': Decimal(amount), 'expiration_date': expiration_date}]
#     except NameError as ne:
#         print(f'Ошибка {ne} проверить есть ли словарь {items}')
#     except Exception as ex:
#         print(f'Ошибка {ex}')

# add(goods, 'Пельмени Универсальные', Decimal('0.5'), datetime.date(2023, 7, 15))
# add(goods, 'Пельмени Универсальные', Decimal('2'), datetime.date(2023, 8, 1))
# add(goods, 'Вода', Decimal('1.5'))

# pprint(goods)

import datetime

date_str = '2023-10-28'
year, month, day = map(int, date_str.split('-'))
date_obj = datetime.date(year, month, day)

print(date_obj)
