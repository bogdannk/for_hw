"""HW OOP"""


class Apple:

    def __init__(self, variety, age, height, weight):
        self.variety = variety
        self.__age = age
        self.height = height
        self.weight = weight

    def grow(self):
        return f'I will grow'

    def get_age(self):
        return f' my age is {self.__age}'

    def set_age(self, new_age):
        self.__age = new_age



apple1 = Apple("Semerinka", 3, 15, 0.35)

print(apple1.get_age())
apple1.set_age(4)
print(apple1.get_age())
apple1.variety = "Chempion"
print(apple1.variety)
class Old_Apple(Apple):

    def __init__(self,variety, age, height, weight, price):
        super().__init__(variety, age, height, weight)
        self._price = price

    def get_price(self):
        return f'I am cost {self._price} $'

    def set_price(self, new_price):
        self._price = new_price

apple2 = Old_Apple("Golden", 10, 12, 1, 100)

print(apple2.get_price())

