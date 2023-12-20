from abstract.product import AbstractProductA, AbstractProductB

class ConcreteProductB1(AbstractProductB):
    def function_product_b(self) -> None:
        print("Result: Concret product B1")

    def another_function_product_b(self, product: AbstractProductA) -> str:
        product.function_product_a()
        return "Result: Product B1 intersect Product A"

class ConcreteProductB2(AbstractProductB):
    def function_product_b(self) -> None:
        print("Result: Concret product B2")

    def another_function_product_b(self, product: AbstractProductA) -> str:
        product.function_product_a()
        return "Result: Product B2 intersect Product A"