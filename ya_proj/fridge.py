import datetime 
from decimal import Decimal 
from pprint import pprint

# goods = {
#     'Пельмени Универсальные': [
#         {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 9, 30)}
#     ]
# }

# def add(items, title, amount, expiration_date=None):
#     try:
#         title_in = title.strip()
#         if expiration_date:
#             year, month, day = map(int, expiration_date.split('-'))
#             date_in = datetime.date(year, month, day)
#         else:
#             date_in = None
#         if title_in in items:
#             items[title_in].append({'amount': Decimal(amount), 'expiration_date': date_in})
#         else:
#             items[title_in] = [{'amount': Decimal(amount), 'expiration_date': date_in}]
#     except NameError as ne:
#         print(f'Ошибка {ne} проверить есть ли словарь {items}')
#     except Exception as ex:
#         print(f'Ошибка {ex}')
goods = {}

def add(items, title, amount, expiration_date=None):
    title_in = title.strip()
    if expiration_date:
        year, month, day = map(int, expiration_date.split('-'))
        date_in = datetime.date(year, month, day)
    else:
        date_in = None
        if title_in in items:
            items[title_in].append({'amount': Decimal(amount), 'expiration_date': date_in})
        else:
            items[title_in] = [{'amount': Decimal(amount), 'expiration_date': date_in}]


def add_by_note(items, note):
    note_in_list = note.split()
    result_list = []
    if '-' not in note_in_list[2]:
        result_list.append(' '.join(note_in_list[:2]))
        result_list.append(note_in_list[2])
        result_list.append(None)
    else:
        result_list.append(' '.join(note_in_list[:-2]))
        result_list.append(note_in_list[-2])
        result_list.append(note_in_list[-1])

    title, good_amount, expiration_date = result_list
    add(items, title, good_amount, expiration_date)


def find(items, needle):
    return [prod for prod in items if needle.lower() in prod.lower()]


def amount(items, needle):
    list_products = find(items, needle)
    counter = 0

    for product in list_products:
        for value in items[product]:
            counter += value['amount']
    return Decimal(str(counter))


def expire(items, in_advance_days=0):
    products_to_expire = dict()

    for product in items:
        for values in items[product]:
            if values.get('expiration_date') and (
                    values.get('expiration_date') <= datetime.date.today()
                    + datetime.timedelta(in_advance_days)):
                if products_to_expire.get(product):
                    products_to_expire[product] += values['amount']
                else:
                    products_to_expire[product] = values['amount']
    return list(products_to_expire.items())

if __name__ == '__main__':
    # проверка функции add
    # add(goods, 'Пельмени Универсальные', Decimal('2'), '2023-10-28')
    # add(goods, 'Яйца', Decimal('10'), '2023-9-30')
    # add(goods, 'Яйца', Decimal('3'), '2023-10-15')
    # add(goods, 'Вода', Decimal('2.5'))
    # pprint(goods)
    add_by_note(goods, 'Яйца гусиные 4 2023-07-15')
    add_by_note(goods, 'Яйца куриные 5')
#     goods = {
#     'Яйца': [{'amount': Decimal('1'), 'expiration_date': datetime.date(2023, 6, 24)}],
#     'Яйца гусиные': [{'amount': Decimal('4'), 'expiration_date': datetime.date(2023, 7, 15)}],
#     'Морковь': [{'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 6)}]
# }
#     print(find(goods, 'йц'))
#     goods = {
#     'Яйца': [{'amount': Decimal('1'), 'expiration_date': None}],
#     'Морковь': [
#         {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
#         {'amount': Decimal('3'), 'expiration_date': datetime.date(2023, 8, 6)}
#     ],
#     'Вода': [{'amount': Decimal('2.5'), 'expiration_date': None}]
# }
#     print(amount(goods, 'яйца'))
# # Вывод: 1
#     print(amount(goods, 'морковь'))
# # Вывод: 5 

    print(goods
    )

