from abc import ABC, abstractmethod
class AbstractProductA(ABC):
    @abstractmethod
    def function_product_a(self) -> None:
        raise NotImplementedError

class AbstractProductB(ABC):
    @abstractmethod
    def function_product_b(self) -> None:
        raise NotImplementedError

    def another_function_product_b(self, product: AbstractProductA) -> str:
        raise NotImplementedError
