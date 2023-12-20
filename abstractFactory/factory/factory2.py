from abstract.factory import AbstractFactory
from abstract.product import AbstractProductA, AbstractProductB
from product.productA import ConcreteProductA2
from product.productB import ConcreteProductB2

class ConcreteFactory2(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()