# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров.
# Ваша задача — создать класс `Store`, который можно будет использовать для создания различных магазинов.
# Шаги:
# 1. Создай класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
#
# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
#
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
#
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.

class Store:
    def __init__(self, name, address, items):
        self.name = name
        self.address = address
        self.items = {
    'apples': 0.5,
    'bananas': 0.75,
    'oranges': 0.65,
    'grapes': 2.0,
    'pears': 1.2
}
        self.adds = []

    def adds(self, items):
        add = Store(items)
        self.adds.append(add)

    def deletes(self, items):
        delete = Store(items)
        self.remove(delete)

    def clears(self, items):
        clear = Store(items)
        self.clear(clear)

    def prices(self, items):
        price = Store(items)
        self.get(price)
