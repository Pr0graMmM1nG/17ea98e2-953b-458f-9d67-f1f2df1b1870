from abstract.factory import AbstractFactory

def code(factory: AbstractFactory):
    productA = factory.create_product_a()
    productB = factory.create_product_b()

    productA.function_product_a()
    productB.function_product_b()