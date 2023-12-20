from abstract.factory import AbstractFactory
from abstract.product import AbstractProductA, AbstractProductB
from product.productA import ConcreteProductA1
from product.productB import ConcreteProductB1


class ConcreteFactory1(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()