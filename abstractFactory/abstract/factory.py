from abc import ABC, abstractmethod
from abstract.product import AbstractProductA, AbstractProductB

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        raise NotImplementedError

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        raise NotImplementedError