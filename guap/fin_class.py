class Person:
    """Класс физ лицо"""
    def __init__(self, name, phone_number, address):
        self.__name = name
        self.__phone_number = phone_number       
        self.__address = address       

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address


class Customer(Person):
    """Класс покупатель"""
    client_id_counter = 1 

    def __init__(self, name, phone_number, address):
        super().__init__(name, phone_number, address)
        self.client_id = Customer.client_id_counter  # присваиваем id покупателя
        Customer.client_id_counter += 1  # увеличиваем id для следующего покупателя


class ShoppingCart:
    """Корзина для покупок"""
    def __init__(self):
        self.product_list = []
    
    def add_list_product(self, title, count, price):
        """добавляет товары в корзину"""
        self.product_list.append((title, count, price))
    
    def get_product_by_title(self, title):
        """возвращает продукт по названию"""
        for product in self.product_list:
            if product[0] == title:
                return product
    
    def get_product_list(self):
        return ', '.join([product[0] for product in self.product_list])

    def calculate_total(self):
        """возвращает суммарную цену всех продуктов"""
        return f'цена всех товаров в корзине: {sum(product[1] * product[2] for product in self.product_list)}'
    
    def remove_product(self, title):
        product = self.get_product_by_title(title)
        if product is not None:
            if product[1] == 1:
                self.product_list.remove(product)
                print(f'Удалено: {title}')
            elif product[1] > 1:
                title, count, price = product
                self.product_list.remove(product)
                self.add_list_product(title, count-1, price)
                print(f'Сейчас в корзине: {self.get_product_by_title(title)}')
        else:
            print(f'Все {title} удалены!')

class FailedClientID(Exception):
    pass

class Shop:
    """магазин, который работает с клиентами и их покупками"""
    def __init__(self):
        # используется для хранения клиентов и их корзин покупок
        self.customers = {}
    
    def add_customer(self, customer, shopping_cart):
        """позволяет добавлять клиента и его корзину покупок в магазин"""
        self.customers[customer.client_id] = shopping_cart
    
    def get_order_shopping(self, client_id):
        """возвращает общую стоимость всех товаров в корзине покупок клиента по его ID"""
        if client_id in self.customers:
            return f'Клиент {client_id} : {self.customers[client_id].calculate_total()}'
        else:
            raise FailedClientID(f'Корзины покупок для клиента c id={client_id} не найдено!')
    
    def get_shopping_customer(self, client_id):
        "возвращает список товаров клиент по его ID"
        if client_id in self.customers:
            return f'Клиент {client_id}, список продуктов: {self.customers[client_id].get_product_list()}'
        else:
            raise FailedClientID(f'Корзины покупок для клиента c id={client_id} не найдено!')


if __name__ == '__main__':
    try:
        customer1 =Customer('Pert', 42, 'Мск')
        customer2 =Customer('Sveta', 30, 'Спб')
        customer3 =Customer('Vova', 25, 'Екб')
        shoppingCard1 = ShoppingCart()
        shoppingCard1.add_list_product('яблоки', 2, 10)
        shoppingCard1.add_list_product('вода', 3, 20)
        shoppingCard2 = ShoppingCart()
        shoppingCard2.add_list_product('хлеб', 2, 10)
        shoppingCard2.add_list_product('виноград', 1, 30)
        shop = Shop()
        shop.add_customer(customer1, shoppingCard1)
        shop.add_customer(customer2, shoppingCard2)
        # print(shop.customers)
        print(shop.get_order_shopping(customer1.client_id))
        print(shop.get_order_shopping(customer2.client_id))
        print(shop.get_shopping_customer(customer1.client_id))
        print(shop.get_shopping_customer(customer2.client_id))
        print(shop.get_shopping_customer(customer3.client_id))       
        print(shop.get_order_shopping(customer3.client_id))
    except FailedClientID as fa_id:
        print(fa_id)
    except Exception as ex:
        print(f'Иная ошибка {ex}')
