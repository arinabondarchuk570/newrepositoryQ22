from abc import ABC, abstractmethod


class Pizza:
   # price = {"small": 10, "medium": 15, "large": 20}

    def  __init__(self, size: str, ingredients: list[str], base_price: float):
        self._size = size
        self._base_price = base_price
        self._ingredients = self.add_ingredients(ingredients)

    def get_ingredients(self):
        return self._ingredients

    def add_ingredients(self, ingredients):
        if len(ingredients) < 10:
           return ingredients
        else:
            print("Ингридиентов не может быть больше 10")
            return ['Сыр']

    def calculate_price(self):
        return self._base_price + len(self._ingredients)

    def __str__(self):
        return "Pizza"

class SmallPizza(Pizza):

    def __init__(self, ingredients, size = "small", base_price = 10):
        super().__init__( size, ingredients, base_price)

class MediumPizza(Pizza):

    def __init__(self,ingredients,  size = "medium", base_price = 15):
        super().__init__( size, ingredients, base_price)

class LargePizza(Pizza):

    def __init__(self, ingredients, size = "large", base_price = 20):
        super().__init__( size, ingredients, base_price)

class MeatPizza(Pizza):

    def calculate_price(self):
        return (self._base_price + len(self._ingredients)) * 1.2

    def str(self):
        return "meat"

class VegetablePizza(Pizza):

    def calculate_price(self):
        return (self._base_price + len(self._ingredients)) * 0.9

    def str(self):
        return "vegetable"

class Order(ABC):
    @abstractmethod
    def prepare(self):
        pass

class PizzaOrder(Order):

    def __init__(self, pizza: Pizza):
        self._pizza = pizza
    def prepare(self):
        print(f"Готовим пиццу {self._pizza.__str__()} {self._pizza._size}: Цена {self._pizza.calculate_price()}$")

pizza = LargePizza(ingredients=['Сыр', 'Грибы', 'Ветчина'])
order = PizzaOrder(pizza)
order.prepare()
